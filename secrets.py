import pymysql.cursors
import pymysql
import re
import os
    
access_token = os.environ["ACCESS_TOKEN"]
db_name      = os.environ["DB_NAME"]
db_password  = os.environ["DB_PASSWORD"]
db_username = os.environ["DB_USERNAME"]
db_hostname     = os.environ["DB_HOSTNAME"]

def getConnection():
    connection = pymysql.connect(host=db_hostname,
                                user=db_username,
                                password=db_password,
                                db=db_name,
                                charset='utf8mb4',
                                cursorclass=pymysql.cursors.DictCursor)
    return connection

def getToken():
    token = access_token
    return token
