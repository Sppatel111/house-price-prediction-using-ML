from flask import Flask, request, render_template, redirect,session,url_for
from flask_mysqldb import MySQL
import joblib
from sklearn.preprocessing import LabelEncoder
import numpy as np 
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


# Predict page
@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        
        # Get the input data from the form
        area_type = request.form['area_type']
        
        label_encoder = LabelEncoder()
        area_type = label_encoder.fit_transform([area_type])[0]
        
        size_bhk = int(request.form['size_bhk'])
        total_sqft = float(request.form['total_sqft'])
        bath = int(request.form['bath'])
        balcony = int(request.form['balcony'])
        price_per_sqft = float(request.form['price_per_sqft'])
        
        locality = request.form['locality']
        
        if locality=="Bangalore":  
            # Load the saved model
            loaded_model = joblib.load('bangalore_gbr_model.joblib')
            
            # Make a prediction using the loaded model
            prediction = loaded_model.predict([[area_type, size_bhk, total_sqft, bath, balcony, price_per_sqft]])
            #print("Prediction value", prediction)
            
            
        if locality=="Pune":  
            # Load the saved model
            loaded_model = joblib.load('pune_gbr_model.joblib')
            
            # Make a prediction using the loaded model
            prediction = loaded_model.predict([[area_type, size_bhk, total_sqft, bath, balcony, price_per_sqft]])
            
        # Format the prediction as a currency value in lakh
        #prediction_in_lakh = "{:.2f} lakh".format(prediction[0])
        
        # Convert the prediction to an integer value in rupees
        #prediction_integer = int(prediction[0] * 100000)
        
        # Convert the prediction to an integer value in rupees using NumPy
        prediction_integer = np.round(prediction[0] * 100000).astype(int)
        
        return render_template('prediction_result.html', prediction=prediction_integer)
    
    return render_template('predict.html')



if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0", port=5000)