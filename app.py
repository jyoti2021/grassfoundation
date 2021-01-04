import numpy as np
import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
from flask import Flask
import os
from dash.dependencies import Input, Output, State


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__,external_stylesheets=external_stylesheets)
server = app.server
#app.config.supress_callback_exceptions = True
prefix = ''

if os.getenv('DASH_APP_NAME'):
    prefix = '/{0}/'.format(os.getenv('DASH_APP_NAME'))

app.config.update({
 	# remove the default of '/'
 	'routes_pathname_prefix': prefix,
 	# remove the default of '/'
 	'requests_pathname_prefix': prefix,
})


textBoxStyle = {"height": "auto", "margin-bottom": "auto",'fontWeight':'bold','fontSize':'0.9rem','text-align':'auto'}
logoStyle = {'height': '10%','width': '10%','margin':'auto','display':'inline-block'}
headingStyle = {'textAlign': 'center', 'color':'rgb(0,0,0)', 'margin':'auto' }
headingStyle2 = {'textAlign': 'center', 'color':'rgb(0,0,0)', 'margin':'auto','font-style': 'italic'}

population = pd.read_excel(open('.//files//'+'Population.xlsx', 'rb'),sheet_name='Sheet1',engine='openpyxl')
target_5 = pd.read_excel(open('.//files//'+'Target_5_Population.xlsx', 'rb'),sheet_name='Sheet1',engine='openpyxl')
target_10 = pd.read_excel(open('.//files//'+'Target_10_Population.xlsx', 'rb'),sheet_name='Sheet1',engine='openpyxl')
target_15 = pd.read_excel(open('.//files//'+'Target_15_Population.xlsx', 'rb'),sheet_name='Sheet1',engine='openpyxl')
target_20 = pd.read_excel(open('.//files//'+'Target_20_Population.xlsx', 'rb'),sheet_name='Sheet1',engine='openpyxl')
target_25 = pd.read_excel(open('.//files//'+'Target_25_Population.xlsx', 'rb'),sheet_name='Sheet1',engine='openpyxl')


app.layout = html.Div(
    [
        # html.Div([
        # html.Img(src=app.get_asset_url('Logo.jpeg'),style = {'display': "inline-block",'justifyContent':'right','width':'30%','height':'5%'})],style = dict(display='flex', justifyContent='center')),
        html.H1('GRASS FOUNDATION',style={'textAlign': 'center', 'color':'#77dd77', 'margin':'auto','fontSize':'5em'}),
        html.Br(),
        html.Br(),
        html.H3('World’s Population – Tragedy to Target',style={'textAlign': 'center', 'color':'rgb(0,0,0)', 'margin':'auto','fontSize':'2em'}),
        html.Br(),
        html.H4('What is needed?',style={'textAlign': 'center', 'color':'rgb(0,0,0)', 'margin':'auto','fontSize':'1.5em'}),
        html.Br(),
        html.Div([
        html.P('If you are told that you are holding a ticking bomb, what would be your first reaction? You will just throw it impulsively because you don’t know what to do with it. And if you are told that there is a green button to stop it. You will press that button immediately. This is exactly the situation with world’s population. It is a ticking bomb with a green button because we know what is needed here. Irony is we are moving aimlessly because we are not realizing that we are holding a ticking bomb or we don’t even know what to do and which direction to take.'),
        html.Br(),
        html.P('This report is an attempt to give a targeted direction for desired population for each country.'),
        html.Br(),
        html.P('Today, whatever actions or measures we take for the betterment of humanity become ineffective. These actions may be in the form of grants, innovations, philanthropic activities, and so forth. There is hardly any visible impact because we are too many. On the contrary, because of overpopulation, there is upsurge to insecurity, incivility, aggression, depression, poverty, greed, etc. amongst the larger section of the population.'),
        html.Br(),
        html.P('Rather than blaming past generations, governments, world agencies or their actions or behaviors and rather than bellowing to reduce population, we must set a target on how much to reduce, by when to reduce and how to reduce. There is some good news that population is becoming stable in many parts of the world including India . Which means we are just replacing the existing numbers and that is not a solution  to any existing problem caused by population explosion.'),
        html.Br(),
        html.P('We need to have a targeted approach, in the same manner as we go on drives for a specific disease eradication such as Polio or Malaria. Awareness plus execution is needed to convert this tragedy of over population to targeted population. For which we need to know the target and then decide on how much to produce, migrate etc. and in how much time span.'),
        html.Br(),
        html.P('Let us attempt to reduce population in a directional manner as our contribution to save mother earth because survival is the basic requirement. If we could survive only then we will thrive.'),
        ],style = {'backgroundColor':'#CEFFC9','margin': 'auto','width':'80%','padding':'10px'},),
        html.Br(),
        html.Div([
            html.Div([
	        html.Div([html.H5('Group Type'),
            dcc.Dropdown(id = 'type-drop', options = [{'label':str(ix).upper(), 'value':ix,} for ix in sorted(population['Type'].unique())] ,value = [],
            style={"display":"block",'textAlign':'center'},
            searchable = True,
            multi = False
            )]
            ,style={"width": '30%', 'display': "inline-block",'justifyContent':'center','padding':'1%'}),
            html.Div([html.H5('Country/Region'),
            dcc.Dropdown(id = 'reg-drop', options = [] ,value = [],
            style={"display":"block",'textAlign':'center'},
            searchable = True,
            multi = False
            )]
            ,style={"width": '40%', 'display': "inline-block",'justifyContent':'center','padding':'1%'}),
            html.Div([html.H5('Start Year'),
            dcc.Dropdown(id = 'year-drop', options = [{'label':ix, 'value':ix} for ix in range(1950,2001,10)] ,value = [],
            style={"display":"block",'textAlign':'center'},
            searchable = True,
            multi = False
            )]
            ,style={"width": '10%', 'display': "inline-block",'justifyContent':'center','padding':'1%'}),
            ],style = dict(display='flex', justifyContent='center')),
            html.Br(),
            html.Div([html.Button('Submit', style={"height": "auto", "margin-bottom": "auto",
              'font-weight': 'bold','backgroundColor':'#CEFFC9','color':'black','border':'black solid','fontSize':'1em'},
	                              id='button'), ],style=dict(display='flex', justifyContent='center')),
            html.Br(),
	        html.Div(id="prediction-out", style={'margin':'auto','width':'80%'}),
            html.Br(),
            html.Br(),
            html.Div([html.Button('Additional Information', style={"height": "auto", "margin-bottom": "auto",
              'font-weight': 'bold','backgroundColor':'#CEFFC9','color':'black','border':'black solid','fontSize':'1em'},
	                              id='add-button'), ],style=dict(display='flex', justifyContent='left')),

            html.Br(),
	        html.Div([
            html.Div([
            html.H6('Source of Data:',style = {'fontWeight':'bold'}),
            html.Br(),
            html.P([html.Span("The data in this report is primarily sourced from United Nations’ databases namely "),html.A('https://population.un.org/wpp/',href = 'https://population.un.org/wpp/'),html.Span(' ; '),html.A('https://data.un.org/Search.aspx?q=population',href='https://data.un.org/Search.aspx?q=population'),html.Span(" and various topic related news, reports and analysis available on open sources.")]),
            ],style = {'backgroundColor':'#CEFFC9','margin': 'auto','width':'80%','padding':'10px'},),
            html.Br(),
            html.Div([
            html.H6('How to Use Live Graphs:',style = {'fontWeight':'bold'}),
            html.Br(),
            html.Ul('* Click on Group Type and choose a group given in the dropdown list.'),
            html.Ul('* Once a group is selected, click on Country/Region to choose a country or region.'),
            html.Ul("* Last list is of Start Year for the graph, you may choose a year to see the trend along with target data or just the target data."),
            ],style =  {'backgroundColor':'#CEFFC9','margin': 'auto','width':'80%','padding':'10px'}),
            html.Br(),
            html.Div([
            html.H6('Assumptions:',style = {'fontWeight':'bold'}),
            html.Br(),
            html.P('We have made following assumptions for calculating the target population and fertility rate:'),
            html.Br(),
            html.Ul('* There is an understanding that we are three (3) times more than the required population on this planet. Therefore, we have taken this assumption as a base for our calculation purposes. '),
            html.Ul('* The population density of all the countries is considered to be constant across all regions for our calculations.'),
            html.Ul("* The population decrease year wise is based on exponential decrease. The exponential factor is calculated for each region and scenario keeping targeted years’ intervals as: 5,10,15,20,25 years hence."),
            html.Ul('* The death rate calculation for future years (2020-2045) is based on the medium variant of CRUDE_DEATH_RATE.'),
            html.Ul('* The population line in our graph has the estimated population year wise (1950 to 2020) from the TOTAL_POPULATION data and the future years are based on the medium variant prediction of population for the specific region.'),
            html.Ul('* The ratio of fertile female (Mother) population to total population is assumed to be constant across all the future years. This may be debatable as future fertility plays a major role. However, due to lack of required data, we have to work around with this fixed ratio.'),
            html.Ul('* The data is calculated for 251 regions while there was insufficient data for 34 regions which accounts for 1.13M population so not much impacting overall target numbers.')
            ],id = 'assumption',style =  {'backgroundColor':'#CEFFC9','margin': 'auto','width':'80%','padding':'10px'}),
            html.Br(),
            html.Div([
            html.H6('Disclaimer:',style = {'fontWeight':'bold'}),
            html.Br(),
            html.Ul('* This report is an attempt to give a targeted direction for desired population for each country. Many data sets for our study are not available to us. Therefore, projected data may vary hugely from actual future population.'),
            html.Ul('* We have made many assumptions for our calculations. If reader(s) of this report has access to better and more reliable assumptions and data sets, we are open to revise our calculations.'),
            html.Ul("* The purpose of this report is to initiate a direction driven approach for managing future population. The calculations are ball park figures. Therefore, readers of this report are requested to use their own judgement while using this data. We do not take any responsibility of an impact (positive or negative) on anyone using our report for current or future plans.")
            ],id = 'disclaimer',style =  {'backgroundColor':'#CEFFC9','margin': 'auto','width':'80%','padding':'10px'}),
            html.Br(),
            html.Div([
            html.H6('Appeal To Users:',style = {'fontWeight':'bold'}),
            html.Br(),
            html.P(['Here is an appeal by Mr. David Attenborough  to save our plant in many ways ',html.A('Click here', href='https://www.youtube.com/watch?v=a8hhAfSPBq8')]),
            html.P([html.Span("It is recommended for everyone to watch "),html.Strong('A Life On Our Planet'),html.Span(" available on Netflix and YouTube, a movie on humanity's impact on nature and a message of hope for future generations.")]),
            ],style = {'backgroundColor':'#CEFFC9','margin': 'auto','width':'80%','padding':'10px'},),
            html.Br(),
            html.Div([
            html.H6('About Authors:',style = {'fontWeight':'bold'}),
            html.P('The authors of this report are:'),
            html.Br(),
            html.P([html.Strong('Jyoti Khetarpal'),html.Span(' - The idea of this effort is initiated by Jyoti because this cause is very close to her heart since childhood.')]),
            html.P([html.Span('About Jyoti Khetarpal:',style = {'font-style':'italic'}),html.Span(' Jyoti is an India qualified Chartered Accountant with over 20 years of corporate experience with reputed organizations like Dun & Bradstreet and American Express. She has been instrumental in providing industry solutions, outlining risk mitigation & management methodology and creating better places to work. She is a speaker, writer, leader and driving force for any organization.')]),
            html.A('https://www.linkedin.com/in/jyotikhetarpal/',href = 'https://www.linkedin.com/in/jyotikhetarpal/'),
            html.Br(),
            html.Br(),
            html.P([html.Strong('Ramendra Singla'),html.Span(' - Special thanks to Ramendra, our young Data Scientist, for his efforts in analyzing the data in right perspective.')]),
            html.P([html.Span('About Ramendra Singla:',style = {'font-style':'italic'}),html.Span(' Ramendra is a final year student pursuing his B.Tech in Computer Science from IP University, Delhi. He has completed multiple internships in the field of Data Science from S&P Global Market Intelligence and finalist in Smart India Hackathon 2019, specializing in data analysis, machine learning and python development. He is an asset to any project involving data science and data analysis.')]),
            html.A('https://www.linkedin.com/in/ramendrasingla/',href = 'https://www.linkedin.com/in/ramendrasingla/')
            ],style =  {'backgroundColor':'#CEFFC9','margin': 'auto','width':'80%','padding':'10px'}),
            html.Br(),
            html.Div([
            html.H6('Contact Us:',style = {'fontWeight':'bold'}),
            html.Br(),
            html.Ul(['* For any queries or suggestions, please contact us at ',html.A('info@briskcheck.com',href = 'mailto:info@briskcheck.com'),'. You will hear back from us in less than 24 hours.']),
            html.Ul(['* If you are an international or national agency or a country representative and need our support in defining path for future population of a region or your country, please write to us with the subject line ',html.A('Region/Country Specific Population Path',href = 'mailto:info@briskcheck.com?subject=Region/Country Specific Population Path'), ' with your complete contact details, our experts will get back to you.'])
            ],style =  {'backgroundColor':'#CEFFC9','margin': 'auto','width':'80%','padding':'10px'}),
            ],id="additional"),
            html.Div([
            html.Div([
            html.H6('Contact Us:',style = {'fontWeight':'bold'}),
            html.Br(),
            html.Ul(['* For any queries or suggestions, please contact us at ',html.A('info@briskcheck.com',href = 'mailto:info@briskcheck.com'),'. You will hear back from us in less than 24 hours.']),
            html.Ul(['* If you are an international or national agency or a country representative and need our support in defining path for future population of a region or your country, please write to us with the subject line ',html.A('Region/Country Specific Population Path',href = 'mailto:info@briskcheck.com?subject=Region/Country Specific Population Path'), ' with your complete contact details, our experts will get back to you.'])
            ],style =  {'backgroundColor':'#CEFFC9','margin': 'auto','width':'80%','padding':'10px'}),
            html.Br(),
            html.Div([
            html.H6('About Authors:',style = {'fontWeight':'bold'}),
            html.P('The authors of this report are:'),
            html.Br(),
            html.P([html.Strong('Jyoti Khetarpal'),html.Span(' - The idea of this effort is initiated by Jyoti because this cause is very close to her heart since childhood.')]),
            html.P([html.Span('About Jyoti Khetarpal:',style = {'font-style':'italic'}),html.Span(' Jyoti is an India qualified Chartered Accountant with over 20 years of corporate experience with reputed organizations like Dun & Bradstreet and American Express. She has been instrumental in providing industry solutions, outlining risk mitigation & management methodology and creating better places to work. She is a speaker, writer, leader and driving force for any organization.')]),
            html.A('https://www.linkedin.com/in/jyotikhetarpal/',href = 'https://www.linkedin.com/in/jyotikhetarpal/'),
            html.Br(),
            html.Br(),
            html.P([html.Strong('Ramendra Singla'),html.Span(' - Special thanks to Ramendra, our young Data Scientist, for his efforts in analyzing the data in right perspective.')]),
            html.P([html.Span('About Ramendra Singla:',style = {'font-style':'italic'}),html.Span(' Ramendra is a final year student pursuing his B.Tech in Computer Science from IP University, Delhi. He has completed multiple internships in the field of Data Science from S&P Global Market Intelligence and finalist in Smart India Hackathon 2019, specializing in data analysis, machine learning and python development. He is an asset to any project involving data science and data analysis.')]),
            html.A('https://www.linkedin.com/in/ramendrasingla/',href = 'https://www.linkedin.com/in/ramendrasingla/')
            ],style =  {'backgroundColor':'#CEFFC9','margin': 'auto','width':'80%','padding':'10px'})],id='down'),
    ]),
])
@app.callback(
    [Output("additional", "style"),Output("down",'style')],
    [Input('add-button', 'n_clicks')])

def display(n_clicks):
    if n_clicks is None or n_clicks%2==0:
        return {'display':'None'},{}
    else:
        return {},{'display':'None'}
@app.callback(
    Output("reg-drop", "options"),
    [Input('type-drop', 'value')])

def pred(out):
    if out is not None and out!=[]:
        var = population[population['Type']==out]['Region, subregion, country or area *'].unique()
        return [{'label':ix.strip().upper() , 'value':ix.strip()} for ix in var]
    else:
        return []

@app.callback(
    Output("prediction-out", "children"),
    [Input("button", "n_clicks")],
    [State('type-drop','value'),State('reg-drop','value'),State('year-drop','value')]
)
def toggle_container(n_clicks,type,reg,yr):
    if n_clicks is None:
        output = dcc.Graph(id='population_graph',
        figure={
            'data': [],
            'layout': {
            }
            }
        )
        return output
    else:
        col_drop = [str(ix) for ix in range(1950,yr)]
        pop_out = population[population['Region, subregion, country or area *']==reg].drop(['Region, subregion, country or area *','Type']+col_drop,axis=1).values[0]
        t_5 = target_5[target_5['Region, subregion, country or area *']==reg][['Current Population']+sorted([col for col in target_5.columns if col.startswith('Target_Pop_')])].values[0]
        t_10 = target_10[target_10['Region, subregion, country or area *']==reg][['Current Population']+sorted([col for col in target_10.columns if col.startswith('Target_Pop_')])].values[0]
        t_15 = target_15[target_15['Region, subregion, country or area *']==reg][['Current Population']+sorted([col for col in target_15.columns if col.startswith('Target_Pop_')])].values[0]
        t_20 = target_20[target_20['Region, subregion, country or area *']==reg][['Current Population']+sorted([col for col in target_20.columns if col.startswith('Target_Pop_')])].values[0]
        t_25 = target_25[target_25['Region, subregion, country or area *']==reg][['Current Population']+sorted([col for col in target_25.columns if col.startswith('Target_Pop_')])].values[0]
        output = dcc.Graph(id='population_graph',
        figure={
            'data': [
                {'x': [ix for ix in range(yr,2046)], 'y': pop_out, 'type': 'line', 'name': 'Population'},
                {'x': [ix for ix in range(2020,2026)], 'y': t_5, 'type': 'line', 'name': '5 yrs Target'},
                {'x': [ix for ix in range(2020,2031)], 'y': t_10, 'type': 'line', 'name': '10 yrs Target'},
                {'x': [ix for ix in range(2020,2036)], 'y': t_15, 'type': 'line', 'name': '15 yrs Target'},
                {'x': [ix for ix in range(2020,2041)], 'y': t_20, 'type': 'line', 'name': '20 yrs Target'},
                {'x': [ix for ix in range(2020,2046)], 'y': t_25, 'type': 'line', 'name': '25 yrs Target'},
            ],
            'layout': {
                'title': 'POPULATION PLOT FOR {}'.format(reg.upper()),
                'xaxis':{
                    'title':'Year'
                },
                'yaxis':{
                    'title':'Population'
                },
            }
            }
        )
        return output

if __name__ == '__main__':
    app.run_server(debug = True)
