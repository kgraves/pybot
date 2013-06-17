import sqlite3
from datetime import datetime,timedelta

class DB:

  def __init__(self, filename)
    self.filename = filename
    self.age = datetime.now()

  def _open(self):
    self.conn = sqlite3.connect(self.filename)
    self.cur  = self.conn.cursor()

    # self.con = mdb.connect("localhost","pybot","1q2w3e4r","pybot")
    # self.cur = self.con.cursor()
  
  def _close(self):
    self.conn = None
    self.cur.close()

    # self.con = None
    # self.cur.close()

  # IS NOT USED ANYWHERE, NOT IMPLEMENTING AT THIS TIME 
  def _handle(self): global cur
    return None

    # global age
    # now = datetime.now()
    # if now - self.age > timedelta(minutes=5):
      # self.cur.close()
      # self.con = mdb.connect("localhost","pybot","1q2w3e4r","pybot")
      # self.cur = self.con.cursor()

  def select(self, where, what):
    try:
      self._open()
      self.cur.execute("SELECT %s FROM %s" % (what, where))
      data = self.cur.fetchall()
      self._close()
    except:
      data = None
      self._close()

    return data

    # try:
      # self._open()
      # self.cur.execute("""SELECT %s FROM %s""")
      # data = self.cur.fetchall()
      # self._close()
    # except:
      # self._close()
      # return None

    # return data

  def replace(self, where, which, what):
    try:
      self._open()
      self.cur.execute("REPLACE INTO %s (%s) VALUES (%s)" % (where, which, what))
    except:
      # possibly log error or something???
      pass

    self._close()
    return None

    # return data
    # try:
      # self._open()
      # self.cur.execute("""REPLACE INTO %s (%s) VALUES (%s)""",(where, which, what)) 
      # self._close()
    # except:
      # self._close()
      # return None

  # IS NOT USED ANYWHERE, NOT IMPLEMENTING AT THIS TIME 
  def e(self, sql):
    return None

    # try:
      # self._open()
      # self.cur.execute(sql) 
      # if "INSERT" in sql or "REPLACE" in sql:
        # self.con.commit()
        # self._close()
      # elif "SELECT" in sql:
        # e = self.cur.fetchall()
        # self._close()
        # return e
    # except Exception, e:
      # print e
      # self.con.rollback()
      # self._close()
      # return None

  def insert(self, where, which, what):
    try:
      self._open()
      self.cur.execute("INSERT INTO %s (%s) VALUES (%s)" % (where, which, what))
    except:
      # possibly log error or something???
      pass

    self._close()
    return None

    # try:
      # self._open()
      # self.cur.execute("""INSERT INTO %s (%s) VALUES (%s)""",(where, which, what)) 
      # self._close()
    # except:
      # self._close()
      # return None

  def updateSeen(self, who, statement, event):
    # formats data and uses the replace method

    which = 'user_name, statement, event'
    what = str(who) + ' ' + str(statement) + ' ' str(event)
    self.replace('seen', which, what)

    return None

    # self._open()
    # #print "executing REPLACE INTO seen (user_name, statement, event) VALUES ( " + str(who) + " " + str(statement) + " " + str(event) + ")"
    # self.cur.execute("REPLACE INTO seen (user_name, statement, event) VALUES (%s, %s, %s)", (who, statement, event))
    # self._close()

  def getSeen(self, who):
    self._open()
    if who != "":
      self.cur.execute("SELECT user_name, date, statement, event FROM seen WHERE user_name = %s", who)
      data = self.cur.fetchone()
      return data;
      self._close()
    else:
      self._close()
      return None 

  def _insertImg(self, user, url):
    self._open()
    if user == "" or user == None:
      user = "nobody"
    try:
      self.cur.execute("""INSERT INTO img (user, url) VALUES (%s, %s)""", (user, url))
      self.con.commit()
    except:
      self.con.rollback()

    self._close()

  def _getImgs(self):
    self._open()
    try:
      self.cur.execute("""SELECT * FROM img ORDER BY time""")
      data = self.cur.fetchall()
      self._close()
    except:
      self._close()
      return None

    return data

  def _isAdmin(self, username):
    self._open()
    try:
      self.cur.execute("""SELECT * FROM admins WHERE username = %s""",(username))
      data = self.cur.fetchall()
      self._close()
    except:
      self._close()
      return None

    return data
