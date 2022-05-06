from flask import Flask, render_template, url_for, request
from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage
import mysql.connector
from mysql.connector import Error
from datetime import datetime,date

now=datetime.now()
cur_time=now.strftime("%H:%M:%S")

eidn=3
app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def index():
  QTc_result = False
  if request.method == 'POST':
    form = request.form
    heart_rate = request.form['hr']
    qt_int = request.form['qt']
    print(heart_rate+"    "+qt_int)

  #new
    
    mydb = mysql.connector.connect(
      host='localhost',
      database='druglist',
      user='root',
      password='1234'
    )
      
    mycursor = mydb.cursor()
    screenshot = request.files['file']
    filename = secure_filename(screenshot.filename)
    MEDIA_ROOT = "./media/"
    screenshot.save(MEDIA_ROOT+filename)

    sql = "INSERT INTO entry3(eid,loc,text,img,dat,timestamp) VALUES (%s,%s,%s,%s,%s,%s)"
    val=(eidn,heart_rate,qt_int, filename,now,cur_time)
    mycursor.execute(sql, val)

    mydb.commit()

    print(mycursor.rowcount, "record inserted.")
    
  return render_template('index.html')
  
 

if __name__ == "__main__":
  app.run(debug=True)
