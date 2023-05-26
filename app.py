from flask import Flask, render_template

app = Flask(__name__)

@app.routes('/', methods=['GET'])
def index():
    render_template('index.html')


if __name__ == '__main__':
    app.run()
