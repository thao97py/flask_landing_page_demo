from flask import Flask, render_template, request, redirect
app = Flask(__name__)
@app.route('/')
def greeting():
    return render_template('index.html', name = 'World')

@app.route('/dojos/new')
def dojos():
    print "Got Post info"
    return render_template('dojos.html')

@app.route('/new/users', methods=['POST'])
def create_user():
    name = request.form('name')
    email = request.form('email')
    return redirect('/new')

@app.route('/ninjas')
def info_ninja():
    return render_template('ninjas.html', name='Ninja Thao')
app.run(debug=True)