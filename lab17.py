from flask import Flask, render_template
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
bootstrap = Bootstrap5(app)

#task2
@app.route('/')
def hello():
    return 'Hello world from Flask!'

#task3
@app.route('/')
def t_Test():
    return render_template('template_1.html')

#task4
@app.route('/delight')
def acronym():
    return render_template('template_2.html')