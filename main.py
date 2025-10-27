from flask import Flask, render_template, jsonify, request
import os
from datetime import datetime
import json

app = Flask(__name__)

# حالة البوت الافتراضية
bot_status = {
    "status": "running",
    "balance": 1000.00,
    "profit_loss": +25.50,
    "active_trades": 2,
    "last_update": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
}

@app.route('/')
def home():
    return '''
    <html>
    <head>
        <title>البوت التجاري السحابي</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>
            body { 
                font-family: Arial, sans-serif; 
                text-align: center; 
                padding: 50px; 
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: white;
            }
            .container {
                background: rgba(255,255,255,0.1);
                padding: 30px;
                border-radius: 15px;
                backdrop-filter: blur(10px);
                max-width: 500px;
                margin: 0 auto;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🚀 البوت التجاري السحابي</h1>
            <p>النظام يعمل بنجاح على Railway!</p>
            <p>الحالة: <strong>جاري التشغيل</strong></p>
            <p>الرصيد: <strong>1,000.00$</strong></p>
            <p>الأرباح: <strong style="color: #4CAF50;">+25.50$</strong></p>
        </div>
    </body>
    </html>
    '''

@app.route('/api/status')
def get_status():
    return jsonify(bot_status)

@app.route('/api/trades')
def get_trades():
    trades = [
        {"id": 1, "pair": "BTC/USDT", "type": "buy", "amount": 0.01, "price": 45000, "time": "10:30:15"},
        {"id": 2, "pair": "ETH/USDT", "type": "sell", "amount": 0.1, "price": 2500, "time": "10:25:30"}
    ]
    return jsonify(trades)

@app.route('/api/control', methods=['POST'])
def control_bot():
    action = request.json.get('action')
    if action == 'start':
        bot_status['status'] = 'running'
    elif action == 'stop':
        bot_status['status'] = 'stopped'
    
    return jsonify({"message": f"Bot {action}ped", "status": bot_status['status']})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
