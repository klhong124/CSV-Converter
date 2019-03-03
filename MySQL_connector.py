import pymysql.cursors
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

connection = pymysql.connect(
  host='localhost',
  user='root',
  password='',
  db='cc_logistics',
  charset='utf8mb4',
  cursorclass=pymysql.cursors.DictCursor)

def check(data):
  print(Fore.GREEN +"\nChecking shipper_id exist in database...")
  with connection.cursor() as cursor:
    result = cursor.execute(f'''
      SELECT
        `shipper_id`
      FROM
        `shipper_table`
      WHERE
        `username` = '{data['shipper_name']}'
    ''')
    cursor.close()
  if result:
    return list(cursor)[0]["shipper_id"]
  else:
    return 0

def create_shipper(data):
  print(Fore.GREEN +"\nCreating shipper_id...")
  with connection.cursor() as cursor:
    cursor.execute(f'''
      INSERT INTO 
        `shipper_table` 
      VALUES (
        NULL,
        '{data["shipper_name"]}', 
        '{data["shipper_email"]}', 
        'password', 
        CURRENT_TIMESTAMP, 
        CURRENT_TIMESTAMP, 
        NULL
      );
    ''')
    shipper_id = connection.insert_id()
    connection.commit()
    cursor.close()
    print(f"\t\t\t\t...shipper_id[{shipper_id}] created!")
  return shipper_id

def create_order(data, shipper_id):
  print(Fore.GREEN +f"\nCreating order by shipper_id[{shipper_id}]...")
  invoice_id = create_invoice(shipper_id)
  invoice_init(data,invoice_id)

def create_invoice(shipper_id):
  with connection.cursor() as cursor:
    cursor.execute(f'''
      INSERT INTO 
        `invoice_table`
      VALUES (
        NULL,
        '{shipper_id}'
      );
    ''')
    invoice_id = connection.insert_id()
    connection.commit()
    cursor.close()
    print(f"\t\t\t\t...invoice[{invoice_id}] created!")
  return invoice_id

def invoice_init(data,invoice_id):
   with connection.cursor() as cursor:
      cursor.execute(f'''
        INSERT INTO 
          `invoice_process` (
            `invoice_id`
            ) 
        VALUES (
          '{invoice_id}'
        );
      ''')
      connection.commit()
      print("\t\t\t\t...invoice_process initialized!")
      cursor.execute(f'''
        INSERT INTO 
          `invoice_receiver`
        VALUES (
          '{invoice_id}',
          '{data["receiver_name"]}', 
          '{data["receiver_address"]}', 
          '{data["receiver_contact"]}'
        );
      ''')
      connection.commit()
      print("\t\t\t\t...invoice_receiver initialized!")
      cursor.execute(f'''
        INSERT INTO 
          `invoice_detail`
        VALUES (
          '{invoice_id}',
          '{data["quantity"]}', 
          '{data["weight"]}', 
          'normal'
        );
      ''')
      connection.commit()
      print("\t\t\t\t...invoice_detail initialized!")
      cursor.close()
      