from flask import Flask, request, render_template

# Initialize Flask app.
app = Flask(__name__)

# Root endpoint
@app.route('/', methods=['GET'])
def home():
    return 'Root URL'

# Hello endpoint
@app.route('/hello', methods=['GET'])
def hello():
    return 'Hello World'

# Sum endpoint
@app.route('/product', methods=['POST'])
def product():
    a = int(request.form['first'])
    b = int(request.form['second'])
    product = str(a*b)
    return 'Product of {} and {} is {}'.format(a, b, product)

# Message endpoint
@app.route('/message', methods=['POST'])
def message():
    message = request.form['message']
    print(message)
    return 'Message Sent!'

# Hello endpoint
@app.route('/pokemon', methods=['GET'])
def pokemon():
    return render_template('index.html', name="Pikachu")
		
if __name__ == '__main__':
   app.run()