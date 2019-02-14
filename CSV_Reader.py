import codecs
import csv

def csv2json(csvpath):
    with codecs.open(csvpath, "r", "utf-8")  as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            print(len(row))