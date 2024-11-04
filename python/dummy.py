from datetime import datetime
from flask import send_file
import io

def dummy():
    return [
        {"line": "1", "eta": datetime.now().strftime("%H:%M:%S"), "etl": datetime.now().strftime("%H:%M:%S"), "time": 1, "dir": "Univ.", "stop": "Moz."},
        {"line": "2", "eta": datetime.now().strftime("%H:%M:%S"), "etl": datetime.now().strftime("%H:%M:%S"), "time": 15, "dir": "Univ.", "stop": "Moz."},
        {"line": "3", "eta": datetime.now().strftime("%H:%M:%S"), "etl": datetime.now().strftime("%H:%M:%S"), "time": 35, "dir": "Hbf.", "stop": "Burg."},
        {"line": "4", "eta": datetime.now().strftime("%H:%M:%S"), "etl": datetime.now().strftime("%H:%M:%S"), "time": int(datetime.now().strftime("%S")), "dir": "Hbf.", "stop": "Burg."},
    ]

def dummy_bitmap():
    booleans = list()
    bytess = bytearray()
    for i in range(0,200):
        for j in range(0, 200):
            if(i > j):
                booleans.append(True)
            else:
                booleans.append(False)
    for i in range(0, int((len(booleans))/8)):
        bytess.append(sum(map(lambda x: x[1] << 7-x[0], enumerate(booleans[i*8:i*8+7]))))
    return send_file(
                     io.BytesIO(bytess),
                     mimetype='image/bitmap'
               )