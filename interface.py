import MySQLdb as sql

global db

db = sql.connect(
    host='',
    user='',
    passwd='',
    db='')

class dboject:

    def __init__(self):
        global db
        self.db = db
        self.cursor = self.db.cursor()
    
    def select(self, table):
        self.cursor.execute(f'SELECT * FROM {table}')
        return self.cursor.fetchall()

    def create(self, table, prm):
        self.cursor.execute(f'CREATE TABLE {table} ({prm})')
        self.db.commit()
    
    def insert(self, table, prm, vls):
        self.cursor.execute(f'INSERT INTO {table} ({prm}) VALUES ({vls})')
        self.db.commit()