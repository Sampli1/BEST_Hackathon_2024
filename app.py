from flask import Flask, render_template

app = Flask(__name__, template_folder="template")
app.config['TEMPLATES_AUTO_RELOAD'] = True
@app.route('/')
def hello():
    return render_template('HOME.html') 

@app.route('/OUT')
def res():
    return render_template('RESULTS.html') 