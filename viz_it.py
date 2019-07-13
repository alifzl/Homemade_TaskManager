# needful basic libraries
import datetime as dt
import os
import time
# greatest library ever, needed for IO and calculations
import pandas as pd
# Dash Visulization library
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
# Flask caching system for memorizing the input
from flask_caching import Cache
# memory profiler, for measuring the efficiency of the code
from memory_profiler import profile

# loading some beautiful CSS
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

### you can choose between the two caching system, indicated below ###

# Redis DB caching system

cache = Cache(app.server, config={
    'CACHE_TYPE': 'redis',
    'CACHE_REDIS_URL': os.environ.get('redis://', '')
})

# File System caching system (store in File)

# cache = Cache(app.server, config={
#     'CACHE_TYPE': 'filesystem',
#     'CACHE_DIR': 'cache-directory'
# })

# refresh duration new data
TIMEOUT = 60


@cache.memoize(timeout=TIMEOUT)
def query_data():
    '''
    opens the Log File, parses the columns,
    and produces the compressed json file.
    '''

    col = ['Time', 'Memory Avalable Space (MB)', 'Memory Cache Faults',
           'Eth0 Bytes (Send/Sec)', 'Wireless Bytes (Send/Sec)', 'Eth0 Bytes (Recieved/Sec)',
           'Wireless Bytes (Recieved/Sec)', 'Processor Time',
           'P0_Maximum Frequency(%)', 'P1_Maximum Frequency(%)', 'P2_Maximum Frequency(%)', 'P3_Maximum Frequency(%)']
    # This could be an expensive data querying step
    df = pd.read_csv("Log.csv")
    df.columns = col
    # now = dt.datetime.now()
    # df['time'] = [now - dt.timedelta(seconds=5*i) for i in range(100)]
    # df.to_csv("Log.csv")
    return df.to_json(date_format='iso', orient='split')


def dataframe():
    '''
    reads the Json file
    return our the data-frame
    '''

    return pd.read_json(query_data(), orient='split')


# define the structure of the User Interface
app.layout = html.Div([
    dcc.Markdown('''
#### Home Made Task Manager

Source code of this Visualization can be found [here](https://github.com/AFZL95/Homemade_TaskManager).
'''),
    html.Div('Data was updated within the last {} seconds'.format(TIMEOUT)),
    dcc.Dropdown(
        id='live-dropdown',
        value='Time',
        options=[{'label': i, 'value': i} for i in dataframe().columns]
    ),
    dcc.Graph(id='live-graph')
])

# define the pricedure of data refreshing
@app.callback(Output('live-graph', 'figure'),
              [Input('live-dropdown', 'value')])
def update_live_graph(value):
    df = dataframe()
    now = dt.datetime.now()
    return {
        'data': [{
            'x': df['Time'],
            'y': df[value],
            'line': {
                'width': 1,
                'color': '#0074D9',
                'shape': 'spline'
            }
        }],
        'layout': {
            # display the current position of now
            # this line will be between 0 and 60 seconds
            # away from the last datapoint
            'shapes': [{
                'type': 'line',
                'xref': 'x', 'x0': now, 'x1': now,
                'yref': 'paper', 'y0': 0, 'y1': 1,
                'line': {'color': 'darkgrey', 'width': 1}
            }],
            'annotations': [{
                'showarrow': False,
                'xref': 'x', 'x': now, 'xanchor': 'right',
                'yref': 'paper', 'y': 0.95, 'yanchor': 'top',
                'text': 'Current time ({}:{}:{})'.format(
                    now.hour, now.minute, now.second),
                'bgcolor': 'rgba(255, 255, 255, 0.8)'
            }],
            # aesthetic options
            'margin': {'l': 40, 'b': 40, 'r': 20, 't': 10},
            'xaxis': {'showgrid': True, 'zeroline': True},
            'yaxis': {'showgrid': True, 'zeroline': True}
        }
    }
# fake function, only for being able to use the memory profiler decorator
@profile
def start_from_here():
    app.run_server(debug=True)


if __name__ == '__main__':

    # in the case you dont need the performance evaluation
    # app.run_server(debug=True)

    start_from_here()
