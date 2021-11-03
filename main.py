# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from datetime import date

from flask import Flask, render_template
import GetCurrency
# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__)


# The route() function of the Flask class is a decorator,
# which tells the application which URL should call
# the associated function.
@app.route('/')
def Home():
    return render_template('index.html',DATA = date.today() ,USD_SALE = GetCurrency.GetCurrencyTodayRatesAsk("USD"), CHF_SALE = GetCurrency.GetCurrencyTodayRatesAsk("CHF"), EURO_SALE = GetCurrency.GetCurrencyTodayRatesAsk("EUR"), USD_BUY = GetCurrency.GetCurrencyTodayRatesBid('USD'), EURO_BUY =GetCurrency.GetCurrencyTodayRatesBid('EUR'), CHF_BUY=GetCurrency.GetCurrencyTodayRatesBid('CHF'))

@app.route('/gold')
def Gold():
    return render_template('gold.html', content="Hello World!")

@app.route('/silver')
def Silver():
    return render_template('silver.html', content="Hello World!")
@app.route('/currency')
def Currency():
    return render_template('currency.html', content="Hello World!")

# main driver function
if __name__ == '__main__':
    app.debug = True
    app.run()
    app = Flask(__name__, template_folder='templates',static_folder='static')
