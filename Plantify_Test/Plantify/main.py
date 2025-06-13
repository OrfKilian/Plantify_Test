# Datei: main.py (robuste Version mit automatischer Tabellenerstellung)
import mariadb

def get_connection():
    try:
        conn = mariadb.connect(
            host="localhost",
            user="placeholder_user",
            password="placeholder_password",
            database="pflanzen_db"
        )
        return conn
    except mariadb.Error as e:
        print(f"Datenbankverbindungsfehler: {e}")
        return None

def create_table_if_not_exists():
    """Erstellt die Tabelle 'pflanzen', falls sie nicht existiert"""
    conn = get_connection()
    if conn is None:
        return False
    
    try:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS pflanzen (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255) NOT NULL
            )
        """)
        
        # Tabelle anlegen, falls sie noch nicht existiert
        
        conn.commit()
        cursor.close()
        conn.close()
        return True
    except mariadb.Error as e:
        print(f"Fehler beim Erstellen der Tabelle: {e}")
        if conn:
            conn.close()
        return False

def get_all_plants():
    # Zunächst versuchen, die Tabelle zu erstellen
    if not create_table_if_not_exists():
        print("Datenbank nicht verfügbar.")
        return []
    
    conn = get_connection()
    if conn is None:
        return []
    
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT id, name FROM pflanzen")
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        return [{'id': r[0], 'name': r[1]} for r in rows]
    except mariadb.Error as e:
        print(f"Fehler beim Abrufen der Pflanzen: {e}")
        if conn:
            conn.close()
        return []

if __name__ == '__main__':
    plants = get_all_plants()
    for plant in plants:
        print(f"Pflanze: {plant['name']}")
