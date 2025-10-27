from flask import Flask, render_template, jsonify, request
import os
from datetime import datetime

app = Flask(__name__)

# حالة البوت
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
                body { font-family: Arial; text-align: center; padding: 20px; background: #f0f0f0; }
                .card { background: white; padding: 20px; margin: 10px; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }
                .profit { color: green; }
            </style>
        </head>
        <body>
            <h1>🤖 البوت التجاري السحابي</h1>
            <div class="card">
                <h3>الحالة: ✅ يعمل</h3>
                <p>الرصيد: <strong>1,025.50$</strong></p>
                <p class="profit">الأرباح: +25.50$</p>
                <p>الصفقات النشطة: 2</p>
            </div>
            <p>تم النشر بنجاح على Vercel! 🚀</p>
        </body>
    </html>
    '''

@app.route('/api/status')
def status():
    return jsonify(bot_status)

if __name__ == '__main__':
    app.run(debug=True)
