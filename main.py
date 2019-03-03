import MySQL_connector
import CSV_reader
import json
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
print('\033[2J'+Fore.YELLOW+Back.RED+"\tWelcome to "+Fore.WHITE+Back.RED+"CC_LOGISTICS"+Fore.YELLOW+Back.RED+" .csv converter\t")

data = json.loads(CSV_reader.csv2json("demo.csv"))[0]

if MySQL_connector.check(data):
    print("\t\t\t\t...shipper_id exist!")
    MySQL_connector.create_order(data)
else:
    print("\t\t\t\t...shipper_id not exist!")
    MySQL_connector.create_shipper(data)
