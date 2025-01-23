from datetime import datetime, timedelta
import random
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

client = MongoClient(os.getenv('DB_TO'))
db = client['time_series_samples']

def generate_data(sensor_id, start_time, delta, entries):
    data = []
    current_time = start_time
    for _ in range(entries):
        temperature = round(random.uniform(10, 35), 1)
        humidity = random.randint(30, 90)
        entry = {
            "createdAt": current_time,
            "metaData": { "sensorId": sensor_id },
            "temperature": temperature,
            "humidity": humidity
        }
        data.append(entry)
        current_time += timedelta(minutes=delta)
    return data

sensor_data = []
entries = 100000
start_time = datetime.now()
sensor_data.extend(generate_data("sensor1", start_time, 1, entries))
sensor_data.extend(generate_data("sensor2", start_time, 1, entries))
sensor_data.extend(generate_data("sensor3", start_time, 1, entries))

db["sensorData"].insert_many(sensor_data)

