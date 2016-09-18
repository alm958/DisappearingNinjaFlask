from flask import Flask, render_template, redirect

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<ninja>')
def ninja(ninja):
    if ninja == 'blue':
        ninja = 'leonardo'
    elif ninja == 'orange':
        ninja = 'michelangelo'
    elif ninja == 'red':
        ninja = 'raphael'
    elif ninja == 'purple':
        ninja = 'donatello'
    else:
        ninja = 'notapril'
    return render_template('ninja.html', ninja = ninja)

if __name__ == '__main__':
    app.run(debug=True)
