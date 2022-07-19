#!/usr/bin/env python

# minimal example using Kerberos auth
import sys
import os
import re
import pyodbc

driver='{ODBC Driver 17 for SQL Server}'
server = sys.argv[1]
database = sys.argv[2]

# trusted_connection uses kerberos ticket and ignores UID and PASSWORD in connection string
# https://docs.microsoft.com/en-us/sql/connect/odbc/linux-mac/using-integrated-authentication?view=sql-server-ver15

try:
    cnxn = pyodbc.connect(driver=driver, server=server, database=database, trusted_connection='yes')
    cursor = cnxn.cursor()
except pyodbc.Error as ex:
    msg = ex.args[1]
    if re.search('No Kerberos', msg):
        print('You must login using kinit before using this script.')
        exit(1)
    else:
        raise

# Sample select query
cursor.execute("SELECT @@version;")
row = cursor.fetchone()
while row:
    print(row[0])
    row = cursor.fetchone()
print('success!!')
