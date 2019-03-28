import config
import MySQLdb

conn = MySQLdb.connect(host=config.MYSQL['host'],
                       user=config.MYSQL['user'],
                       password=config.MYSQL['password'],
                       db=config.MYSQL['database'])

def run(query):
  cur = conn.cursor()
  cur.execute(query)
  return cur
