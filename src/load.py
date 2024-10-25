import sqlite3
import yaml

def load_to_db(df, config_path='config/config.yaml'):
    with open(config_path, 'r') as file:
        config = yaml.safe_load(file)
        
    db_path = config['database']['db_path']
    conn = sqlite3.connect(db_path)
    df.to_sql('vehicle_maintenance_records', conn, if_exists='replace', index=False)
    conn.close()
import sqlite3
import yaml

def load_to_db(df, config_path='config/config.yaml'):
    with open(config_path, 'r') as file:
        config = yaml.safe_load(file)
        
    db_path = config['database']['db_path']
    conn = sqlite3.connect(db_path)
    df.to_sql('vehicle_maintenance_records', conn, if_exists='replace', index=False)
    conn.close()
