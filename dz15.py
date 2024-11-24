"bash"
"pip install requests beautifulsoup4"
import sqlite3

import datetime
import time

def create_db():
    conn = sqlite3.connect('weather.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS weather (
            date TEXT,
            time TEXT,
            temperature REAL
        )
    ''')
    conn.commit()
    conn.close()

def get_temperature():
    url = 'URL'


def insert_data(temperature):
    conn = sqlite3.connect('weather.db')
    cursor = conn.cursor()
    now = datetime.datetime.now()
    cursor.execute('''
        INSERT INTO weather (date, time, temperature) VALUES (?, ?, ?)
    ''', (now.date(), now.time(), temperature))
    conn.commit()
    conn.close()

def update_weather():
    create_db()
    while True:
        temperature = get_temperature()
        insert_data(temperature)
        print(f'Updated: {datetime.datetime.now()}: {temperature}°C')
        time.sleep(1800)

if __name__ == "__main__":
    update_weather()