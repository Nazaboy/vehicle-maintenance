import pandas as pd
import logging

def clean_data(df):
    # Handle missing values
    df['Last_Service_Date'] = pd.to_datetime(df['Last_Service_Date'], errors='coerce')
    df['Warranty_Expiry_Date'] = pd.to_datetime(df['Warranty_Expiry_Date'], errors='coerce')
    df.fillna(method='ffill', inplace=True)  # Forward-fill as a placeholder

    # Log duplicates before removal
    duplicates = df[df.duplicated(subset=['Vehicle_Model', 'Odometer_Reading'], keep=False)]
    if not duplicates.empty:
        logging.info("Found duplicate records before removal:")
        logging.info(duplicates)

    # Remove duplicates based on specific columns
    df.drop_duplicates(subset=['Vehicle_Model', 'Odometer_Reading'], inplace=True)
    
    logging.info("Duplicates removed based on 'Vehicle_Model' and 'Odometer_Reading'.")

    return df
