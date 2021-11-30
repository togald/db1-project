#!/usr/bin/env python3

import dbthing

data = dbthing.tunneled_sql('show tables')

dbthing.sql_print(data)
