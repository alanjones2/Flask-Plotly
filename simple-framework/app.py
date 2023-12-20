from flask import Flask, render_template, request
import pandas as pd
#import json
#import plotly
import plotly.express as px

app = Flask(__name__)

@app.route('/callback', methods=['POST', 'GET'])
def cb():
    return gm(request.args.get('data'))
   
@app.route('/')
def index():
    return render_template('chartsajax.html')#,  graphJSON=gm())

def gm(country='United Kingdom'):
    df = pd.DataFrame(px.data.gapminder())

    fig = px.line(df[df['country']==country], x="year", y="gdpPercap", title=country)

    graphJSON = fig.to_json() #json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON

