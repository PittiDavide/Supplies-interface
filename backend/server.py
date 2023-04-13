from flask import Flask, send_from_directory, jsonify
from flask_mysqldb import MySQL
from flask_cors import CORS
from datetime import datetime
import os


app = Flask(__name__)
CORS(app)

# MySQL configurations
app.config['MYSQL_HOST'] = os.environ['MYSQL_HOST']
app.config['MYSQL_PORT'] = os.environ.get("MYSQL_PORT") or 3306
app.config['MYSQL_USER'] = os.environ['MYSQL_USER']
app.config['MYSQL_PASSWORD'] = os.environ.get('MYSQL_PASSWORD')
app.config['MYSQL_DB'] = os.environ['MYSQL_DB']

mysql = MySQL(app)


@app.cli.command("create_tables")
def create_tables():
    with app.open_resource("schema.sql", mode="r") as f:
        cursor = mysql.connection.cursor()
        cursor.execute(f.read())
    print("Initialized the database.")


# Path for all the static files (compiled JS/CSS, etc.)


@app.route('/<path:path>')
def send_static(path):
    return send_from_directory('static', path)


@app.route('/', methods=['GET'])
def redirect_to_index():
    return send_from_directory('static', 'index.html')


@app.route('/database_insert', methods=['GET'])
def database_insert():
    cursor = mysql.connection.cursor()
    cursor.execute(
        ''' INSERT INTO `goods`(`id_g`, `name`) VALUES (1,'g1')''')
    cursor.execute(
        ''' INSERT INTO `goods`(`id_g`, `name`) VALUES (2,'g2')''')
    cursor.execute(
        ''' INSERT INTO `supplier`(`id_s`, `name`, `address`) VALUES (1, 's1', 'a1@gmail')''')
    cursor.execute(
        ''' INSERT INTO `supplier`(`id_s`, `name`, `address`) VALUES (2, 's2', 'a2@gmail')''')
    cursor.execute(''' INSERT INTO `supplies`(`id_supplies`, `price`, `delivery_time`, `quantity`, `quantity_for_sale`, `quantity_sale`, `value`, `value_sale`, `s_date`, `e_date`, `date_sale`, `season`, `season_sale`, `id_s`, `id_g`) VALUES (1, 20, 10, 100, 50, 10, 100, 20, '2019-01-01', '2019-01-10', 20, 'september', 20, 1, 1)''')
    cursor.execute(''' INSERT INTO `supplies`(`id_supplies`, `price`, `delivery_time`, `quantity`, `quantity_for_sale`, `quantity_sale`, `value`, `value_sale`, `s_date`, `e_date`, `date_sale`, `season`, `season_sale`, `id_s`, `id_g`) VALUES (2, 20, 10, 100, 50, 10, NULL, NULL, NULL, NULL, NULL, 'september', 20, 2, 2)''')
    mysql.connection.commit()
    cursor.close()
    return "inserted"

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
    date = datetime.strptime(date, '%Y-%m-%d').date()
    cursor = mysql.connection.cursor()
    # select all the supplies joined whit suppliers and whit the goods table to get the name of the goods, the date and the quantity
    cursor.execute(''' SELECT * FROM supplies inner JOIN supplier ON supplies.id_s = supplier.id_s 
    inner JOIN goods ON supplies.id_g = goods.id_g WHERE goods.name = %s AND supplies.quantity >= %s''', (name, quantity))
    suppliers = cursor.fetchall()
    array = []
    for i in suppliers:
        # if a element is null or 0, change it in a int 0
        price = i[1] or 0
        quantity_discount = i[5] or 0
        value_discount = i[7] or 0
        season_discount = i[12] or 0
        date_discount = i[10] or 0
        print(price, quantity)
        started_price = price * quantity
        total_price = started_price
        print(total_price)
        # if quantity required is more than the quantity of the supplies
        if (quantity > i[3]):
            return "quantity required is more than the quantity of the supplies"
        out = {
            # id_supplies, price, delivery_time, quantity, quantity_for_sale, quantity_sale, value, value_sale, s_date, e_date,date_sale, season,seson_sale, id_s,id_g,id_s,name_s,address,id_g,name_g
            "id_supplies": i[0],
            "price": price,
            "delivery_time": i[2],
            "quantity": i[3],
            "quantity_for_sale": i[4],
            "quantity_sale": quantity_discount,
            "value": i[6],
            "value_sale": value_discount,
            "s_date": i[8],
            "e_date": i[9],
            "date_sale": date_discount,
            "season": i[11],
            "seson_sale": season_discount,
            "id_s": i[13],
            "id_g": i[14],
            "name_s": i[16],
            "address": i[17],
            "name_g": i[19],
        }
        # if the quantity for sale is not null
        if (i[4] != 0 and i[4] is not None and quantity_discount != 0):
            out["quantity_discount"] = "offers a " + \
                str(quantity_discount) + "% discount if you order " + \
                str(i[4]) + " pcs or more"
            if (quantity >= i[4]):
                total_price = total_price - \
                    (started_price * quantity_discount / 100)

        else:
            out["quantity_discount"] = "no discount"
        # if the season for sale and seosn is not null or 0
        if (i[11] != 0 and i[11] is not None and season_discount != 0):
            out["season_discount"] = "offers a " + \
                str(season_discount) + \
                "% for purcheases placed in " + str(i[11])
        else:
            out["season_discount"] = "no discount"
        # if the date for sale, e_date and s_date is not null
        if (date_discount and i[9] is not None and i[9] != 0 and i[8] is not None and i[8] != 0):
            out["date_discount"] = "offers a " + str(date_discount) + "% discount for purcheases between " + \
                str(i[8]) + " and " + str(i[9])
            if (date >= i[8] and date <= i[9]):
                total_price = total_price - \
                    (started_price * date_discount / 100)
        else:
            out["date_discount"] = "no discount"
        # if the value and value sale is not null
        if (i[6] != 0 and i[6] is not None and value_discount != 0):
            out["value_discount"] = "offers a " + \
                str(value_discount) + "% discount for purcheases of minimum " + \
                str(i[6]) + "€"
            if (started_price >= i[6]):
                total_price = total_price - \
                    (started_price * value_discount / 100)
        else:
            out["value_discount"] = "no discount"
        print(total_price)
        out["total_price"] = total_price
        array.append(out)
    cursor.close()
    return jsonify(array)


@app.after_request
def apply_caching(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
