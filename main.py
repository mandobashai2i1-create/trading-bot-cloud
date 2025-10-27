from flask import Flask, render_template, jsonify, request
import requests
import json
from datetime import datetime
import os

app = Flask(__name__)

# حالة البوت الحقيقية
bot_status = {
    "status": "stopped",  # متوقف في البداية
    "balance": 1000.00,
    "profit_loss": 0.00,
    "active_trades": 0,
    "total_trades": 0,
    "last_update": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
}

# الحصول على أسعار حية من بينانس
def get_live_prices():
    try:
        response = requests.get('https://api.binance.com/api/v3/ticker/price', timeout=5)
        if response.status_code == 200:
            prices = response.json()
            # تصفية العملات الرئيسية فقط
            major_pairs = [p for p in prices if p['symbol'] in ['BTCUSDT', 'ETHUSDT', 'ADAUSDT', 'DOTUSDT', 'LINKUSDT']]
            return major_pairs
        return []
    except:
        return []

@app.route('/')
def dashboard():
    return render_template('dashboard.html')

@app.route('/api/status')
def get_status():
    # تحديث الأسعار الحية
    live_prices = get_live_prices()
    
    status_data = {
        **bot_status,
        "live_prices": live_prices,
        "server_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    return jsonify(status_data)

@app.route('/api/control', methods=['POST'])
def control_bot():
    action = request.json.get('action')
    
    if action == 'start':
        bot_status['status'] = 'running'
        bot_status['last_update'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        message = "✅ البوت يعمل الآن ويتحليل السوق"
        
    elif action == 'stop':
        bot_status['status'] = 'stopped' 
        bot_status['last_update'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        message = "⏹️ البوت متوقف"
        
    elif action == 'reset':
        bot_status.update({
            "balance": 1000.00,
            "profit_loss": 0.00,
            "active_trades": 0,
            "total_trades": 0,
            "last_update": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
        message = "🔄 تم إعادة التعيين"
    
    return jsonify({
        "message": message,
        "status": bot_status['status'],
        "balance": bot_status['balance']
    })

@app.route('/api/trades')
def get_trades():
    # صفقات افتراضية للعرض
    trades = [
        {
            "id": 1, 
            "symbol": "BTCUSDT", 
            "type": "buy", 
            "amount": 0.002, 
            "price": 43250, 
            "time": "10:30:15",
            "profit": +25.50
        },
        {
            "id": 2, 
            "symbol": "ETHUSDT", 
            "type": "sell", 
            "amount": 0.1, 
            "price": 2580, 
            "time": "10:25:30", 
            "profit": +12.30
        }
    ]
    return jsonify(trades)

@app.route('/api/market/data')
def market_data():
    # بيانات السوق الحية
    prices = get_live_prices()
    return jsonify({
        "prices": prices,
        "timestamp": datetime.now().isoformat()
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
