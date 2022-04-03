
# import importlib
from distutils.log import debug
from black import main
from flask import Flask, redirect, url_for, render_template, jsonify, json
from gevent.pywsgi import WSGIServer

from EquityBulls import limited
#from iifl import limitedIifl
from third import headings_links

app = Flask(__name__) #define app

@app.route('/') #path set
def home():
    return render_template('index.html')

@app.route('/equitybulls') #path set
def EQ():
    return render_template('newsEquity.html',limited=limited)

# @app.route('/iifl') #path set
# def iifl():
#     return render_template('newsIifl.html',limitedIifl=limitedIifl)

@app.route('/livemint') #path set
def livemint():
    return render_template('livemint.html',limited=headings_links)


@app.route('/predict') #path set
def predict():
    # scaler=MinMaxScaler(feature_range=(0,1))
    # nifty_quote = web.DataReader('^NSEI',data_source='yahoo',start='2016-01-01',end=today)
    # #create a new dataframe
    # new_df = nifty_quote.filter(['Close'])
    # #get the last 60 day closing price values and convert the dataframe to an array 
    # last_60_days = new_df[-60:].values
    # #scale the data to be values between 0 and 1
    # last_60_days_scaled = scaler.transform(last_60_days)
    # #create an empty list
    # X_test = []
    # #APPEND THE LAST 60 DAYS
    # X_test.append(last_60_days_scaled)
    # #convert the X_test data set to np array
    # X_test = np.array(X_test)
    # #Reshape
    # X_test = np.reshape(X_test,(X_test.shape[0],X_test.shape[1],1))
    # #get predicted scaled price
    # pred_price = model.predict(X_test)
    # pred_price = scaler.inverse_transform(pred_price)
    # print(pred_price)
    # #nifty_quote
    return render_template('predict.html')

@app.route('/sentiment') #path set
def sentiment():
    return render_template('sentiment.html')

app.run(debug=True)

# @app.route("/<name>")
# def user(name):
#     return f"Hello {name}"


# @app.route("/admin/")
# def admin():
#     return redirect(url_for("user", name="Admin"))


if __name__ == "__main__":
    app.run(debug=True)
    http_server = WSGIServer(('', 5000), app)
    http_server.serve_forever()