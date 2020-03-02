import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go #used in graph function
import requests  #to grab data from site

app = dash.Dash() #dash app

#scraping every 8 seconds
#total count is what we are concerned about
#this depend on webscraping
#line plot for total no of flights every 8 seconds

#setup app layout - Iframe displays original site
app.layout = html.Div([
    html.Div([   #another div with pre formatting block , showing text etc
    html.Pre(
        id='counter_text',
        children='Active flights worldwide:' #comes are string
    ),
    #adding graph component will be used below , updting each 6 secs
    dcc.Graph(id='live-update-graph',style={'width':1200}),
    dcc.Interval(    #how fast u wanna refresh/update
        id='interval-component',
        interval=6000, # 6000 milliseconds = 6 seconds
        n_intervals=0   #initial no of intervals
    )])
])
counter_list = []  #keep appending to this , over update_layout , append current count

#connect components with update_layout function
#update layout will be called on every update

@app.callback(Output('counter_text', 'children'),
              [Input('interval-component', 'n_intervals')])
#returning back to children the no of active flights
#taking same info and updating the fig and returning
def update_layout(n):   #url came from webscraping
    url = "https://data-live.flightradar24.com/zones/fcgi/feed.js?faa=1\
           &mlat=1&flarm=1&adsb=1&gnd=1&air=1&vehicles=1&estimated=1&stats=1"
    # A fake header is necessary to access the site:
    res = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    data = res.json()
    counter = 0
    for element in data["stats"]["total"]:
        counter += data["stats"]["total"][element]
    counter_list.append(counter)
    return 'Active flights worldwide: {}'.format(counter)


#adding graph as well for above live value count which is live
#send info to graph and update the graph
@app.callback(Output('live-update-graph','figure'),
              [Input('interval-component', 'n_intervals')])
def update_graph(n):
    fig = go.Figure(
        data = [go.Scatter(
        x = list(range(len(counter_list))), #from 0 to how many points we counted so far
        y = counter_list,  #actual count value of flights
        mode='lines+markers'
        )])
    return fig  #return fig to the figure

if __name__ == '__main__':
    app.run_server()
