from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField, TextAreaField
from werkzeug.utils import secure_filename
import os
from wtforms.validators import InputRequired
import csv 
import pandas as pd
import parse

app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey'
app.config['UPLOAD_FOLDER'] = 'static/files'

player_dataframe = ""

class UploadFileForm(FlaskForm):
    file = FileField("File", validators=[InputRequired()])
    submit = SubmitField("Upload File")
    address = TextAreaField('Mailing Address')
    address.label = ("Email Address")

@app.route('/')

def home():
    return render_template('index.html')

@app.route('/insert', methods=['GET',"POST"])

def insert():
    form = UploadFileForm()
    return render_template('insert.html', form=form)

@app.route('/upload', methods=['GET',"POST"])

def upload():
    form = UploadFileForm()
    if form.validate_on_submit():
        file = form.file.data
        if file.filename[-4:] != ".csv":
            return "Your input file was not a csv"
        file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)),secure_filename(file.filename)))
        return init_parse(file.filename)
    return render_template('upload.html', form=form)

def init_parse(filename):
    player_dataframe = parse.parse(filename)
    html = player_dataframe.to_html()
    return(html)
    
if __name__ == '__main__':
    app.run(debug=True)