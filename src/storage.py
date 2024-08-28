import sqlite3
import os

def db_path():
    project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    db_path = os.path.join(project_dir, 'data', 'raw', 'olimpicos.db')
    return db_path

def create_table():
    create_table_medal_table()
    create_medal_table_by_sport()
    create_medal_medals_per_event()
    create_sportsman()

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
                    Link TEXT,   
                    FOREIGN KEY (Country) REFERENCES Medal_table(Country),
                    FOREIGN KEY (Sport) REFERENCES Medal_table_by_sport(Sport)       
                )
            ''')
    except sqlite3.Error as e:
        print(f"Error al crear la tabla: {e}")

def create_sportsman():
    try:
        with sqlite3.connect(db_path()) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS Sportsman (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    Sportsman TEXT NOT NULL, 
                    Date_of_birth TEXT NOT NULL,
                    Age INTEGER NOT NULL,
                    Gender TEXT NOT NULL,  
                    Function TEXT NOT NULL,  
                    Height_m_ft_in TEXT NOT NULL,  
                    FOREIGN KEY (Sportsman) REFERENCES Medal_per_event(Sportsman)
                )
            ''')
    except sqlite3.Error as e:
        print(f"Error al crear la tabla: {e}")


def check_url(field_name):
    try:
        with sqlite3.connect(db_path()) as conn:
            cursor = conn.cursor()
            sql_query = "SELECT Sportsman, Link FROM Medal_per_event WHERE Sportsman = ?"
            cursor.execute(sql_query, (field_name,))
            result = cursor.fetchone()  # Utilizar fetchone() para obtener un solo resultado
            if result:
                return list(result)  # Retornar ambos valores en una lista
            else:
                return []  # Retornar una lista vacía si no hay resultados
    except sqlite3.Error as e:
        print(f"Error al consultar la tabla: {e}")
        return []

    
def get_unique_sportsmen():
    try:
        with sqlite3.connect(db_path()) as conn:
            cursor = conn.cursor()
            sql_query = "SELECT DISTINCT Sportsman FROM Medal_per_event"
            cursor.execute(sql_query)
            results = cursor.fetchall()  # Obtener todos los resultados

            # Convertir la lista de tuplas en una tupla
            unique_sportsmen = tuple(row[0] for row in results)
            return unique_sportsmen

    except sqlite3.Error as e:
        print(f"Error al consultar la tabla: {e}")
        return None


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
            conn.commit()
    except sqlite3.Error as e:
        print(f"Error al insertar valores: {e}")


def insert_value_data_per_event(country,sport, gold, silver, bronze, total):
    if not isinstance(country, str) or not isinstance(sport, str) or not isinstance(gold, int) or not isinstance(silver, int) or not isinstance(bronze, int) or not isinstance(total, int):
        raise ValueError("Datos inválidos: asegúrate de que country sea un string y las medallas sean enteros.")
    try:
        with sqlite3.connect(db_path()) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO Medal_table_by_sport (Country,Sport ,Gold, Silver, Bronze, Total) 
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (country,sport,gold, silver, bronze, total))
            conn.commit()
    except sqlite3.Error as e:
        print(f"Error al insertar valores: {e}")


def insert_value_data_sports(country,sport,sport_test,sportsman, medal, link='null'):
    if not isinstance(country, str) or not isinstance(sport, str) or not isinstance(sport_test, str) or not isinstance(sportsman, str) or not isinstance(medal, str):
        raise ValueError("Datos inválidos")
    try:
        with sqlite3.connect(db_path()) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO Medal_per_event (Country,Sport ,Sport_test, Sportsman, Medal, Link) 
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (country,sport,sport_test, sportsman, medal, link))
            conn.commit()
    except sqlite3.Error as e:
        print(f"Error al insertar valores: {e}")


def insert_sportsman(sportsman, date_of_birth, age, gender, function, height):
    # Validación de tipos de datos
    if not isinstance(sportsman, str):
        raise ValueError("Datos inválidos: 'sportsman' debe ser strings.")
    if not isinstance(date_of_birth, str) or not isinstance(gender, str) or not isinstance(function, str) or not isinstance(height, str):
        raise ValueError("Datos inválidos: 'date_of_birth', 'gender', 'function' y 'height' deben ser strings.")
    if not isinstance(age, int):
        raise ValueError("Datos inválidos: 'age' debe ser un entero.")

    try:
        with sqlite3.connect(db_path()) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO Sportsman (Sportsman, Date_of_birth, Age, Gender, Function, Height_m_ft_in)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (sportsman, date_of_birth, age, gender, function, height))
            conn.commit()
            print("Valores insertados correctamente.")
    except sqlite3.Error as e:
        print(f"Error al insertar valores: {e}")