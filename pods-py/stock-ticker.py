import dash
import dash_core_components as dcc
import dash_html_components as html
from pandas_datareader import data as wb
import datetime
from dateutil.relativedelta import relativedelta
import plotly.graph_objs as go

start = datetime.datetime.today() - relativedelta(years=5)
end = datetime.datetime.today()

df = wb.DataReader('BBRI.JK',data_source='yahoo',start=start,
						end=end)

trace_close = go.Scatter(x=list(df.index),
						 y=df['Close'],
						 name='Close',
						 line=dict(color='red'))

data= [trace_close]

layout = dict(title='Stock Chart',
			  showlegend=False)

fig = dict(data=data,layout=layout)

app = dash.Dash()

app.layout = html.Div([
	html.Div(html.H1(children="Stock-Close",className='nine columns')),
	html.Div(
		dcc.Graph(id='Stock Chart',
		figure=fig)),
	html.Div(
		dcc.Graph(id='Stock boom',
		figure=fig)
	)
])

if __name__ == '__main__':
	app.run_server(debug=True)


#print(df.head())
