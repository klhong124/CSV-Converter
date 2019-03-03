import codecs
import csv
import json
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

def csv2json(csvpath):
    print(Fore.GREEN +"\nConverting .csv file to JSON format...")
    with codecs.open(csvpath, "r", "utf-8")  as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=',', quotechar='"')
        data = [col for col in csv_reader]
    print ("\t\t\t\t...convert completed!")
    return json.dumps(data)