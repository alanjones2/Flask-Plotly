from flask import Flask, render_template, request
import pandas as pd
import json
import plotly
import plotly.express as px
import yfinance as yf

app = Flask(__name__)


# Define the root route
@app.route('/')
def index():

    return render_template('index.html')

@app.route('/callback/<endpoint>')
def cb(endpoint):   
    if endpoint == "getStock":
        return gm(request.args.get('data'))
    elif endpoint == "getInfo":
        stock = request.args.get('data')
        st = yf.Ticker(stock)
        #print(st,st.info)
        return json.dumps(st.info)
    else:
        return "Bad endpoint", 400

# Return the JSON data for the Plotly graph
def gm(stock):
    st = yf.Ticker(stock)
  
    # Create a line graph
    df = st.history(period=("1d"), interval="1m")
    df=df.reset_index()

    max = (df['Open'].max())
    min = (df['Open'].min())
    range = max - min
    margin = range * 0.05
    max = max + margin
    min = min - margin
    fig = px.area(df, x='Datetime', y="Open",
        hover_data=("Open","Close","Volume"), 
        range_y=(min,max), template="seaborn" )


    # Create a JSON representation of the graph
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON