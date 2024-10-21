from datetime import datetime

def dummy():
    return [
        {"line": 1, "time": datetime.now().strftime("%H:%M:%S"), "dir": "Univ.", "stop": "Moz."},
        {"line": 2, "time": datetime.now().strftime("%H:%M:%S"), "dir": "Univ.", "stop": "Moz."},
        {"line": 3, "time": datetime.now().strftime("%H:%M:%S"), "dir": "Hbf.", "stop": "Burg."},
        {"line": 4, "time": datetime.now().strftime("%H:%M:%S"), "dir": "Hbf.", "stop": "Burg."},
    ]
