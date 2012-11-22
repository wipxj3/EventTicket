__author__ = 'DEXTER'
import sqlite3

conn = sqlite3.connect("test.db")
conn.execute ("""
              CREATE TABLE QRs (
                  requestID INTEGER PRIMARY KEY AUTOINCREMENT,
                  qrImage TEXT ,
                  qrInfo TEXT ,
                  qrHash TEXT UNIQUE);
             """)