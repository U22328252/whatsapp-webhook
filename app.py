from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def verify():
    return "Webhook alive ✅"

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    print("📩 Mensaje recibido:")
    print(data)
    return "ok", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
