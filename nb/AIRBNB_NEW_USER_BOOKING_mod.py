# load package
import datetime
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import mpld3

def draw_trend(train, which, lab = '', var = 'date_first_booking'):
    
    f, ax = plt.subplots(figsize = (12,3))

    trend_group = train.groupby([var])
    trend = trend_group.size().reset_index()
    trend.columns = ['date', 'count']
    
    t = trend.copy()
    t['y'] = t.date.dt.year

    if which == 'day of year':
        # day of year
        t[which] = t.date.dt.dayofyear
        t = t.groupby(['y', which])['count'].sum().reset_index()
        m = 366
        
    elif which == 'month':
        # month
        t[which] = t.date.dt.month
        t = t.groupby(['y', which])['count'].sum().reset_index()
        m = 13
    
    elif which == 'day of month':
        # day of month
        t[which] = t.date.dt.day
        t = t.groupby(['y', which])['count'].sum().reset_index()
        m = 32
    
    elif which == 'day of week':
        # day if week
        t[which] = t.date.dt.dayofweek+1
        t = t.groupby(['y', which])['count'].sum().reset_index()
        m = 8
        
    elif which == 'hour of day':
        # hr of day
        t[which] = t.date.dt.hour
        t = t.groupby(['y', which])['count'].sum().reset_index()
        m = 24

    elif which == 'country_destination':
        trend_group = train.groupby([var, which])
        trend = trend_group.size().reset_index()
        trend.columns = ['date', which, 'count']
        t = trend.copy()
        t['y'] = t.date.dt.year
        t[which] = t[which]
        t = t.groupby(['y', which])['count'].sum().reset_index()
        m = 12
    else:
        raise ValueError('Module not built yet, please insert code in module')

    if which in ['day of year', 'month', 'day of month', 'day of week', 'hour of day']:
        newfrindex = range(m)
    else:
        newfrindex = t[which].unique().tolist()

    newframe = pd.DataFrame(index = newfrindex, columns = [x for x in range(2010,2016)])
    
    allyr = range(2010,2016)
    
    for yr in allyr:
        minitb = t[t.y == yr][[which, 'count']]
        minitb.index = minitb[which]
        minitb.drop(which, axis = 1, inplace = True)
        newframe[yr] = minitb

    newframe.fillna(0, inplace = True); 

    if lab == '':
        titlelab = ''
    else:
        titlelab = 'by %s' %lab
    ax.set_title('%s - Year Trend (%s) %s' %(var, which, titlelab))

    css = ".mpld3-tooltip{\
            background-color:rgba(255, 255, 255, .8);\
            text-align: center;\
            font-family: Calibri;\
    }"

    html = '<div>%s</div>'
    handles = []
    for yri in range(len(allyr)):
        yr = allyr[yri];        
        l = ax.plot(newframe[yr].values, marker='o', label = str(yr), lw = 2, alpha=1);
        handles.append(l);
        label_text = newframe[yr].values.tolist();
        labels = [html%('Year %i, %s %s; <br> Total %s: %i' %(yr, which, str(x), var, label_text[x])) for x in range(len(label_text))];
        tooltip = mpld3.plugins.PointHTMLTooltip(ax.get_lines()[yri], labels=labels, voffset=-10, hoffset=15, css = css);
        mpld3.plugins.connect(f, tooltip);

    ax.set_xlabel(which);
    ax.set_xlim(1,(m-1));

    if which == 'country_destination':
        ax.set_xticks(range(m));
        ax.set_xticklabels(newframe.index.tolist());
    
    labels = [str(x) for x in allyr]
    interactive_legend = mpld3.plugins.InteractiveLegendPlugin(handles,labels)
    mpld3.plugins.connect(f, interactive_legend)

    # f.tight_layout()

class transformation:
    """
    This class will transform each attribute according to the transform
    You are free to write any heuristic to help identify the transformation 
    if it's not provided as well.
    
    input:
        DataFrame
        List of transformation on each of the features:
            Feature Label:
                Transformation:
                    Id
                    Dummy
                    Date
                    Numeric
                    None
        Options:
            Scale Method (Other than Dummy Coding)
    Output:
        Numpy Matrix
        Labels of features
    """
    
    def __init__(self, df, transform):

        if len(transform) != self.m:
            raise ValueError("Transformation vector should share the same length\
                               as features in df")

        self.dummy_code_scheme = dict()
        self.df = df
        self.n = self.df.shape[0]
        self.m = self.df.shape[1]
        self.transform = transform

        # auto generate transformation on features
        self.transformation_heuristic()

    def transformation_heuristic(self, transform):
        for ti in range(self.m):
            t = transform[ti]
            feat = self.df.iloc[:, ti]
            if t is None:
                if len(feat.unique()) == self.m:
                    # unique value == row numbers
                    self.transform[ti] = 'Id'
                if feat.dtypes == '<M8[ns]':
                    # date
                    self.transform[ti] = 'Date'
                if feat.dtypes == 'float64':
                    self.transform[ti] = 'Numeric'
                else:
                    self.transform[ti] = 'Dummy'
            else:
                continue

    def is_there_unique_identifyer(self, df):
        if 'Id' in self.transform:
            return False
        else:
            return True
    
    def concat_df(self, new = False, df = None, newdf = None, axis = 1):
        # attach newdf to df
        # default by columns
        
        output = pd.DataFrame()
        if new:
            output = newdf
        else:
            output = pd.concat([df, newdf], axis = axis)
        return output
    
    def get_dummies(self, feat):
        # faster get dummies
        self.dummy_code_scheme[feat] = self.df[feat].to_dict()
        
        output = []
        n = len(self.dummy_code_scheme[feat].keys())
        
        for v in self.df[feat].values:
            row = [0 for x in range(n)]       
    
    def compress(self, transform):
        new = True
        df = pd.DataFrame()
        
        for feati in range(len(transform)):
            feat = transform[feati]
            
            if feat == 'Dummy':
                
                concat_df(new,df,)
                
            if new:
                new = False