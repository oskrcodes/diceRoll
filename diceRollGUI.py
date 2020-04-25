from flask import Flask, render_template

app = Flask(__name__)

rollsHistory = [
    {
        'rollNum': 'One',
        'rollValue': 'Four'
    },
    {
        'rollNum': 'Two',
        'rollValue': 'Six'
    },
    {
        'rollNum': 'Three',
        'rollValue': 'One'
    }
]


@app.route("/")
@app.route("/home")
def hello():
    return render_template('home.html', rollsHistory=rollsHistory)


@app.route("/about")
def about():
    return render_template('about.html')