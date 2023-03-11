from flask import Flask
app = Flask(__name__)
@app.route('/', methods=['GET'])
def home():
    return 'HEllO FLASK'
app.run(port=3333)