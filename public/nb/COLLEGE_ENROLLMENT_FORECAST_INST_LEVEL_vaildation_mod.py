from statsmodels.tsa.arima_model import ARIMA
from tqdm import *
import matplotlib.pyplot as plt
import numpy as np

class predict_by_cluster:
    """
    The class establish a pipeline to manipulate cluster -> forecast module and 
    parametrize key manipulating variables to validate error.
    
    ds: dataset (row(Period) x columns(attribute))
    
    Scaling:
    rebase_to_n = 0: rebase to latest n period, use 0 to scale to the first period.
    
    Clustering:
    cluster_method = 'gmm': gmm or kmeans
    n_clusters = (n/2)^(.5): n clusters
    cluster_n_period = 0: cluster the last n period, use 0 to use all history available
    seed = 27914004: random seed to produce repeatable result
    
    Validation:
    n_ahead = 2: predict n period ahead
    hold_out_n = 2: hold out n period for validation, use 0 to do prediction. If >0, n_ahead = hold_out_n.
    
    Forecasting:
    exog = None: please specify exog if available
    order = (1, 0, 0): ARIMA (p, d, q) order
    """
    
    def __init__(self, ds, rebase_to_n = 0, 
                 cluster_method = 'gmm', n_clusters = 0, cluster_n_period = 0, seed = 27914004,
                 n_ahead = 2, hold_out_n = 2, 
                 exog = None, order = (1, 0, 0)):
        
        # init vars
        self.ds = ds
        # Scaling
        self.scale(rebase_to_n)
        # create self.ds_s, use this going forward
        
        # Clustering
        if n_clusters == 0:
            # use default
            n_clusters = int((ds.shape[1] / 2)**(.5))
        self.n_clusters = n_clusters
        self.cluster_n_period = cluster_n_period
        self.seed = seed
        self.cluster(cluster_method, self.n_clusters, cluster_n_period)
        # create self.ds_c, cluster based on the scaled data
        
        # Validation
        # Forecasting
        self.current = int(str(ds.index[-1]))
        
        self.aggregate_by_cluster()
        # aggregate the cluster enrollment by real data
        # create self.ds_agg_by_c, a matrix with row = periods and columns = cluster agg result
        
        self.hold_out_n = hold_out_n
        if hold_out_n > 0:
            self.n_ahead = self.hold_out_n
        else:
            self.n_ahead = n_ahead

        self.forecast_by_cluster(hold_out_n, n_ahead, order, exog)
        # create self.ds_c_for, a matrix with row = forecasted period and columns = cluster n
        
        self.disaggregate_by_cluster()
        # disaggregate the trend by institute size
        # create self.ds_for

        if hold_out_n > 0:

            # print error

            print('WMAPE on Cluster')
            self.cwmape, self.cape = self.report_wmape(self.ds_agg_by_c[-self.hold_out_n:, :], self.ds_c_for)
            # wmape of cluster forecast

            print('WMAPE on Institution')
            self.iwmape, self.iape = self.report_wmape(self.ds.iloc[-self.n_ahead:, :].values, self.ds_for.iloc[-self.n_ahead:, :].values)
            # wmape of real forecast

    def get_forecast(self):
        return self.ds_for

    def scale(self, rebase_to_n):
        from sklearn.preprocessing import MinMaxScaler
        scaler = MinMaxScaler()
        ds_scaled = scaler.fit_transform(self.ds)
        if rebase_to_n == 0:
            ds_scaled = ds_scaled - ds_scaled[0,:]
        else:
            ds_scaled = ds_scaled - ds_scaled[-rebase_to_n,:]
        self.ds_s = ds_scaled
    
    def cluster(self, cluster_method, n_cluster, cluster_n_period):
        from sklearn.mixture import GMM
        from sklearn.cluster import KMeans

        if cluster_method == 'gmm':
            m = GMM(n_components=n_cluster, covariance_type='full', random_state = self.seed)
        else:
            m = KMeans(n_clusters = n_cluster, random_state = self.seed,  n_jobs=-1)
        
        ds_c = np.zeros((1,self.ds.shape[1]))
        dfit = self.ds_s.transpose()
        
        if cluster_n_period > 0:
            dfit = dfit[:,-cluster_n_period:]

        m.fit(dfit)
        ds_c = m.predict(dfit)
        
        self.ds_c = ds_c
 
    ### drawing ###

    def draw_cluster_error(self):
        if self.n_clusters > 1000:
            print('too many clusters, will take a longer time to draw (Y/n)')
            response = input()
            if input == 'n':
                return None
        f, ax= plt.subplots(3, 1, figsize = (15,9));

        # cluster aggregate error
        ax[0].plot(self.cape[0], '-o');
        ax[0].plot(self.cape[1], '-o');
        ax[0].legend(self.ds.index[-2:].tolist());
        ax[0].set_title('CLUSTER AGGREGATE ERROR')

        # institute within cluster error
        institute_cluster_within_error = []
        cluster_size = []
        for c in range(self.n_clusters):
            true = self.ds.iloc[-self.n_ahead:, self.ds_c == c].values
            forecast = self.ds_for.iloc[-self.n_ahead:, self.ds_c == c].values
            cwmape, iape = self.report_wmape(true, forecast, print_error = False)
            institute_cluster_within_error.append(cwmape)
            cluster_size.append(np.sum(true, axis = 1))

        error = np.array(institute_cluster_within_error).transpose()
        ax[1].plot(error[0], '-o');
        ax[1].plot(error[1], '-o');
        ax[1].set_title('WITHIN CLUSTER ERROR');

        size = np.array(cluster_size).transpose();
        ax[2].plot(np.sum(size, axis = 0), '-o');
        ax[2].set_title('CLUSTER SIZE');
        ax[2].legend(['CLUSTER SIZE'], loc = 'upper left');

        for x in ax:
            x.set_xticks(range(self.n_clusters));
            x.set_xlim(0, self.n_clusters);
            x.set_xticklabels(range(self.n_clusters), rotation=90)

        ax2 = ax[2].twinx();
        ax2.plot(np.bincount(self.ds_c), '-o', color = 'green');
        ax2.legend(['NUMBER OF INSTITUTION'], loc = 'upper right');

        f.tight_layout();

    def draw_trend(self, *args, one = False):
        n_fig = len(args)
        if one:
            figsize = (15,3)
            m = 1
            n = 1
        else:
            figsize = (15,n_fig*2)
            m = n_fig
            n = 2

        f, ax= plt.subplots(m,n, figsize = figsize);

        for x in range(n_fig):
            if not(one):
                ax[x][0].plot(self.ds.iloc[:,args[x]]);
                ax[x][1].plot(self.ds_s[:,args[x]]);
                ax[x][1].set_title('School - %i (Scaled)'%x)
            if x < n_fig:
                if one:
                    ax.plot(self.ds_s[:,args[x]]);
                    ax.set_title(args)
                else:
                    ax[n_fig-1][1].plot(self.ds_s[:,args[x]]);

        f.tight_layout()
    
    def draw_cluster_trend(self, n, n_trend = 5):
        self.draw_trend(np.where(self.ds_c == n)[0][:n_trend], one = True)

    def look_at_institute(self, n):
        fig, ax = plt.subplots(figsize = (15,3))
        ax.plot(self.ds.iloc[:,n])
        ax.plot(self.ds_for.iloc[:,n])
        ax.set_title('School %i Forecast versus True (Disaggregated from cluster %i)' %(n, self.ds_c[n]))
        ax.legend(['True', 'Forecast'], loc = 'upper left')
        ax.set_xticks(range(self.ds.shape[0]))
        ax.set_xticklabels([str(x) for x in self.ds.index])

        ax2 = ax.twinx()
        ax2.plot(self.ds_agg_by_c[:, self.ds_c[n]], color = 'Orange')
        ax2.legend(['Cluster Trend'], loc = 'upper center')

    def aggregate_by_cluster(self):
        self.ds_agg_by_c = np.zeros((self.ds.shape[0], self.n_clusters))

        for c in range(self.n_clusters):
            agg = self.ds.iloc[:, np.where(self.ds_c == c)[0]]
            self.ds_agg_by_c[:,c] = np.sum(agg, axis = 1)

    def forecast_by_cluster(self, hold_out_n, n_ahead, order, exog):
        dfit = self.ds_agg_by_c
        
        efit = efor = None
        if hold_out_n > 0:
            # hold out validation required
            dfit = dfit[:-hold_out_n]
            if (exog is not None):
                efit = exog[:-hold_out_n]
                efor = exog[-hold_out_n:]
        else:
            if (exog is not None):
                efit = exog[:-n_ahead]
                efor = exog[-n_ahead:]
        ds_c_for = np.zeros((n_ahead, self.n_clusters))

        for c in tqdm(range(self.n_clusters)):
            cdfit = dfit[:,c]
            if sum(cdfit) == 0:
                ds_c_for[:,c] = 0
                continue
            m = ARIMA(cdfit, exog = efit, order = order)
            mf = m.fit()
            f = mf.forecast(n_ahead, exog = efor, alpha = .95)[0]
            ds_c_for[:,c] = f
        
        self.ds_c_for = ds_c_for

    def disaggregate_by_cluster(self):
        """
        Calculate the ratio by total enrollment in cluster_n_period
        Why not do period basis?
        If forecasting forward, there's no future enrollment available, therefore,
        no way to calculate weight
        to calculate weight by current period, might seem cheating in validation
        """
        # wt = np.zeros((1, self.ds.shape[1]))
        # total = np.zeros((self.n_ahead, self.ds.shape[1]))
        
        agg_cluster_ds = np.zeros((self.n_ahead+1, self.n_clusters))
        agg_cluster_ds[0] = self.ds_agg_by_c[-1]
        agg_cluster_ds[1:] = self.ds_c_for
        cluster_perc_change = np.diff(agg_cluster_ds, axis = 0) / agg_cluster_ds[:-1]

        cluster_scaling_vector = np.zeros((2, self.ds.shape[1]))

        # break down proportionally -> don't work well
        # for c in range(self.n_clusters):
            # c_m = self.ds.iloc[-self.cluster_n_period:, np.where(self.ds_c == c)[0]]
            # c_sum = sum(c_m)
            # indiv_sum = np.sum(c_m, axis = 0)
            # wt[:,np.where(self.ds_c == c)[0]] = (indiv_sum/c_sum)
            # total[:,np.where(self.ds_c == c)[0]] = np.reshape(
            #     np.repeat(self.ds_c_for[:,c], c_m.shape[1]), (self.n_ahead, c_m.shape[1]))
            
        # multiply by the perc change
        
        for i in range(self.ds_c.shape[0]):
            cluster_scaling_vector[:,i] = cluster_perc_change[:,self.ds_c[i]]
        cluster_scaling_vector = cluster_scaling_vector+1
        cluster_scaling_vector = np.array(cluster_scaling_vector)
        
        self.ds_for = self.ds.copy()

        for yr in range(self.n_ahead)[::-1]:
            # forecast on foretasted number
            yr_ind = self.ds_for.index[-(yr+1)]
            self.ds_for.ix[yr_ind] = self.ds_for.iloc[-(yr+2),:].values * cluster_scaling_vector[-(yr+1)]

        # self.ds_for.iloc[-(self.n_ahead):,:] = self.ds_for.iloc[-(self.n_ahead+1):-1,:].values * np.array(cluster_scaling_vector)

        # if negative -> 0
        self.ds_for[self.ds_for < 0] = 0

    def rescale(self):
        """
        f_scale(x) = (x_scaled)

            max(x) - min(x)
        x * --------------- - x[rebase_to_n] = x_scaled
                 max(x)
        f_scaled^(-1)(x_scaled) = (x) (Inverse Function)
                                             max(x)
        x = x_scaled + x[re_base_to_n] * ---------------
                                         max(x) - min(x)
        
        Note: if the rebase_to_n is less than hold_out_n, you would be
        forecasting the base, in that case, it will be rescale back to
        original enrollment using forecasted base, and might be different
        from what it was.

        Note: The max/min is referring to the max/min prior or equal to current
        """
        # forecast on real data, don't need this anymore
        pass

    def wmape(self, true, forecast):
        true_ = true.copy()
        true_[true_ == 0] = np.inf
        try:
            forecast[np.isnan(forecast)] = 0
        except TypeError:
            pass
        wmape = np.sum((true * (abs(true - forecast)/true_)), axis = 1) / np.sum(true, axis = 1)
        ape = abs(true - forecast)/true_
        return wmape, ape

    def report_wmape(self, true, forecast, print_error = True):
        wmape, ape = self.wmape(true, forecast)
        for p in range(1,(self.hold_out_n+1))[::-1]:
            if print_error:
                print('WMAPE of %s = %f' %(str(self.ds.index[-p]), wmape[-p]))
        return [wmape, ape]

    def adaptive_fit(self):
        """
        heuristic:
        if following the trend does not make sense in the last n_ahead period,
        forecast by the individual trend instead
        """