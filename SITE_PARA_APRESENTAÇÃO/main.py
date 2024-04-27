from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/conceito')
def conceito():
    return render_template('conceito.html')

@app.route('/historia')
def historia():
    return render_template('historia.html')

@app.route('/biblia')
def biblia():
    return render_template('biblia.html')


if __name__ == '__main__':
    app.run(debug=True)
