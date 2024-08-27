import sqlite3
import os

def db_path():
    project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    db_path = os.path.join(project_dir, 'data', 'raw', 'olimpicos.db')
    return db_path

def create_table():
    create_table_medal_table()
    create_medal_table_by_sport()

def create_table_medal_table():
    try:
        with sqlite3.connect(db_path()) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS Medal_table (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    Rank INTEGER NOT NULL,
                    Country TEXT NOT NULL UNIQUE,
                    Gold INTEGER NOT NULL,
                    Silver INTEGER NOT NULL,
                    Bronze INTEGER NOT NULL,
                    Total INTEGER NOT NULL        
                )
            ''')
    except sqlite3.Error as e:
        print(f"Error al crear la tabla: {e}")
def create_medal_table_by_sport():
    try:
        with sqlite3.connect(db_path()) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS Medal_table_by_sport (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    Country TEXT NOT NULL,
                    Sport TEXT NOT NULL,                
                    Gold INTEGER NOT NULL,
                    Silver INTEGER NOT NULL,
                    Bronze INTEGER NOT NULL,
                    Total INTEGER NOT NULL,
                    FOREIGN KEY (Country) REFERENCES Medal_table(Country)       
                )
            ''')
    except sqlite3.Error as e:
        print(f"Error al crear la tabla: {e}")

def create_medal_medals_per_event():
    try:
        with sqlite3.connect(db_path()) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS Medal_per_event (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    Country TEXT NOT NULL,
                    Sport TEXT NOT NULL, 
                    Sport_test TEXT NOT NULL,
                    Sportsman TEXT NOT NULL,   
                    Medal INTEGER NOT NULL,
                    FOREIGN KEY (Country) REFERENCES Medal_table(Country),
                    FOREIGN KEY (Sport) REFERENCES Medal_table_by_sport(Sport)       
                )
            ''')
    except sqlite3.Error as e:
        print(f"Error al crear la tabla: {e}")




def insert_value(rank, country, gold, silver, bronze, total):
    if not isinstance(rank, int) or not isinstance(country, str) or not isinstance(gold, int) or not isinstance(silver, int) or not isinstance(bronze, int) or not isinstance(total, int):
        raise ValueError("Datos inválidos: asegúrate de que country sea un string y las medallas sean enteros.")
    try:
        with sqlite3.connect(db_path()) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO Medal_table (Rank, Country, Gold, Silver, Bronze, Total) 
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (rank, country, gold, silver, bronze, total))
            print("Datos guardados exitosamente.")
            conn.commit()
    except sqlite3.Error as e:
        print(f"Error al insertar valores: {e}")


def insert_value_data_sports(country,sport, gold, silver, bronze, total):
    if not isinstance(country, str) or not isinstance(sport, str) or not isinstance(gold, int) or not isinstance(silver, int) or not isinstance(bronze, int) or not isinstance(total, int):
        raise ValueError("Datos inválidos: asegúrate de que country sea un string y las medallas sean enteros.")
    try:
        with sqlite3.connect(db_path()) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO Medal_table_by_sport (Country,Sport ,Gold, Silver, Bronze, Total) 
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (country,sport,gold, silver, bronze, total))
            print("Datos guardados exitosamente.")
            conn.commit()
    except sqlite3.Error as e:
        print(f"Error al insertar valores: {e}")


