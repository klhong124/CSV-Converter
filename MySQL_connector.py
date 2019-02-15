import pymysql.cursors
connection = pymysql.connect(
  host='localhost',
  user='root',
  password='root',
  db='cc_logistics',
  charset='utf8mb4',
  cursorclass=pymysql.cursors.DictCursor
)

def insert(logistic_id,product_list,origin_address,shipping_address,order_date,user_id,customer_info):
  with connection.cursor() as cursor:
    cursor.execute(f'''
    INSERT INTO `order_request` (`id`, `logistic_id`, `product_list`, `origin_address`, `shipping_address`, `invoice_id`, `order_date`, `user_id`, `customer_info`) 
    VALUES (
      null,
      {logistic_id},
      "{product_list}",
      "{origin_address}",
      "{shipping_address}",
      "{order_date}",
      1,
      {user_id},
      "{customer_info}"
      );
    ''')
    connection.commit()
    connection.close()

