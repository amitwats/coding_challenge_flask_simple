from flask import Flask, request, jsonify
import math

app = Flask(__name__)

def compute_sqrt_of_sum_of_squares(numbers):
    highest_three = sorted(numbers, reverse=True)[:3]
    squares = list(map(lambda x: x ** 2, highest_three))
    result = math.sqrt(sum(squares))
    return result

@app.route('/compute', methods=['POST'])
def compute():
    try:
        data = request.json.get('data', [])
        
        # Validating
        if not isinstance(data, list) or not all(isinstance(i, (int, float)) for i in data):
            return jsonify({"error": "Input should be a list of numbers"}), 400
        
        if len(data) < 3:
            return jsonify({"error": "At least 3 numbers are required"}), 400
        
        result = compute_sqrt_of_sum_of_squares(data)
        return jsonify({"output": round(result, 2)}), 200
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/', methods=['GET'])
def index():
    return 'Main Page. To test application use a POST request, with json data like {"data": [5, 4, 6, 1]})'


if __name__ == '__main__':
    app.run(debug=True)
