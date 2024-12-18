from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data.get('message', '')
    response_message = "You said: " + user_message
    return jsonify({"message": response_message})

if __name__ == '__main__':
    app.run(port=5000)
