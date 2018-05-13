from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def greeting():
    return render_template('index.html', name = 'World')
@app.route('/ninjas')
def info_ninja():
    return render_template('ninjas.html', name='Ninja Thao')
@app.route('/dojos/new', methods=['POST'])
def dojos():
    name = request.form['name']
    email = request.form['email']
    return redirect('/')
app.run(debug=True)