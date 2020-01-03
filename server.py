import base64
import os
import datetime
import json
import time
from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify
import http.client
import urllib

app = Flask(__name__)


# Fill in your Citi API keys - https://sandbox.developerhub.citi.com/application
CITI_CLIENT_ID = os.getenv('CITI_CLIENT_ID')
CITI_SECRET = os.getenv('CITI_SECRET')
CITI_PUBLIC_KEY = os.getenv('CITI_PUBLIC_KEY')

#  Citi test accounts are as follows for authentication
#        Username:        Password:
#        SandboxUser1    P@ssUser1$
#        SandboxUser2    P@ssUser2$
#        SandboxUser3    P@ssUser3$
#        SandboxUser4    P@ssUser4$

# Use 'sandbox' to test with Citi's Sandbox environment (username: user_good,
# password: pass_good)
# Use `development` to test with live users and credentials and `production`
# to go live
# CITI_ENV = os.getenv('CITI_ENV', 'sandbox')
# CITI_PRODUCTS is a comma-separated list of products to use when initializing
# Link. Note that this list must contain 'assets' in order for the app to be
# able to create and retrieve asset reports.
# CITI_PRODUCTS = os.getenv('CITI_PRODUCTS', 'transactions')

# CITI_COUNTRY_CODES is a comma-separated list of countries for which users
# will be able to select institutions from.
# CITI_COUNTRY_CODES = os.getenv('CITI_COUNTRY_CODES', 'US,CA,GB,FR,ES')

# client = citi.Client(client_id = CITI_CLIENT_ID, secret=CITI_SECRET,
#                       public_key=CITI_PUBLIC_KEY, environment=CITI_ENV, api_version='2019-05-29')

@app.route('/')
def index():
  return render_template(
    'index.ejs',
    citi_public_key=CITI_PUBLIC_KEY,
    citi_environment=CITI_ENV,
    citi_products=CITI_PRODUCTS,
    citi_country_codes=CITI_COUNTRY_CODES,
  )

access_token = None

# Exchange token flow - exchange a Link public_token for
# an API access_token
# https://sandbox.developerhub.citi.com/api/united-states/authorize/documentation#authCodeoauth2authorize_get
@app.route('/get_access_token', methods=['POST'])
def get_access_token():
  queryParam = dict();
  queryParam["response_type"] = "code";
  # Replace with environment variable
  queryParam["client_id"] = "code";
  # Scope can either be 
  # 1. pay_with_points
  # 2. accounts_details_transactions
  queryParam["scope"] = "accounts_details_transactions";
  queryParam["countryCode"] = "US";
  queryParam["businessCode"] = "GCB";
  queryParam["locale"] = "en_US";
  queryParam["state"] = "12093";
  queryParam["redirect_uri"] = "code";
  
  print(urllib.parse.urlencode(queryParam));

  # conn = http.client.HTTPSConnection("sandbox.apihub.citi.com")

  headers = { 'accept': "application/json" }

#  conn.request("GET", "/gcb/api/authCode/oauth2/authorize" ?response_type=REPLACE_THIS_VALUE&client_id=REPLACE_THIS_VALUE&scope=REPLACE_THIS_VALUE&countryCode=REPLACE_THIS_VALUE&businessCode=REPLACE_THIS_VALUE&locale=REPLACE_THIS_VALUE&state=REPLACE_THIS_VALUE&redirect_uri=REPLACE_THIS_VALUE", headers=headers)

#  res = conn.getresponse()
#  data = res.read()

 # print(data.decode("utf-8"))
    
 # global access_token
 # public_token = request.form['public_token']
 # try:
 #   exchange_response = client.Item.public_token.exchange(public_token)
 
 # except citi.errors.CitiError as e:
  #  return jsonify(format_error(e))

 # pretty_print_response(exchange_response)
 # access_token = exchange_response['access_token']
 # return jsonify(exchange_response)

#app.route('/set_access_token', methods=['POST'])
#def set_access_token():
#  global access_token
#  access_token = request.form['access_token']
#  item = client.Item.get(access_token)
#  return jsonify({'error': None, 'item_id': item['item']['item_id']})
  return

def pretty_print_response(response):
  print(json.dumps(response, indent=2, sort_keys=True))

def format_error(e):
  return {'error': {'display_message': e.display_message, 'error_code': e.code, 'error_type': e.type, 'error_message': e.message } }

if __name__ == '__main__':
    app.run(port=os.getenv('PORT', 5000))
