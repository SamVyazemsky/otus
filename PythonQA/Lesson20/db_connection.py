from sqlalchemy import create_engine


# engine = create_engine("mysql://store:qwerty@localhost/shop")
# result = engine.execute(
#             "SELECT * FROM `oc_order")
# row = result.fetchall()
# result.close()
# print(row)
e = create_engine("sqlite:///:memory:")
e.execute("""
    create table customers (cust_id integer primary key,
                            cust_name varchar
                            )
""")
print(e.execute("select * from customers"))




