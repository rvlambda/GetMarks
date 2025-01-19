import json
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def get_marks():
    names = request.args.getlist('name')
    
    with open('public/q-vercel-python.json', 'r') as file:
        data = json.load(file)
    
    marks = {name: data.get(name, 0) for name in names}
    
    return jsonify({"Marks": marks})

if __name__ == '__main__':
    app.run(debug=True)