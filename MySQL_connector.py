import pymysql.cursors
import JSON_generator
import colorama
import PATH_controll
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
  try:
    print(Fore.GREEN +"\nChecking shipper_id exist in database...")
    with connection.cursor() as cursor:
      result = cursor.execute(f'''
        SELECT
          `id`
        FROM
          `users`
        WHERE
          `name` = '{data['shipper_name']}'
      ''')
      cursor.close()
    if result:
      return list(cursor)[0]["id"]
    else:
      return 0
  except:
      print(Fore.RED+"\t\t\t\t...data[{shipper_name}] missing!")
      print(Fore.RED+Back.YELLOW+"\n\t\t\t!--ERROR--! \t\t\t\t")
      JSON_generator.log_update(PATH_controll.csvname, "shipper_name")
      quit()

def create_shipper(data):
  try:
    data["shipper_email"]
  except KeyError:
    data["shipper_email"] = "NULL"
  with connection.cursor() as cursor:
    try:
      cursor.execute(f'''
        INSERT INTO 
          `users` 
        VALUES (
          NULL,
          '{data["shipper_name"]}', 
          '{data["shipper_email"]}', 
          'password', 
          CURRENT_TIMESTAMP, 
          CURRENT_TIMESTAMP, 
          NULL,
          2
        );
      ''')
      shipper_id = connection.insert_id()
      connection.commit()
      print(f"\t\t\t\t...shipper_id[{shipper_id}] created!")
    except:
      print(Fore.RED+"\t\t\t\t...data[{shipper_email}] error!")
      print(Fore.RED+Back.YELLOW+"\n\t\t\t!--ERROR--! \t\t\t\t")
      JSON_generator.log_update(PATH_controll.csvname, "shipper_email")
      quit()
    try:
      cursor.execute(f'''
        INSERT INTO 
          `users_detail`(id)
          VALUES (
          '{shipper_id}'
        );
      ''')
      connection.commit()
      print("\t\t\t\t...invoice_process initialized!")
    except:
      print(Fore.RED+"\t\t\t\t...data[{shipper_id}] missing!")
      print(Fore.RED+Back.YELLOW+"\n\t\t\t!--ERROR--! \t\t\t\t")
      JSON_generator.log_update(PATH_controll.csvname, "interal error")
      quit()

  cursor.close()
  return shipper_id

def create_order(data, shipper_id):
  print(Fore.GREEN +f"\nCreating order by shipper_id[{shipper_id}]...")
  invoice_id = create_invoice(shipper_id)
  invoice_init(data,invoice_id)
  return invoice_id

def create_invoice(shipper_id):
  try:
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
  except:
    print(Fore.RED+"\t\t\t\t...data[{shipper_id}] missing!")
    print(Fore.RED+Back.YELLOW+"\n\t\t\t!--ERROR--! \t\t\t\t")
    JSON_generator.log_update(PATH_controll.csvname, "interal error")
    quit()
    
  return invoice_id

def invoice_init(data,invoice_id):
   with connection.cursor() as cursor:
      try:
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
      except:
        print(Fore.RED+"\t\t\t\t...data[{shipper_id}] missing!")
        print(Fore.RED+Back.YELLOW+"\n\t\t\t!--ERROR--! \t\t\t\t")
        JSON_generator.log_update(PATH_controll.csvname, "interal error")
        quit()
      try:
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
      except:
        print(Fore.RED+"\t\t\t\t...data[{invoice_receiver}] missing!")
        print(Fore.RED+Back.YELLOW+"\n\t\t\t!--ERROR--! \t\t\t\t")
        JSON_generator.log_update(PATH_controll.csvname, "receiver_name,receiver_address,receiver_contact")
        quit()
      try:
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
      except:
        print(Fore.RED+"\t\t\t\t...data[{invoice_detail}] missing!")
        print(Fore.RED+Back.YELLOW+"\n\t\t\t!--ERROR--! \t\t\t\t")
        JSON_generator.log_update(PATH_controll.csvname, "quantity,weight")
        quit()

      cursor.close()
