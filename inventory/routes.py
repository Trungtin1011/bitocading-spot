from flask import Blueprint, request, jsonify
from models import Product
import sqlite3
import logging

# Init logger
logging.getLogger('werkzeug').disabled = False
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Init database
def initDB():
    try:
        conn = sqlite3.connect('./data/inventory.db')
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS inventory
                    (id int, name text, description text, price real)''')
        conn.commit()
        conn.close()
        logger.info("Database initialized!")
        return True
    except Exception as e:
        logger.error(e.args[0])
        return False

db = initDB()

def initDBConnection():
    if db == True:
        try:
            conn = sqlite3.connect('./data/inventory.db')
            return conn
        except Exception as e:
            logger.error(e.args[0])
            return e.args[0]
    else:
        return 0

# Init routes
routes = Blueprint('routes', __name__)

@routes.route('/products', methods=['GET'])
def get_products():
    conn = initDBConnection()
    if conn != 0:
        try:
            cursor = conn.cursor()
            cursor.execute('''SELECT * FROM inventory''')
            res = cursor.fetchall()
            conn.commit()
            conn.close()

            logger.info(res)
            return res
        except Exception as e:
            logger.error(e.args[0])
            return e.args[0]
    else:
        logger.error("Database has not been initialized!")
        return "Database has not been initialized!"

@routes.route('/products', methods=['POST'])
def add_product():
    id = request.json['id']
    name = request.json['name']
    description = request.json['description']
    price = request.json['price']
    new_product = Product(id, name, description, price)
    # products.append(new_product.__dict__)

    conn = initDBConnection()
    if conn != 0:
        try:
            conn = sqlite3.connect('./data/products.db')
            cursor = conn.cursor()
            cursor.execute(f"""INSERT INTO inventory VALUES
              ('{new_product.id}','{new_product.name}','{new_product.description}','{new_product.price}')""")
            conn.commit()
            conn.close()

            logger.info("Data written to Database")
            return "Data written to Database"

        except Exception as e:
            logger.error(e.args[0])
            return e.args[0]
    else:
        logger.error("Database has not been initialized!")
        return "Database has not been initialized!"

# @routes.route('/products/<id>', methods=['GET'])
# def get_product(id):
#     for product in products:
#         if product['id'] == int(id):
#             logger.info(jsonify(products))
#             return jsonify(product)
#     logger.error(jsonify({"message": "Product not found"}), 404)
#     return jsonify({"message": "Product not found"}), 404
