from flask import Flask, request,jsonify

app = Flask(__name__)

@app.route('/')
def home():
    names = request.args.getlist('name')
    if not names:
        return jsonify({"error": "Name parameter is missing"}), 400
    #return names
    results = "10 20"
    if results:
        results = results.strip()
        return jsonify({"marks": results}), 200
    else:
        return jsonify({"error": "Names not found"}), 404

@app.route('/about')
def about():
    return 'About'