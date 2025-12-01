"""
Data Cleaning and Preprocessing Functions for COVID-19 Vaccination Outcomes
"""

import pandas as pd
import numpy as np
from datetime import datetime

def load_and_validate_data(file_path):
    """
    Load dataset and perform initial validation
    """
    df = pd.read_csv(file_path)
    df['Week End'] = pd.to_datetime(df['Week End'])
    
    print(f"Dataset loaded: {df.shape[0]} rows, {df.shape[1]} columns")
    print(f"Time range: {df['Week End'].min()} to {df['Week End'].max()}")
    
    return df

def create_age_groups(age_group):
    """
    Standardize age group categories
    """
    if age_group == 'All':
        return None
    elif age_group in ['0-4', '5-11']:
        return '0-10 Years'
    elif age_group in ['12-17', '18-29']:
        return '11-24 Years'
    elif age_group in ['30-49']:
        return '25-50 Years'
    elif age_group in ['50-64']:
        return '50-80 Years'
    elif age_group in ['65-79', '80+']:
        return '80+ Years'
    else:
        return age_group

def handle_missing_values(df):
    """
    Strategic handling of missing values
    """
    df_clean = df.copy()
    
    # Population columns - zeros likely represent missing data
    population_cols = ['Population Unvaccinated', 'Population Vaccinated', 'Population Boosted']
    for col in population_cols:
        if col in df_clean.columns:
            df_clean[col] = df_clean[col].replace(0, np.nan)
    
    # Create missing data flags
    rate_columns = ['Unvaccinated Rate', 'Vaccinated Rate', 'Boosted Rate']
    for col in rate_columns:
        if col in df_clean.columns:
            df_clean[f'{col}_missing'] = df_clean[col].isnull()
    
    return df_clean

def create_derived_metrics(df):
    """
    Create calculated metrics for analysis
    """
    df_derived = df.copy()
    
    # Total outcomes
    outcome_cols = ['Outcome Unvaccinated', 'Outcome Vaccinated', 'Outcome Boosted']
    if all(col in df.columns for col in outcome_cols):
        df_derived['Total_Outcomes'] = df[outcome_cols].sum(axis=1, skipna=True)
    
    # Risk reduction calculations
    if 'Unvaccinated Rate' in df.columns and 'Vaccinated Rate' in df.columns:
        mask = (df['Unvaccinated Rate'] > 0) & df['Unvaccinated Rate'].notna() & df['Vaccinated Rate'].notna()
        df_derived.loc[mask, 'Vaccinated_Risk_Reduction'] = (
            (df.loc[mask, 'Unvaccinated Rate'] - df.loc[mask, 'Vaccinated Rate']) / 
            df.loc[mask, 'Unvaccinated Rate'] * 100
        )
    
    # Temporal features
    df_derived['Year'] = df_derived['Week End'].dt.year
    df_derived['Month'] = df_derived['Week End'].dt.month
    df_derived['Week_Number'] = df_derived['Week End'].dt.isocalendar().week
    
    # Vaccination periods
    def time_period(date):
        if date < pd.Timestamp('2021-12-01'):
            return 'Early Vaccination'
        elif date < pd.Timestamp('2022-06-01'):
            return 'Mid Vaccination'
        else:
            return 'Late Vaccination'
    
    df_derived['Vaccination_Period'] = df_derived['Week End'].apply(time_period)
    
    return df_derived

def clean_dataset(file_path, save_path=None):
    """
    Main data cleaning pipeline
    """
    # Load data
    df = load_and_validate_data(file_path)
    
    # Apply cleaning steps
    df['Age_Group_New'] = df['Age Group'].apply(create_age_groups)
    df_filtered = df[df['Age_Group_New'].notna()]
    
    df_clean = handle_missing_values(df_filtered)
    df_final = create_derived_metrics(df_clean)
    
    # Save cleaned data
    if save_path:
        df_final.to_csv(save_path, index=False)
        print(f"Cleaned dataset saved to: {save_path}")
    
    return df_final

if __name__ == "__main__":
    # Example usage
    cleaned_df = clean_dataset('../data/raw/COVID19_Vaccination_Outcomes.csv', 
                             '../data/cleaned/COVID19_Vaccination_Outcomes_Cleaned.csv')
