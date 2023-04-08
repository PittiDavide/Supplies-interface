from flask import Flask, send_from_directory, render_template, request
from flask_mysqldb import MySQL
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# MySQL configurations
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'supplies_database'

mysql = MySQL(app)

# Creating a connection cursor
"""
cursor = mysql.connection.cursor()
 
#Executing SQL Statements
cursor.execute(''' CREATE TABLE table_name(field1, field2...) ''')
cursor.execute(''' INSERT INTO table_name VALUES(v1,v2...) ''')
cursor.execute(''' DELETE FROM table_name WHERE condition ''')
 
#Saving the Actions performed on the DB
mysql.connection.commit()
 
#Closing the cursor
cursor.close()
"""


# Path for all the static files (compiled JS/CSS, etc.)

@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)


# get all the supplier data
@app.route("/suppliers", methods=['GET'])
def get_suppliers():
    cursor = mysql.connection.cursor()
    cursor.execute(''' SELECT * FROM supplier ''')
    suppliers = cursor.fetchall()
    cursor.close()
    return {"suppliers": suppliers}


@app.after_request
def apply_caching(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
