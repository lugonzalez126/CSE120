import pandas as pd
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import json

df = pd.read_csv('dataLog_Doogie_220815_175620.csv')
df['DateAndTime'] = pd.to_datetime(df['DateAndTime  (string)'])

app = dash.Dash(__name__)

fig = make_subplots(specs=[[{"secondary_y": True}]])

fig.add_trace(go.Scatter(x=['2023-01-01 10:00:00'], y=[0], name='State of Charge'), secondary_y=False)
fig.add_trace(go.Scatter(x=['2023-01-01 10:00:00'], y=[0], name='Battery Voltage'), secondary_y=True)

app.layout = html.Div([
    dcc.Graph(id='charging-graph', figure=fig),
    html.Div(id='selected-data')
])

@app.callback(
    Output('charging-graph', 'figure'),
    Input('charging-graph', 'relayoutData')
)
def update_graph(_):
    
    filtered_data = df[['DateAndTime  (string)', 'BatteryStateOfCharge  (instantaneous, percent)', 'BatteryVoltage  (instantaneous, volts)']]
   
    filtered_data.columns = ['DateAndTime', 'BatteryStateOfCharge', 'BatteryVoltage']
    
    fig = make_subplots(specs=[[{"secondary_y": True}]])
    
    fig.add_trace(go.Scatter(x=filtered_data['DateAndTime'], y=filtered_data['BatteryStateOfCharge'], name='State of Charge'), secondary_y=False)
    
    fig.add_trace(go.Scatter(x=filtered_data['DateAndTime'], y=filtered_data['BatteryVoltage'], name='Battery Voltage'), secondary_y=True)
    
   
    fig.update_xaxes(title_text='Time')
    fig.update_yaxes(title_text='State of Charge', secondary_y=False)
    fig.update_yaxes(title_text='Battery Voltage', secondary_y=True)
    

    fig.update_layout(title_text='State of Charge and Battery Voltage Over Time')
    fig.update_layout(height=800, width=1800)

    return fig

@app.callback(
    Output('selected-data', 'children'),
    Input('charging-graph', 'clickData')
)
def display_selected_data(clickData):
    if clickData:
      
        selected_date_time = clickData['points'][0]['x']
        
        selected_data = df[df['DateAndTime'] == selected_date_time]
        
        formatted_data = json.dumps(selected_data.to_dict('records'), indent=2)
        
        return f"Selected Data:\n{formatted_data}"

if __name__ == '__main__':
    app.run_server(debug=True)
