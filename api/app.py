from flask import Flask, request,jsonify

app = Flask(__name__)

@app.route('/')
def home():
    names = request.args.getlist('name')
    if not names:
        return jsonify({"error": "Name parameter is missing"}), 400
    return names

@app.route('/about')
def about():
    return 'About'