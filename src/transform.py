from sklearn.preprocessing import LabelEncoder, StandardScaler

def transform_data(df):
    # Encoding categorical features
    label_encoder = LabelEncoder()
    for col in ['Vehicle_Model', 'Maintenance_History', 'Fuel_Type']:
        df[col] = label_encoder.fit_transform(df[col])
    
    # Scaling numeric features
    scaler = StandardScaler()
    df[['Mileage', 'Odometer_Reading']] = scaler.fit_transform(df[['Mileage', 'Odometer_Reading']])
    return df
