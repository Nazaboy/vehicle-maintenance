import pandas as pd
import logging

def data_quality_checks(df):
    completeness = df.isnull().sum().sum() == 0
    validity = (df['Last_Service_Date'] <= pd.Timestamp.now()).all()
    duplicates = df[df.duplicated(subset=['Vehicle_Model', 'Odometer_Reading'], keep=False)]
    consistency = duplicates.empty

    logging.info(f"Data Quality - Completeness: {completeness}, Validity: {validity}, Consistency: {consistency}")

    if not consistency:
        logging.warning("Found duplicate records based on 'Vehicle_Model' and 'Odometer_Reading':")
        logging.warning(duplicates)
        
    return completeness and validity and consistency
