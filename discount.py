#!/usr/bin/env python3

import dbthing as dbt

if __name__ == "__main__":
    pids = [ pid[0] for pid in dbt.tunneled_sql('select ProductID from product') ]
    pid = ''
    while True:
        pid = int(input('Product ID: ')) or ''
        if pid in pids: break
        print('Invalid product ID, try again!')
    discount = dbt.tunneled_sql(f"select Discount from product where ProductID={pid}")
    new_discount = input(f"Discount: [{float(discount[0][0])}]: ") or discount
    dbt.tunneled_sql(f"update product set Discount={new_discount} where ProductId={pid}")
