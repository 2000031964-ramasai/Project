from flask import Flask, render_template, request,redirect,url_for,flash,session
from jinja2 import defaults
from flask_mysqldb import MySQL
from forms import LoginForm
from forms import RegisterForm
import MySQLdb.cursors

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ramasai@2002'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Ramasai@08'
app.config['MYSQL_DB'] = 'myown'

db = MySQL(app)


@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")


@app.route('/contact')
def contact():
    return render_template("contact.html")


@app.route('/aboutus')
def about():
    return render_template("aboutus.html")


@app.route('/login',methods =['GET','POST'])
def login():
    form = LoginForm(request.form)
    if form.validate() and request.method == 'POST':
        username = request.form.get('username')
        password = request.form['password']
        cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM REGISTER1 WHERE username = %s and password = %s', (username,password,))
        account = cursor.fetchone()
        if account:
            session['loged_in'] = True
            session['user'] = username
            return redirect(url_for('index'))
        else:
            flash('Invalid Credentials ..! Username or Password Incorrect')
    return render_template('login.html', form=form)


@app.route('/register',methods =['GET','POST'])
def register():
    form = RegisterForm(request.form)
    if form.validate() and request.method == 'POST':
        username = request.form.get('username')
        password = request.form['password']
        repassword = request.form['repassword']
        gender = request.form.get('gender')
        phoneno = request.form.get('phoneno')
        email = request.form.get('email')
        address = request.form.get('address')

        cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM REGISTER1 WHERE username = %s', (username,))
        account = cursor.fetchone()
        if not account:
            cursor.execute('INSERT INTO REGISTER1 VALUES(NULL,%s,%s,%s,%s,%s,%s,%s)',
                           (username,password,repassword,gender,phoneno,email,address,))
            db.connection.commit()
            return redirect(url_for('login'))
        else:
            flash('User already existed..! Try another UserName')

    return render_template('register.html', form=form)

@app.route('/logout')
def logout():
    session.pop('loged_in',None)
    session.pop('user',None)
    return redirect(url_for('login'))
@app.route('/user', defaults={'name': 'Guest'})
@app.route('/user/<name>')
def user(name):
    context = [

        {
            'stuid': '2000031964',
            'stuname': 'ramasai',
            'maths': 50,
            'phy': 50,
            'chem': 50,
        },
        {
            'stuid': '2000012345',
            'stuname': 'kalyan',
            'maths': 50,
            'phy': 50,
            'chem': 50,

        }
    ]
    return render_template('user.html', data=name, con=context)


if __name__ == '__main__':
    app.run(debug=True)
