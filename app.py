import os
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def hello():
    return jsonify({"message": "Hello, DevOps!"})

@app.route('/health')
def health():
    return jsonify({"status": "healthy"})

@app.route('/info')
def info():
    return jsonify({
        "version": os.getenv("APP_VERSION", "1.0.0"),
        "environment": os.getenv("ENVIRONMENT", "development")
    })

@app.route('/api/echo', methods=['GET'])
def echo_service():
    message = request.args.get('message')
    if message is None:
        return jsonify({"error": "message parameter is required"}), 400
    return jsonify({"echo": message, "length": len(message)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
