from flask import Flask, request, jsonify
import requests
import json

app = Flask(__name__)

# Define a simple endpoint for a GET request
@app.route('/', methods=['GET'])
def home():
    return 'Hello, this is a simple Flask app!'

# Define an endpoint for a POST request
@app.route('/api', methods=['POST'])
def api_endpoint():
    try:
        # Get the JSON data from the request
        json_data = request.get_json()

        if json_data:
            # Process the JSON data (echo it in this case)
            result = {"result": "Received json data", "data": json_data}
            return jsonify(result), 200
        else:
            return jsonify({"error": "JSON body is empty"}), 400

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    


if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True, host='0.0.0.0', port=5000)
