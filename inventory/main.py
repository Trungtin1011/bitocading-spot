from flask import Flask
from routes import routes

# Init app
app = Flask(__name__)

# Register routes
app.register_blueprint(routes)

# Run Server
if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=8080)
