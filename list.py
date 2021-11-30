#!/usr/bin/env python3

import dbthing as dbt

if __name__ == "__main__":
    dids = [ did[0] for did in dbt.tunneled_sql('select DepartmentID from department') ]
    did = ''
    while True:
        did = int(input('Department ID: ')) or ''
        if did in dids: break
        print('Invalid department ID, try again!')
    
    if () == dbt.tunneled_sql(f"select DepartmentID from department where parent_depart={did}"):
        data = dbt.tunneled_sql(f"select ProductID,ProductTitle,Unit_price,Discount,tax from product where id_department={did}")
        chdata = [ ('Product ID', 'Product title', 'Retail price') ]
        for row in data: 
            chdata.append(( row[0], row[1], (1+float(row[4]))*(float(row[2])*float(row[3])) ))
    else:
        data = dbt.tunneled_sql(f"Select DepartmentId,Department_Title from department where parent_depart={did}")
        chdata = [ ('Department ID', 'Department name') ]
        for row in data:
            chdata.append(( row[0], row[1] ))
    dbt.sql_print(chdata)
