import os
from flask import Flask
from PhisingDetection import getResult, getMultiResult, Mode
from print_dict import pd as printdict
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from flask import jsonify
from werkzeug.utils import secure_filename
app = Flask(__name__,template_folder="web/templates",static_folder="web/static",static_url_path="/public")

UPLOAD_FOLDER= './files'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
ALLOWED_EXTENSIONS = set(['txt', 'csv'])

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/result', methods = ['GET', 'POST'])
def result():
    if request.method == 'POST':
        print(request.files)
        if 'file' not in request.files:
            return "No file has been upload"
        file = request.files['file']
        if file.filename == '':
            flash('no select file')
            return 'false'
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            print(app.config['UPLOAD_FOLDER'])
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            type_model = int(request.form.get("type"))
            if type_model == 2:
                model = Mode.LOGISTIC_REGRESSION
            elif type_model == 3:
                model = Mode.SVM
            else:
                model = Mode.RANDOM_FOREST
            result = getMultiResult(os.path.join(app.config['UPLOAD_FOLDER'], filename),model)
            printdict(result)
            return result
    else:
        urlname  = request.args['name']
        type_model = int(request.args['type'])
        if urlname == "":
            return "Invalid URL"
        if type_model == 2:
            model = Mode.LOGISTIC_REGRESSION
        elif type_model == 3:
            model = Mode.SVM
        else:
            model = Mode.RANDOM_FOREST
        result = getResult(urlname, model)
        printdict(result)
        return result

# @app.route('/upload')
# def upload():
# 	return 'yes'

@app.route('/', methods = ['GET', 'POST'])
def single():
	return  render_template("home.html")

@app.route('/multi')
def multi():
	return  render_template("multi.html")
			


if __name__ == '__main__':
    app.run(debug=True)
