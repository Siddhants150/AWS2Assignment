from flask import Flask, render_template, url_for, request
from flaskext.mysql import MySQL
from datetime import datetime
# import MySQLdb.cursors

curDTObj = datetime.now()
app = Flask(__name__)
# current date


app = Flask(__name__)
app.config['MYSQL_DATABASE_HOST'] = 'siddhantdbmysql.cldb1lgd5bay.us-east-1.rds.amazonaws.com'
app.config['MYSQL_DATABASE_USER'] = 'admin'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'logDb'
app.config['MYSQL_PORT'] = '3306'
mysql = MySQL(app)

@app.route('/', methods = ['POST', 'GET'])
def index():
    post = {}
    dateStr = datetime.now().strftime('%Y%m%d%H%M%S')
    cur = mysql.get_db().cursor()
    cur.execute("INSERT INTO log(entry) VALUES (%s)", (dateStr))
    mysql.get_db().commit()
    post[0] = [dateStr]
    print(dateStr)
    return render_template("index.html", dateStr = dateStr)

if __name__ == "__main__":
    app.run(debug = False)