import pymysql.cursors
connection = pymysql.connect(
  host='localhost',
  user='root',
  password='',
  db='cc_logistics',
  charset='utf8mb4',
  cursorclass=pymysql.cursors.DictCursor
)

def insert(logistic_id,product_list,origin_address,shipping_address,order_date,user_id,customer_info):
  with connection.cursor() as cursor:
    cursor.execute('''
    INSERT INTO `order_request` (`id`, `logistic_id`, `product_list`, `origin_address`, `shipping_address`, `invoice_id`, `order_date`, `user_id`, `customer_info`) 
    VALUES (
      null,
      1,
      "[{'product_id':'2','product_name':'王泉','qty':'11','description':'Wong330ml','weight':'330g'},{'product_id':'1','product_name':'玉泉','qty':'12','description':'CreamSoda330mL','weight':'330g'}]",
      'cityu,kln',
      'cityu,ac2,kln',
      '2019-01-3111:06:03',
      1,
      2,
      "<'customer_name':'玉王牌','contact':'59883943','description':'SoftDrinkCompany','address':'cityu,ac2,kln'}"
      );
    ''')
    connection.commit()
    connection.close()

