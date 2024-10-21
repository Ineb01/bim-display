from datetime import datetime

def dummy():
    return [
        {"line": "1", "eta": datetime.now().strftime("%H:%M:%S"), "etl": datetime.now().strftime("%H:%M:%S"), "time": 1, "dir": "Univ.", "stop": "Moz."},
        {"line": "2", "eta": datetime.now().strftime("%H:%M:%S"), "etl": datetime.now().strftime("%H:%M:%S"), "time": 15, "dir": "Univ.", "stop": "Moz."},
        {"line": "3", "eta": datetime.now().strftime("%H:%M:%S"), "etl": datetime.now().strftime("%H:%M:%S"), "time": 35, "dir": "Hbf.", "stop": "Burg."},
        {"line": "4", "eta": datetime.now().strftime("%H:%M:%S"), "etl": datetime.now().strftime("%H:%M:%S"), "time": int(datetime.now().strftime("%S")), "dir": "Hbf.", "stop": "Burg."},
    ]
