# IBMG12-Data-Redundancy-Removal-System

1. Create a virtual environment
2. create a folder drr
3. activate environment
   - venv/Script/activate or go to file in cmd and  run `activate`
4. in drr folder git pull request
   - git init
   - git pull "link-github-repo"
   - 
5. Model Code
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.impute import SimpleImputer
from sklearn.cluster import KMeans

# Step 3: Preprocess the dataset from a CSV file
def preprocess_dataset(csv_file):
    df = pd.read_csv(csv_file)
    
    # Separate numeric and non-numeric columns
    numeric_columns = df.select_dtypes(include=[np.number]).columns
    non_numeric_columns = df.select_dtypes(exclude=[np.number]).columns
    
    # Encode non-numeric columns
    encoded_data = pd.DataFrame()
    for column in non_numeric_columns:
        encoder = LabelEncoder()
        encoded_data[column] = encoder.fit_transform(df[column])
    
    # Impute missing values
    imputer = SimpleImputer(strategy='mean')
    numeric_data_imputed = imputer.fit_transform(df[numeric_columns])
    
    # Scale numeric columns
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(numeric_data_imputed)
    
    # Combine scaled numeric and encoded non-numeric data
    X = np.concatenate((scaled_data, encoded_data), axis=1)
    
    return X, df

# Step 5: Use K-means to identify duplicate records
def identify_duplicates(X):
    kmeans = KMeans(n_clusters=2, random_state=42)  # Assuming there are only two clusters (duplicates and non-duplicates)
    kmeans.fit(X)
    labels = kmeans.labels_
    return labels

# Step 6: Remove duplicate records from the dataset
def remove_duplicates_from_dataset(X, df, labels):
    df['Labels'] = labels
    df_unique = df[df['Labels'] == 1].drop(columns=['Labels'])
    return df_unique

# Load data and preprocess
X_scaled, original_df = preprocess_dataset('/content/drive/MyDrive/dataset/sales.csv')  # Replace 'your_dataset.csv' with your CSV file path

# Identify duplicate records using K-means
labels = identify_duplicates(X_scaled)

# Remove duplicate records from the dataset
cleaned_df = remove_duplicates_from_dataset(X_scaled, original_df, labels)

# Save the cleaned data to a CSV file
cleaned_df.to_csv('/content/drive/MyDrive/dataset/cleaned_sales.csv', index=False)

     
