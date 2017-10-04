import MySQLdb
import time
import random
import socket
import hashlib



# Open database connection
try:
  db = MySQLdb.connect(host="raspberrypi",user="pc",passwd="a1b3c569",db="test")
# prepare a cursor object using cursor() method
  cursor = db.cursor()
except:
  db = MySQLdb.connect(host="raspberrypi",user="pc",passwd="a1b3c569")
# prepare a cursor object using cursor() method
  cursor = db.cursor()
  print("no database")

#-----------------------------------------------------------------------------------------------------
def dbconn():
   global db
   global cursor
   db.close()
   cursor.close()
   db = MySQLdb.connect(host="raspberrypi",user="pc",passwd="a1b3c569",db="test")
   cursor = db.cursor()
   
#-----------------------------------------------------------------------------------------------------   
def DBversion():
    # execute SQL query using execute() method.
    cursor.execute("SELECT VERSION()")
    # Fetch a single row using fetchone() method.
    data = cursor.fetchone()
    return(data[0])    
#-----------------------------------------------------------------------------------------------------    
def register(benutzername,password,first_name, last_name, alter, geschlecht):
    
    
    id = getid()

    register = ("INSERT INTO user(benutzername,password,id,first_name, last_name, alt,geschlecht) VALUES (%s,%s,%s,%s,%s,%s,%s)" )
    cursor.execute(register,(benutzername,password,id, first_name, last_name, alter, geschlecht) )
    db.commit()
    return("OK")
    
#-----------------------------------------------------------------------------------------------------    
def getid():
    
    t = long( time.time() * 1000 )
    r = long( random.random()*100000000000000000L )
    try:
        a = socket.gethostbyname( socket.gethostname() )
    except:
        # if we can't get a network address, just imagine one
        a = random.random()*100000000000000000L
    data = str(t)+' '+str(r)+' '+str(a)
    data = hashlib.md5(data).hexdigest()

    return data
#-----------------------------------------------------------------------------------------------------
def setupdb():
 #  try:
    cursor.execute("CREATE DATABASE test")
    db.commit()
    dbconn()
    cursor.execute("CREATE TABLE user (benutzername TEXT, password TEXT, id TEXT,first_name TEXT, last_name TEXT, alt INTEGER,geschlecht TEXT)")
    db.commit()
    return ("database created")
 #  except:
  #  return("ERROR")
#-----------------------------------------------------------------------------------------------------    
def getuserid(username):
    sql = ("SELECT * FROM user where benutzername = %s")
    cursor.execute(sql,username)
    data = cursor.fetchone()
    retid = data[2]
    return retid
#----------------------------------------------------------------------------------------------------- 
    


