from flask import Flask, request,jsonify,json
from os.path import join

app = Flask(__name__)

@app.route('/')
def home():
    names = request.args.getlist('name')
    if not names:
        return jsonify({"error": "Name parameter is missing"}), 400
    #return names
    try:
        with open(join('public', 'q-vercel-python.json'),'r') as f:
            data = json.load(f)
    except Exception as e:
        print(f"Error loading JSON: {e}")
    results = "10 20"
    if results:
        results = results.strip()
        return jsonify({"marks": results}), 200
    else:
        return jsonify({"error": "Names not found"}), 404

@app.route('/about')
def about():
    return 'About'