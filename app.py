from flask import Flask
import MySQLdb

app = Flask(__name__)
app.config.from_pyfile('config.py')

db = MySQLdb.connect(user=app.config.get("USER"), host=app.config.get("HOST"),  port=app.config.get("PORT"), database=app.config.get("DATABASES"))

from views import  *

if __name__ == '__main__':
    app.run(debug=True)
