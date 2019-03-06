import PATH_controll
import json
import os
import datetime

def json_write(data):
    with open(PATH_controll.reviewpath, 'w') as json_review:
            json_review.write(data)

def log_update(name,status):
    def json_reboot():
        with open(PATH_controll.csvname, 'w') as csv_log:
            csv_log.write('''[\n{"name": "csv_init", "time": "2000-01-01 00:00:00", "status": "init_success"}]''')
    try:
        with open(PATH_controll.csvname) as csv_log:
            try:
                json.load(csv_log)
            except:
                json_reboot()
    except:
        json_reboot()

    with open(PATH_controll.csvname, 'rb+') as csv_log:
        csv_log.seek(-1, os.SEEK_END)
        csv_log.truncate()

    with open(PATH_controll.jsonpath, 'a') as csv_log:
        def json_append(name,status):
            data = {}
            data["name"] = name
            data["time"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            data["status"] = status
            csv_log.write(",\n"+json.dumps(data)+"]")
        json_append(name,status)