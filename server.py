from flask import (
    Flask, 
    render_template, 
    request, 
    redirect,
    url_for,
)
app = Flask(__name__)
@app.route('/')
def greeting():
    return render_template('index.html', name = 'World')

@app.route('/dojos/new',methods=['GET','POST'])
def dojos():
    if request.method == 'GET':
        '''
        if it's GET request => render template
        '''
        return render_template('dojos.html')
    elif request.method == 'POST':
        '''
        else if it's POST request then extract data from form
        '''
        name = request.form["name"]
        email = request.form["email"]
        context ={
            'name': name,
            'email': email,
        }
        return render_template('index.html', **context)

@app.route('/ninjas')
def info_ninja():
    return render_template('ninjas.html', name='Ninja Thao')

app.run(debug=True)