#!/usr/bin/env python3

import pymysql
import pandas as pd
from sshtunnel import SSHTunnelForwarder
import passwd

""" These are the input parameters, change accordingly
"""
ssh_host = 'arrhenius.it.uu.se'
ssh_port = 22
ssh_user = passwd.ssh_user
ssh_pass = passwd.ssh_pass
# If you're not tunneling, anything above this line may just be left as-is
sql_hostname      = 'groucho.it.uu.se'
sql_port          = 3306
sql_username      = passwd.sql_username
sql_password      = passwd.sql_password
sql_main_database = 'ht21_2_project_group_4'
# Arguably the most important thing you're doing
query = 'select * from product'

def tunneled_sql( query
                , ssh_host = ssh_host
                , ssh_port = ssh_port
                , ssh_user = ssh_user
                , ssh_pass = ssh_pass
                , sql_hostname = sql_hostname
                , sql_port     = sql_port    
                ):
    with SSHTunnelForwarder( (ssh_host, ssh_port)
                           , ssh_username = ssh_user
                           , ssh_password = ssh_pass
                           , remote_bind_address = (sql_hostname, sql_port)
                           ) as tunnel:
        return sql_query( query, sql_hostname = '127.0.0.1', sql_port = tunnel.local_bind_port )

def sql_query( query
               , sql_hostname      = sql_hostname     
               , sql_port          = sql_port         
               , sql_username      = sql_username     
               , sql_password      = sql_password     
               , sql_main_database = sql_main_database
               ):
    with pymysql.connect( host   = sql_hostname
                        , user   = sql_username
                        , passwd = sql_password
                        , db     = sql_main_database
                        , port   = sql_port
                        ) as conn:
        return sql_cursor( query, conn )
        #return pd.read_sql_query( query, conn ) # Change to this line if you prefer using pandas for handling data visualization

def sql_cursor( query, conn ):
    cur = conn.cursor()
    cur.execute(query)
    data = cur.fetchall()
    return sql_print( data )

def sql_print( data ):
    maxwidths = []
    result = ''
    for col in zip(*data):
        maxwidths.append(max(map(lambda _: max([len(str(_)), 8]), col)))
    rows = []
    for row in data:
        rows.append([ f"{str(row[i]):{maxwidths[i]}s}" for i in range(len(row)) ])
    result += '#'*(sum(maxwidths)+len(maxwidths)*3+3)+'\n'
    for row in rows:
        result += f"#| {' | '.join(row)} |#"+'\n'
    result += '#'*(sum(maxwidths)+len(maxwidths)*3+3)
    return result

""" Make sure to comment the version you're not using
"""
print(tunneled_sql( query )) # Using tunneling
#print(sql_query( query ))  # NOT using tunneling
