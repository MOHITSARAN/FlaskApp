import sqlite3 as sql

def insertUser(username,password,email,phone):
    with sql.connect("database.db") as con:
        cur = con.cursor()
        cur.execute("INSERT INTO user (username,password,email,phone) VALUES (?,?,?,?)", (username,password,email,phone))
        con.commit()

def validate(username, password):
    completion = False
    with sql.connect("database.db") as con:
    	cur = con.cursor()
    	cur.execute("SELECT username, password FROM user")
    	rows = cur.fetchall()
    	for row in rows:
            dbUser = row[0]
            dbPass = row[1]
            if dbUser==username and dbPass==password:
            	completion = True
    return completion

def insertOrder(order_status,order_id,product_name,product_url,cost_price):
    with sql.connect("database.db") as con:
        cur = con.cursor()
        cur.execute("INSERT INTO orders (order_status,order_id,product_name,product_url,cost_price) VALUES (?,?,?,?,?)", (order_status,order_id,product_name,product_url,cost_price))
        con.commit()

def fetchorder():
    with sql.connect("database.db") as con:
        cur = con.cursor()
        cur.execute("SELECT * FROM orders")
        rows = cur.fetchall()
    return rows