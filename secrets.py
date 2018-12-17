import pymysql.cursors
import pymysql
import re

def getConnection():
    connection = pymysql.connect(host='localhost',
                                user='root',
                                password='',
                                db='karyu_db',
                                charset='utf8mb4',
                                cursorclass=pymysql.cursors.DictCursor)
    return connection

#connection: host = 'localhost', user = 'root', pw = '', db = 'karyu_db'
#venom server: host = 'sql9.freemysqlhosting.net', user and db = 'sql9262534', pw = 'BYwDPuPyas'

def getToken():
    token = "NDY4MzIyMzYwNDU4NzM5NzEy.Dja62g.bh354nnwR7dGif4Id480Xl71Cmw"
    return token
