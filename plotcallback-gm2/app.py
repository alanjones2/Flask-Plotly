from flask import Flask, render_template, request
import pandas as pd
import json
import plotly
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

    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON

"""
                tweetData.plot.bar(subplots=True, figsize=(10,6),y=['favorite_count','retweet_count'], label=['Likes','Retweets'],title=(rvals['name'],''))

            from io import BytesIO
            fig = BytesIO()
            plt.savefig(fig, format='png')
            fig.seek(0)  # rewind to beginning of file
            import base64
            #figdata_png = base64.b64encode(figfile.read())
            rvals['fig'] = base64.b64encode(fig.getvalue())

            return render_template('tsindex.html', result=fig.decode('utf8'))

"""