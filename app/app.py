from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.form['user_input']
    response = generate_response(user_input)
    return render_template('index.html', user_input=user_input, bot_response=response)

def generate_response(input_text):
    # Simple echo response
    return "You said: " + input_text

if __name__ == '__main__':
    app.run(debug=True)
