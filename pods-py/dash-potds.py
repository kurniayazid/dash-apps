# Dasboarding_project: POTDS2020

#load dash libraries
import dash
import dash_auth
import dash_core_components as dcc
import dash_html_components as html

VALID_USERNAME_PASSWORD_PAIRS = {
    'admin': '1234'
    #'potds2020': 'vote4usa100%'
}

app = dash.Dash()
auth = dash_auth.BasicAuth(
    app,
    VALID_USERNAME_PASSWORD_PAIRS
)

#Boostrap CSS.
# app.css.append_css({
#     "external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"
# })

app.title = 'The President of Digital States 2020' # Application title

# Body Layout
app.layout = html.Div([
	 html.Div(
            [
                html.H1(children='The President of Digital States 2020 Dashboard',
                		style={'font-family':'Playfair Display'},
                        className='nine columns'),               
                html.Img(
                    src="https://cdn-images-1.medium.com/max/184/1*5LfyTwH-HeOFbX6mFfo8fg@2x.png",
                    className='three columns',
                    style={
                        'height': '8%',
                        'width': '8%',
                        'float': 'right',
                        'position': 'relative',
                        'margin_top': '10'
                        },
                ),
                html.Div(children='''
                        Developed by @kurniayazid
                        ''',
                        className='nine columns',
                        style={'margin-left': '0',
                        'font-family': 'Calibri'}
                )
            ], className="row"
        ), 
])

if __name__ == '__main__':
	app.run_server(debug=True)
