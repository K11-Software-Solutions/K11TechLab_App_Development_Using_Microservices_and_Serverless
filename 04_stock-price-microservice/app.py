from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

# Example using Yahoo Finance API via rapidapi.com (free tier)
RAPIDAPI_KEY = os.getenv('RAPIDAPI_KEY', 'YOUR_RAPIDAPI_KEY')
RAPIDAPI_HOST = 'yh-finance.p.rapidapi.com'

@app.route('/price')
def get_stock_price():
    symbol = request.args.get('symbol')
    if not symbol:
        return jsonify({'error': 'Symbol parameter is required'}), 400
    url = f'https://yh-finance.p.rapidapi.com/stock/v2/get-summary'
    headers = {
        'X-RapidAPI-Key': RAPIDAPI_KEY,
        'X-RapidAPI-Host': RAPIDAPI_HOST
    }
    params = {'symbol': symbol}
    response = requests.get(url, headers=headers, params=params)
    if response.status_code != 200:
        return jsonify({'error': 'Failed to fetch data'}), 500
    data = response.json()
    price = data.get('price', {}).get('regularMarketPrice', {}).get('raw')
    if price is None:
        return jsonify({'error': 'Price not found'}), 404
    return jsonify({'symbol': symbol, 'price': price})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
