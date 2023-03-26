import sqlite3
from datetime import datetime
import json
import random
def updateData(device_id , level):
    conn = sqlite3.connect('db/test.sqlite')

    current_time = int(datetime.now().strftime("%d%m%Y%H%M%S"))

    cursor = conn.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='DATAPOINT' ''')

    if cursor.fetchone()[0]==1 :
        pass
    else : 
        conn.execute('''CREATE TABLE DATAPOINT("TIME" INT PRIMARY KEY NOT NULL,"DEVICE_ID" TEXT NOT NULL,"LEVEL" INT NOT NULL)''')

    conn.execute(f'INSERT INTO DATAPOINT (TIME,DEVICE_ID,LEVEL) VALUES ("{current_time}", "{device_id}",{level} )')

    conn.commit()
    conn.close()


def retrieve_Data(ranged=None, device_id=None):
    conn = sqlite3.connect("db/test.sqlite")
    current_time = int(datetime.now().strftime("%d%m%Y%H%M%S"))
    date_before = int(datetime.now().strftime("%d%m%Y%H%M%S")) - 1000000000000

    cursor = conn.execute(f"SELECT * FROM DATAPOINT WHERE TIME>{ date_before if ranged==None else ranged[0]} AND TIME<{current_time if ranged==None else ranged[1]} { '' if device_id==None else 'AND DEVICE_ID == '+ device_id }")
    
    data = []
    for i in cursor.fetchall():
        data.append({
            "time": i[0],
            "device_id" : i[1],
            "level" : i[2]
        })
    return (str(json.dumps(data)))
    

# updateData("ESP_32_Home" , random.randint(10 , 90))
# retrieve_Data(ranged=[25032023211810 , 25032023211831])