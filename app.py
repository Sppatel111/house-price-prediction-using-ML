from flask import Flask, request, render_template, redirect,session,url_for
from flask_mysqldb import MySQL

app= Flask(__name__)

#database connectivity
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='sneha'
app.config['MYSQL_DB']='house_price'

mysql = MySQL(app)

app.secret_key = 'usdfuhsfha84isjf'  #for session management

#login page
@app.route('/')
def landing():
    return render_template('landing.html')

@app.route('/user_login',methods=['GET','POST'])
def user_login():
    msg = ''
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM USER_ACCOUNTS WHERE email = %s AND password = %s", (email, password))
        result = cursor.fetchone()
        cursor.close()
        
        #app.logger.info("Result: %s", result)
        
        if result: 
            session['email']=email
            
            return redirect(url_for('home'))
             
        else:
            msg = 'Incorrect email or password!'
            
    return render_template('user_login.html',msg=msg)

#  registration page
@app.route('/user_register', methods=['GET', 'POST'])
def user_register():
    if request.method == 'POST' and 'email' in request.form and 'name' in request.form and 'password' in request.form and 'role' in request.form:
        email = request.form['email']
        name = request.form['name']  
        password = request.form['password']
        role = request.form['role']
        
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO user_accounts (email, name, password, role) VALUES (%s, %s, %s, %s)", (email, name, password, role))
        mysql.connection.commit()
        cursor.close()

        return redirect(url_for('user_login'))
    
    return render_template('user_register.html')


# Choose option page
@app.route('/home', methods=['GET','POST'])
def home():
    
    if 'email' in session: 
        
        if request.method=='POST':
        
            option = request.form['option']
           
            if option == 'buy':
                return redirect(url_for('buy_home'))
            
            elif option == 'sell':
                return redirect(url_for('sell_home'))
    
        return render_template('home.html')
    
    else:
        return redirect(url_for('user_login'))


#Buy page
@app.route('/buy_home', methods=['GET', 'POST'])
def buy_home():
    if 'email' in session:
        
        email = session.get('email')
        
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT name FROM USER_ACCOUNTS WHERE email = %s", (email,))
        name = cursor.fetchone()[0]
        cursor.close()

    
        return render_template('buy_home.html',name=name)
    else:
        return redirect(url_for('user_login'))

#Sell page
@app.route('/sell_home', methods=['GET', 'POST'])
def sell_home():
    if 'email' in session:
        
        email = session.get('email')
        
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT name FROM USER_ACCOUNTS WHERE email = %s", (email,))
        name = cursor.fetchone()[0]
        cursor.close()
        
    
        return render_template('sell_home.html', name=name)
    else:
        return redirect(url_for('user_login'))

#Predict page



if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0", port=5000)