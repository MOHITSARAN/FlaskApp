from app import app
import subprocess
from flask import render_template,redirect, request, send_file
from models import *


@app.route('/signup', methods=['POST', 'GET'])
def signup():
	if request.method=='POST':
   		username = request.form['username']
   		password = request.form['password']
   		email = request.form['email']
                phone = request.form['phone']
   		insertUser(username,password,email,phone)
		return render_template('login.html')
	else:
   		return render_template('signup.html')

@app.route('/scrapy')
def scrapy():
    spider_name = "quotes"
    subprocess.check_output(['scrapy', 'crawl', spider_name, '-t' , 'csv' , '-o' , 'crawlers.csv' , '-a', 'CSV_DELIMITER="/t"'])
    return send_file('../crawlers.csv',
                     mimetype='text/csv',
                     attachment_filename='crawlers.csv',
                     as_attachment=True)

@app.route('/dashboard', methods=['POST', 'GET'])
def order():
  if request.method=='POST':
      order_status = request.form['order_status']
      order_id = request.form['order_id']
      product_name = request.form['product_name']
      product_url = request.form['product_url']
      cost_price = request.form['cost_price']
      insertOrder(order_status,order_id,product_name,product_url,cost_price)
      rows = fetchorder()
      status= 'Your order has been created.'
      return render_template('dashboard.html',rows=rows,status=status)
  else:
    rows = fetchorder()
    return render_template('dashboard.html',rows=rows)

@app.route('/', methods=['POST', 'GET'])
def login():
        error = None
	if request.method=='POST':
   		username = request.form['username']
   		password = request.form['password']
   		completion = validate(username,password)
   		if completion == False:
   			error = 'Invalid Credentials. Please try again.'
   		else:
   			return redirect('/dashboard')
   	return render_template('login.html',error=error)

@app.route('/logout')
def logout():
    return render_template('login.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)