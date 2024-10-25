import logging
import yaml

def setup_logging(config_path='config/config.yaml'):
    with open(config_path, 'r') as file:
        config = yaml.safe_load(file)
        
    logging.basicConfig(filename=config['logging']['file'], level=config['logging']['level'],
                        format='%(asctime)s - %(levelname)s - %(message)s')
