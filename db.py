import cx_Oracle
import os
import pandas as pd

LOCATION = r"C:\instantclient_21_6"
os.environ["PATH"] = LOCATION + ";" + os.environ["PATH"]

OracleConnect = cx_Oracle.connect("data", "1234", "localhost:1521/xe")



OracleCursor = OracleConnect.cursor()


oracleSql = """select PEOPLECD, PEOPLENMEN ,REPROLENM, FILMONAMES from All_movie_people_list where PEOPLENM in ('조성은')
"""
OracleCursor.execute(oracleSql)
for i in OracleCursor:
    print(i)
