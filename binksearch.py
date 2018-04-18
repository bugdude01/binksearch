from flask import flask

app = Flask(__name__)


@app.route('/')
def bink_lookup():
	return 'What would you like to search for today?'


if __name__ == '__main__':
	app.run()