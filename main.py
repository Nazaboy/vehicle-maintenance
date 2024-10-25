import logging
from src.extract import load_data
from src.clean import clean_data
from src.transform import transform_data
from src.quality_checks import data_quality_checks
from src.load import load_to_db
from src.utils import setup_logging

def main():
    setup_logging()
    
    # Step 1: Extract Data
    df = load_data()
    
    # Step 2: Clean Data
    df = clean_data(df)
    
    # Step 3: Transform Data
    df = transform_data(df)
    
    # Step 4: Quality Checks
    if data_quality_checks(df):
        # Step 5: Load Data
        load_to_db(df)
    else:
        logging.warning("Data quality checks failed.")

if __name__ == "__main__":
    main()
