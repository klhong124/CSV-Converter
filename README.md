# .csv Reader
Read .csv file and insert into database
>Execute by enter `python main.py` in cmd or execure `exe.bat`.

## installation requirement
1. pip install pandas
2. pip install xlrd
3. pip install pymysql
4. pyhon -m pip install colorama

## CSV_Reader.py
> Build the object before encoding it to a JSON string
``` python
import json
data = {}
data['key'] = 'value'
json_data = json.dumps(data)
```

>Open the file,Create a CSV reader. This can be simplified a bit with list comprehension, replacing the for loop with [r for r in reader]
``` python
with open("actors.csv") as f:
    reader = csv.reader(f)
    data = [r for r in reader]
    data.pop(0) # remove header
```

## References
* https://stackoverflow.com/questions/23110383/how-to-dynamically-build-a-json-object-with-python
* https://www.alexkras.com/how-to-read-csv-file-in-python/
* https://www.devdungeon.com/content/colorize-terminal-output-python