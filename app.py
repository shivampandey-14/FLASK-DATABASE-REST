from itertools import product
from flask import Flask, request, jsonify
import mysql.connector
import json

# Init app
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="FLASK_DATABASE_REST"
)
cursor = mydb.cursor()
app = Flask(__name__)


# Create a Product
@app.route('/product', methods=['POST'])
def add_product():
    name = request.args['name']
    description = request.args['description']
    price = request.args['price']
    qty = request.args['qty']

    sql = "INSERT INTO `product` (`name`, `description`, `price`, `qty`) VALUES (%s, %s, %s, %s)"
    cursor.execute(sql, (name, description, price, qty))
    mydb.commit()

    return jsonify({"name": name, "description": description, "price": price, "qty":qty})


# Get all Products
@app.route('/product', methods=['GET'])
def get_products():
    items = []
    sql = "select id, name ,description, price, qty from product"
    cursor.execute(sql)
    rows = cursor.fetchall()
    for row in rows:
        items.append({"id":row[0],"name":row[1],"description":row[2],"price":row[3],"qty":row[4]})
    return json.dumps(items)


# Get Single
@app.route('/product/<id>', methods=['GET'])
def get_product(id):
    items = []
    sql = "select id, name ,description, price, qty from product where id = '"+id+"'"
    cursor.execute(sql)
    rows = cursor.fetchall()
    for row in rows:
        items.append({"id":row[0],"name":row[1],"description":row[2],"price":row[3],"qty":row[4]})
    return json.dumps(items)


# Update a Product
@app.route('/product/<id>', methods=['PUT'])
def update_product(id):
    name = request.args['name']
    description = request.args['description']
    price = request.args['price']
    qty = request.args['qty']

    sql = "UPDATE `product` set name = %s, description = %s, price = %s, qty=%s where id = %s"
    cursor.execute(sql, (name, description, price, qty, id))
    mydb.commit()

    return jsonify({"name": name, "description": description, "price": price, "qty":qty})



# Get Single
@app.route('/product/<id>', methods=['DELETE'])
def delete_product(id):
    items = []
    sql = "select id, name ,description, price, qty from product where id = '"+id+"'"
    cursor.execute(sql)
    rows = cursor.fetchall()
    for row in rows:
        items.append({"id":row[0],"name":row[1],"description":row[2],"price":row[3],"qty":row[4]})
        
    sql = "delete from product where id = '"+id+"'"
    cursor.execute(sql)
    return json.dumps(items)

# Run server
if __name__ == '__main__':
    app.run(debug = True)
