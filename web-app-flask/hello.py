from flask import Flask, render_template

app = Flask(__name__)

actions = [
    {
        'Tribe': 'OCF',
        'Squad': 'CIT',
        'Application': 'CASV',
        'OS': 'Linux',
    },
    {
        'Tribe': 'OCF',
        'Squad': 'CIT',
        'Application': 'CASV',
        'OS': 'Linux',
    },

]


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', actions=actions)


@app.route('/about')
def about():
    return render_template('about.html', title='About')


if __name__ == '__main__':
    app.run(debug=True)
