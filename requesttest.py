__author__ = 'Administrator'
import requests
import os
from bs4 import BeautifulSoup
import pymysql

connection = pymysql.connect(host = 'localhost',
                             user = 'root',
                             password = 'yjgd@123',
                             db = 'test',
                             charset = 'utf8mb4',)
repone = connection.ping()
print (repone)
