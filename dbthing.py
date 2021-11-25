#!/usr/bin/env pyton3

"""
Paste this into a terminal and keep that terminal open while working with this: 
ssh -L 3306:groucho.it.uu.se:3306 -o TCPKeepAlive=yes -o ServerAliveInterval=10 -o HostKeyAlgorithms=+ssh-rsa toni1357@beurling.it.uu.se

However, since that doesn't work for some reason, the easiest thing to do is:
SCP the file to Arrhenius: scp dbthing.py toni1357@arrhenius.it.uu.se:/home/toni1357/db1
Connect to Arrhenius: ssh toni1357@arrhenius.it.uu.se
Run the file on Arrhenius instead, because Arrhenius seems to be more updated and doesn't need the weird SSH fix
"""

import pymysql

def sql_query( query
             , sqlhost   = 'groucho.it.uu.se'
             , sqlport   = 3306
             , sqluser   = 'ht21_2_group_4'
             , sqlpasswd = 'pwd_4'
             , sqldb     = 'ht21_2_project_group_4'
             ): 
    with pymysql.connect( host = sqlhost, port = sqlport, user = sqluser, passwd = sqlpasswd, db = sqldb ) as conn:
        cur = conn.cursor()
        cur.execute(query)
        output = cur.fetchall()
    return output

def sql_print( rows ):
    maxwidths = []
    for col in zip(*rows):
        maxwidths.append(max(map(lambda _: max([len(str(_)), 8]), col)))
    rowlists = []
    for row in rows:
        rowlists.append([ f"{str(row[i]):{maxwidths[i]}s}" for i in range(len(row)) ])
    print('#'*(sum(maxwidths)+len(maxwidths)*3+3))
    for rowlist in rowlists:
        print(f"#| {' | '.join(rowlist)} |#")
    print('#'*(sum(maxwidths)+len(maxwidths)*3+3))
        
sql_print(sql_query('select * from product'))
