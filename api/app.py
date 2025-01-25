from flask import Flask, request,jsonify,json
from os.path import join
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api')
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
 
    results = []
    for name in names:
        result = next((item for item in data if item['name'] == name), None)
        if result:
            results.append(result['marks'])
            #results += str(result['marks']) + " "
    
    
    if results:
        #results = results.strip()
        return jsonify({"marks": results}), 200
    else:
        return jsonify({"error": "Names not found"}), 404

@app.route('/about')
def about():
    return 'About'