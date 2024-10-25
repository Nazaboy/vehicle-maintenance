import pandas as pd
import yaml

def load_data(config_path='config/config.yaml'):
    with open(config_path, 'r') as file:
        config = yaml.safe_load(file)
        
    file_path = config['file_paths']['raw_data']
    data = pd.read_csv(file_path)
    return data
