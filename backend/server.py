from flask import Flask, send_from_directory, render_template, request, jsonify
from flask_mysqldb import MySQL
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# MySQL configurations
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'supplies_db'

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


@app.route("/search/<string:name>/<int:quantity>/<string:date>", methods=['GET'])
def search(name, quantity, date):

    cursor = mysql.connection.cursor()
    # select all the supplies joined whit suppliers and whit the goods table to get the name of the goods, the date and the quantity
    cursor.execute(''' SELECT * FROM supplies inner JOIN supplier ON supplies.id_s = supplier.id_s 
    inner JOIN goods ON supplies.id_g = goods.id_g WHERE goods.name = %s AND supplies.quantity >= %s''', (name, quantity))
    suppliers = cursor.fetchall()
    array = []
    for i in suppliers:
        out = {
            # id_supplies, price, delivery_time, quantity, quantity_for_sale, quantity_sale, value, value_sale, s_date, e_date,date_sale, season,seson_sale, id_s,id_g,id_s,name_s,address,id_g,name_g
            "id_supplies": i[0],
            "price": i[1],
            "delivery_time": i[2],
            "quantity": i[3],
            "quantity_for_sale": i[4],
            "quantity_sale": i[5],
            "value": i[6],
            "value_sale": i[7],
            "s_date": i[8],
            "e_date": i[9],
            "date_sale": i[10],
            "season": i[11],
            "seson_sale": i[12],
            "id_s": i[13],
            "id_g": i[14],
            "name_s": i[16],
            "address": i[17],
            "name_g": i[19]
        }
        array.append(out)
    cursor.close()
    return jsonify(array)


@app.after_request
def apply_caching(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
