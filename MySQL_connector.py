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
  cursorclass=pymysql.cursors.DictCursor
)
def check(data):
  print(Fore.GREEN +"\nChecking shipper_id exist in database...")
  with connection.cursor() as cursor:
    result = cursor.execute(f'''
      SELECT
        `shipper_id`
      FROM
        `shipper_table`
      WHERE
        `name` = '{data['shipper_name']}'
    ''')
    cursor.close()
  return result

def create_shipper(data):
  print(Fore.GREEN +"\nCreating shipper_id...")
  with connection.cursor() as cursor:
    cursor.execute(f'''
      INSERT INTO 
        `shipper_table` 
      VALUES (
        NULL,
        '{data["shipper_name"]}', 
        'test', 
        'test', 
        CURRENT_TIMESTAMP, 
        CURRENT_TIMESTAMP, 
        NULL
      )
    ''')
    connection.commit()
    cursor.close()
    print("\t...shipper_id created!")



def create_order(data):
  print(Fore.GREEN +"\nCreating order...")
  # with connection.cursor() as cursor:
  #   cursor.execute(f'''

  #   ''')
  #   connection.commit()
  #   cursor.close()