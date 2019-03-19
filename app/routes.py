from flask import render_template
from app import app
from flask import request

@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET', 'POST'])
def index():
	if request.method == 'POST':
		return render_template('index.html', show_table = True)

	return render_template('index.html', show_table = False)	



