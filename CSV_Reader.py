import codecs
import PATH_controll
import csv
import json
import colorama
import JSON_generator
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

def csv2json(csvpath):
    print(Fore.GREEN +"\nConverting .csv file to JSON format...")
    with codecs.open(csvpath, "r", "utf-8")  as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=',', quotechar='"')
        data = [col for col in csv_reader]
        if(len(json.loads(json.dumps(data))[0].keys())<4):
            print(Fore.RED+"\t\t\t\t...csv format error!")
            print(Fore.RED+Back.YELLOW+"\n\t\t\t!--ERROR--! \t\t\t\t")
            JSON_generator.log_update(PATH_controll.csvname, "csv format","N/A")
            quit()
    print ("\t\t\t\t...convert completed!")
    JSON_generator.json_write(json.dumps(data))
    return json.dumps(data)