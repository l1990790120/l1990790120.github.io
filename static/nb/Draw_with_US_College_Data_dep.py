import pandas as pd
from tqdm import *
import requests
import math


def map_css():
    css = """
    <style>
      .counties {
      fill: #D3D3D3;
    }

    .states {
      fill: none;
      stroke: #fff;
      stroke-linejoin: round;
    }

    .q0-9 { fill:rgb(247,251,255); }
    .q1-9 { fill:rgb(222,235,247); }
    .q2-9 { fill:rgb(198,219,239); }
    .q3-9 { fill:rgb(158,202,225); }
    .q4-9 { fill:rgb(107,174,214); }
    .q5-9 { fill:rgb(66,146,198); }
    .q6-9 { fill:rgb(33,113,181); }
    .q7-9 { fill:rgb(8,81,156); }
    .q8-9 { fill:rgb(8,48,107); }


    div.tooltip {
      position: absolute;
      background: #eee;
      border: 1px solid #ccc;
      padding: 10px;
      border-radius: 8px;
      box-shadow: 0 5px 10px rgba(0, 0, 0, 0.2);
      position: relative;
      width: 200px;
    }
    </style>
    """
    return css


def get_api_key():
    f = open('api.data.gov_API_key.txt')
    api_key = f.read()
    f.close()
    return '&api_key=' + api_key


def get_county_fips(x):
    api = 'http://data.fcc.gov/api/block/find?format=json&'
    lat = x.lat
    lon = x.lon
    query = 'latitude=%f&longitude=%f&showall=false' % (lat, lon)
    jsondata = requests.get(api + query).json()
    return jsondata['County']['FIPS']


def load_geo_lon_lat():
    # the api doesn't support geo coding yet, download from ipeds
    geo = pd.read_csv('unitid_lonlat.csv')
    geo.rename(columns={
        'Longitude location of institution (HD2014)': 'lon',
        'Latitude location of institution (HD2014)': 'lat',
        'UnitID': 'id'}, inplace=True)
    # geo['fips'] = geo.apply(lambda x: get_county_fips(x), axis=1)

    fips = []
    with tqdm(total=geo.shape[0]) as pbar:
        for x in geo.iterrows():
            fips.append(get_county_fips(x[1]))
            pbar.update(1)
    geo['fips'] = fips
    geo.to_hdf('d.h', 'geo', mode='a')


def get_json_df(url, return_page=False):
    jsondata = requests.get(url).json()
    if 'metadata' not in jsondata.keys():
        raise ValueError('Error message returned: %s' % jsondata)

    per_page = jsondata['metadata']['per_page']
    total = jsondata['metadata']['total']
    total_page = math.ceil(total / per_page)
    first = True

    def get_page(url, page):
        pageurl = url + '&page=%i' % page
        jsondata = requests.get(pageurl).json()
        return pd.DataFrame.from_dict(jsondata['results'])

    for x in tqdm(range(total_page)):
        if first:
            first = False
            df = pd.DataFrame.from_dict(jsondata['results'])
        else:
            t = get_page(url, x)
            df = pd.concat([df, t], axis=0)
    return df


def get_yr_query(yr):
    # api query
    url = 'https://api.data.gov/ed/collegescorecard/v1/schools?'
    # 100 records per page
    url += '_per_page=100&'
    # fields to query
    # school info
    url += '_fields=id,'
    url += 'school.name,'
    url += 'school.operating,'
    url += 'school.zip,'
    url += 'school.degrees_awarded.predominant,'
    url += 'school.ownership,'
    url += 'school.locale,'
    url += 'school.carnegie_basic,'
    url += 'school.carnegie_undergrad,'
    url += 'school.carnegie_size_setting,'
    url += 'school.online_only,'
    # everything else is year.dev-category.dev-friendly-variable-name
    # admission info
    url += '%i.admissions.admission_rate.overall,' % yr
    url += '%i.admissions.admission_rate.by_ope_id,' % yr
    url += '%i.admissions.sat_scores.average.overall,' % yr
    url += '%i.admissions.sat_scores.average.by_ope_id,' % yr
    # student demo
    url += '%i.student.size,' % yr
    url += '%i.student.demographics.race_ethnicity.white,' % yr
    url += '%i.student.demographics.race_ethnicity.black,' % yr
    url += '%i.student.demographics.race_ethnicity.hispanic,' % yr
    url += '%i.student.demographics.race_ethnicity.asian,' % yr
    url += '%i.student.demographics.race_ethnicity.non_resident_alien,' % yr
    url += '%i.student.demographics.first_generation,' % yr
    url += '%i.student.demographics.avg_family_income,' % yr
    url += '%i.student.demographics.median_family_income,' % yr
    url += '%i.student.demographics.avg_family_income_independents,' % yr
    url += '%i.student.demographics.avg_family_income_log,' % yr
    url += '%i.student.demographics.avg_family_income_independents_log,' % yr
    url += '%i.student.demographics.share_white.home_ZIP,' % yr
    url += '%i.student.demographics.share_black.home_ZIP,' % yr
    url += '%i.student.demographics.share_asian.home_ZIP,' % yr
    url += '%i.student.demographics.share_hispanic.home_ZIP,' % yr
    url += '%i.student.demographics.share_bachelors_degree_age25.home_ZIP,' % yr
    url += '%i.student.demographics.share_professional_degree_age25.home_ZIP,' % yr
    url += '%i.student.demographics.share_born_US.home_ZIP,' % yr
    # cost
    url += '%i.cost.tuition.in_state,' % yr
    url += '%i.cost.tuition.out_of_state,' % yr
    url += '%i.cost.attendance.academic_year,' % yr
    url += '%i.cost.attendance.program_year,' % yr
    url += '%i.cost.avg_net_price.public,' % yr
    url += '%i.cost.avg_net_price.private,' % yr
    # completion
    url += '%i.completion.completion_rate_4yr_150nt,' % yr
    url += '%i.completion.completion_rate_less_than_4yr_150nt,' % yr
    url += '%i.completion.completion_rate_4yr_150nt_pooled,' % yr
    url += '%i.completion.completion_rate_less_than_4yr_150nt_pooled,' % yr
    url += '%i.completion.completion_rate_4yr_150_white,' % yr
    url += '%i.completion.completion_rate_4yr_150_black,' % yr
    url += '%i.completion.completion_rate_4yr_150_hispanic,' % yr
    url += '%i.completion.completion_rate_4yr_150_asian,' % yr
    # program
    url += '%i.academics.program_percentage.agriculture,' % yr
    url += '%i.academics.program_percentage.resources,' % yr
    url += '%i.academics.program_percentage.architecture,' % yr
    url += '%i.academics.program_percentage.ethnic_cultural_gender,' % yr
    url += '%i.academics.program_percentage.communication,' % yr
    url += '%i.academics.program_percentage.communications_technology,' % yr
    url += '%i.academics.program_percentage.computer,' % yr
    url += '%i.academics.program_percentage.personal_culinary,' % yr
    url += '%i.academics.program_percentage.education,' % yr
    url += '%i.academics.program_percentage.engineering,' % yr
    url += '%i.academics.program_percentage.engineering_technology,' % yr
    url += '%i.academics.program_percentage.language,' % yr
    url += '%i.academics.program_percentage.family_consumer_science,' % yr
    url += '%i.academics.program_percentage.legal,' % yr
    url += '%i.academics.program_percentage.english,' % yr
    url += '%i.academics.program_percentage.humanities,' % yr
    url += '%i.academics.program_percentage.library,' % yr
    url += '%i.academics.program_percentage.biological,' % yr
    url += '%i.academics.program_percentage.mathematics,' % yr
    url += '%i.academics.program_percentage.military,' % yr
    url += '%i.academics.program_percentage.multidiscipline,' % yr
    url += '%i.academics.program_percentage.parks_recreation_fitness,' % yr
    url += '%i.academics.program_percentage.philosophy_religious,' % yr
    url += '%i.academics.program_percentage.theology_religious_vocation,' % yr
    url += '%i.academics.program_percentage.physical_science,' % yr
    url += '%i.academics.program_percentage.science_technology,' % yr
    url += '%i.academics.program_percentage.psychology,' % yr
    url += '%i.academics.program_percentage.security_law_enforcement,' % yr
    url += '%i.academics.program_percentage.public_administration_social_service,' % yr
    url += '%i.academics.program_percentage.social_science,' % yr
    url += '%i.academics.program_percentage.construction,' % yr
    url += '%i.academics.program_percentage.mechanic_repair_technology,' % yr
    url += '%i.academics.program_percentage.precision_production,' % yr
    url += '%i.academics.program_percentage.transportation,' % yr
    url += '%i.academics.program_percentage.visual_performing,' % yr
    url += '%i.academics.program_percentage.health,' % yr
    url += '%i.academics.program_percentage.business_marketing,' % yr
    url += '%i.academics.program_percentage.history,' % yr
    url += '%i.earnings.10_yrs_after_entry.median,' % yr
    url += '%i.earnings.6_yrs_after_entry.median,' % yr
    url += '%i.earnings.8_yrs_after_entry.median_earnings' % yr
    return url


def pull(yrs, api_key):
    for yr in yrs:
        url = get_yr_query(yr)
        df = get_json_df(url + api_key)
        df.to_hdf('d.h', 'yr_%i' % yr, mode='a')
    del df


def visualization_data_wrapper(d, geo, col, func):
    dgeo = d[['id', col]].merge(geo[['id', 'fips']], how='left')
    tb = dgeo[['fips', col]]
    tb = tb.dropna()
    byfips = tb.groupby('fips')[col].apply(func).reset_index()
    byfips.rename(columns={col: 'value'}, inplace=True)
    byfips['fips'] = byfips['fips'].astype('int')
    return byfips


def d3_choropleth_generator(d, geo, col, func, title, div_id):

    draw = visualization_data_wrapper(
        d, geo, col, func)

    js = "var "+ div_id + " = eval(\'" + draw.to_json(orient='records') + "\');" + """
        requirejs.config({
            paths: {
                'd3': ['//cdnjs.cloudflare.com/ajax/libs/d3/3.5.6/d3'],
                'topojson': ['https://cdnjs.cloudflare.com/ajax/libs/topojson/1.6.20/topojson'],
                'math': ['https://cdnjs.cloudflare.com/ajax/libs/mathjs/3.2.1/math']
            }
        });
        require(['d3', 'topojson', 'math'], function(d3, topojson, math) {
            var width = 960;
            var height = 500;

            // create d3.map from data
            var rateByid = d3.map();
            """ + div_id + """.map(function(d) {  rateByid.set(d.fips, d.value)  });

            // initialize map
            var canvas = d3.select( \'#""" + div_id + """\' );
            canvas.select( 'svg' ).remove();
            var svg = canvas.append( 'svg' )
                .attr("width", width)
                .attr("height", height);

            var projection = d3.geo.albersUsa()
                .scale(1000)
                .translate([width / 2, height / 2]);

            var path = d3.geo.path()
                .projection(projection);

            var color = d3.scale.quantize()
                .domain(  [d3.min(""" + div_id + """, function(d) { return d.value; }),
                            d3.max(""" + div_id + """, function(d) { return d.value; })  ])
                .range(d3.range(9).map(function(i) { return "q" + i + "-9"; }));

            // create title
            var title = d3.select( \'#""" + div_id + """\' ).select( 'h3' )
                .text(\'""" + title + """\');

            // add tooltip
            var div = d3.select( \'#""" + div_id + """\' ).append("div")   
                .attr("class", "tooltip")               
                .style("opacity", 0);

            // draw map
            d3.json("USA.json", function(error, us) {
                if (error) throw error;

                svg.append("g")
                    .attr("class", "counties")
                    .selectAll("path")
                    .data(topojson.feature(us, us.objects.counties).features)
                    .enter().append("path")
                    .attr("class", function(d) { return color( rateByid.get(d.id) )
                        })
                    .attr("d", path)
                    .style("opacity", 0.8)

                    //Adding mouseevents
                    .on("mouseover", function(d) {
                        if (rateByid.has(d.id)) {
                            d3.select(this).transition().duration(300).style("opacity", 1);
                            div.transition().duration(300)
                            .style("opacity", 1)
                            div.text( 'FIPS ' + d.id + ' : ' +
                                Number(  (rateByid.get(d.id)).toFixed(2)  ) )
                            .style("left", width-300 + "px")
                            .style("top", -height-30 + "px")
                            } else {div.style("opacity", 0)}
                    })
                    .on("mouseout", function() {
                        d3.select(this)
                        .transition().duration(300)
                        .style("opacity", 0.8);
                        div.transition().duration(300)
                        .style("opacity", 0);
                    });
                svg.append("path")
                    .datum(topojson.mesh(us, us.objects.states, function(a, b) { return a !== b; }))
                    .attr("class", "states")
                    .attr("d", path);
            });

            // legend
            var legend = svg.selectAll("g.legend")
                .data(color.range())
                .enter().append("g")
                .attr("class", "legend");

            var ls_w = 20, ls_h = 20;

            legend.append("rect")
                .attr("x", 20)
                .attr("y", function(d, i){ return height - (i*ls_h) - 2*ls_h;})
                .attr("width", ls_w)
                .attr("height", ls_h)
                .attr("class", function(d, i) { return d; })
                .style("opacity", 0.8);

            legend.append("text")
                .attr("x", 50)
                .attr("y", function(d, i){ return height - (i*ls_h) - ls_h - 10;})
                .text(function(d, i){
                    var r = color.invertExtent(d);
                    return Number((r[1]).toFixed(2))

                });

            d3.select(self.frameElement).style("height", height + "px");

        }) """
    return js
