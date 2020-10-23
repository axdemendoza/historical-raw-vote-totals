import numpy as np
import pandas as pd
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import dash
import dash_core_components as dcc
import dash_html_components as html

df = pd.read_csv('all_data.csv', index_col=0)

dem = df[df['Party']=='Democratic']
rep = df[df['Party']=='Republican']

flo_rep = rep[rep['State']=='Florida']
flo_dem = dem[dem['State']=='Florida']

wis_rep = rep[rep['State']=='Wisconsin']
wis_dem = dem[dem['State']=='Wisconsin']

mich_rep = rep[rep['State']=='Michigan']
mich_dem = dem[dem['State']=='Michigan']

pa_rep = rep[rep['State']=='Pennsylvania']
pa_dem = dem[dem['State']=='Pennsylvania']

nc_rep = rep[rep['State']=='North Carolina']
nc_dem = dem[dem['State']=='North Carolina']

tx_rep = rep[rep['State']=='Texas']
tx_dem = dem[dem['State']=='Texas']

az_rep = rep[rep['State']=='Arizona']
az_dem = dem[dem['State']=='Arizona']

ga_rep = rep[rep['State']=='Georgia']
ga_dem = dem[dem['State']=='Georgia']

oh_rep = rep[rep['State']=='Ohio']
oh_dem = dem[dem['State']=='Ohio']

tick_array = [2000, 2004, 2008, 2012, 2016, 2020]

fig = make_subplots(
    rows=3, cols=3,
    subplot_titles=("Wisconsin", "Michigan", "Pennsylvania",
                    "Florida", "Ohio", "North Carolina", 
                    "Arizona", "Georgia", "Texas")
)


fig.add_trace(go.Scatter(x=wis_dem['Year'], y=wis_dem['Votes'],
                    customdata=wis_dem['Candidate'],
                    mode='lines+markers',
                    line={'color': 'blue'},
                    name='Democratic Votes',
                    legendgroup='Democratic'),
                    row=1, col=1)
fig.add_trace(go.Scatter(x=wis_rep['Year'], y=wis_rep['Votes'],
                    customdata=wis_rep['Candidate'],
                    mode='lines+markers',
                    line={'color': 'red'},
                    name='Republican Votes',
                    legendgroup='Republican'),
                    row=1, col=1)

fig.add_trace(go.Scatter(x=mich_dem['Year'], y=mich_dem['Votes'],
                    customdata=mich_dem['Candidate'],
                    mode='lines+markers',
                    line={'color': 'blue'},
                    name='Democratic Votes',
                    legendgroup='Democratic',
                    showlegend=False),
                    row=1, col=2)
fig.add_trace(go.Scatter(x=mich_rep['Year'], y=mich_rep['Votes'],
                    customdata=mich_rep['Candidate'],
                    mode='lines+markers',
                    line={'color': 'red'},
                    name='Republican Votes',
                    legendgroup='Republican',
                    showlegend=False),
                    row=1, col=2)

fig.add_trace(go.Scatter(x=pa_dem['Year'], y=pa_dem['Votes'],
                    customdata=pa_dem['Candidate'],
                    mode='lines+markers',
                    line={'color': 'blue'},
                    name='Democratic Votes',
                    legendgroup='Democratic',
                    showlegend=False),
                    row=1, col=3)
fig.add_trace(go.Scatter(x=pa_rep['Year'], y=pa_rep['Votes'],
                    customdata=pa_rep['Candidate'],
                    mode='lines+markers',
                    line={'color': 'red'},
                    name='Republican Votes',
                    legendgroup='Republican',
                    showlegend=False),
                    row=1, col=3)
    
fig.add_trace(go.Scatter(x=flo_dem['Year'], y=flo_dem['Votes'],
                    customdata=flo_dem['Candidate'],
                    mode='lines+markers',
                    line={'color': 'blue'},
                    name='Democratic Votes',
                    legendgroup='Democratic',
                    showlegend=False),
                    row=2, col=1)
fig.add_trace(go.Scatter(x=flo_rep['Year'], y=flo_rep['Votes'],
                    customdata=flo_rep['Candidate'],
                    mode='lines+markers',
                    line={'color': 'red'},
                    name='Republican Votes',
                    legendgroup='Republican',
                    showlegend=False),
                    row=2, col=1)

fig.add_trace(go.Scatter(x=oh_dem['Year'], y=oh_dem['Votes'],
                    customdata=oh_dem['Candidate'],
                    mode='lines+markers',
                    line={'color': 'blue'},
                    name='Democratic Votes',
                    legendgroup='Democratic',
                    showlegend=False),
                    row=2, col=2)
fig.add_trace(go.Scatter(x=oh_rep['Year'], y=oh_rep['Votes'],
                    customdata=oh_rep['Candidate'],
                    mode='lines+markers',
                    line={'color': 'red'},
                    name='Republican Votes',
                    legendgroup='Republican',
                    showlegend=False),
                    row=2, col=2)

fig.add_trace(go.Scatter(x=nc_dem['Year'], y=nc_dem['Votes'],
                    customdata=nc_dem['Candidate'],
                    mode='lines+markers',
                    line={'color': 'blue'},
                    name='Democratic Votes',
                    legendgroup='Democratic',
                    showlegend=False),
                    row=2, col=3)
fig.add_trace(go.Scatter(x=nc_rep['Year'], y=nc_rep['Votes'],
                    customdata=nc_rep['Candidate'],
                    mode='lines+markers',
                    line={'color': 'red'},
                    name='Republican Votes',
                    legendgroup='Republican',
                    showlegend=False),
                    row=2, col=3)

fig.add_trace(go.Scatter(x=az_dem['Year'], y=az_dem['Votes'],
                    customdata=az_dem['Candidate'],
                    mode='lines+markers',
                    line={'color': 'blue'},
                    name='Democratic Votes',
                    legendgroup='Democratic',
                    showlegend=False),
                    row=3, col=1)
fig.add_trace(go.Scatter(x=az_rep['Year'], y=az_rep['Votes'],
                    customdata=az_rep['Candidate'],
                    mode='lines+markers',
                    line={'color': 'red'},
                    name='Republican Votes',
                    legendgroup='Republican',
                    showlegend=False),
                    row=3, col=1)
    
fig.add_trace(go.Scatter(x=ga_dem['Year'], y=ga_dem['Votes'],
                    customdata=ga_dem['Candidate'],
                    mode='lines+markers',
                    line={'color': 'blue'},
                    name='Democratic Votes',
                    legendgroup='Democratic',
                    showlegend=False),
                    row=3, col=2)
fig.add_trace(go.Scatter(x=ga_rep['Year'], y=ga_rep['Votes'],
                    customdata=ga_rep['Candidate'],
                    mode='lines+markers',
                    line={'color': 'red'},
                    name='Republican Votes',
                    legendgroup='Republican',
                    showlegend=False),
                    row=3, col=2)

fig.add_trace(go.Scatter(x=tx_dem['Year'], y=tx_dem['Votes'],
                    customdata=tx_dem['Candidate'],
                    mode='lines+markers',
                    line={'color': 'blue'},
                    name='Democratic Votes',
                    legendgroup='Democratic',
                    showlegend=False),
                    row=3, col=3)
fig.add_trace(go.Scatter(x=tx_rep['Year'], y=tx_rep['Votes'],
                    customdata=tx_rep['Candidate'],
                    mode='lines+markers',
                    line={'color': 'red'},
                    name='Republican Votes',
                    legendgroup='Republican',
                    showlegend=False),
                    row=3, col=3)

fig.update_xaxes(type='category')

fig.update_layout(height=800)

fig.update_traces(
    hovertemplate=
    'Year: %{x}<br>'+
    'Number of Votes</b>: %{y:,}<br>'+
    'Candidate</b>: %{customdata}'
)



external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

server = app.server

app.layout = html.Div([
    dcc.Graph(figure=fig)
])

if __name__ == '__main__':
    app.run_server(debug=True)