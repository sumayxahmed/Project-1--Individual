import pandas as pd
import os

# === Define project base directory (cross-platform safe) ===
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_FILE = os.path.join(BASE_DIR, 'data', 'insurance.csv')
CLEANED_FILE = os.path.join(BASE_DIR, 'data', 'cleaned_insurance.csv')

# === Stage 1: Load the data from CSV file ===
def load_data(path=DATA_FILE):
    """
    Reads the insurance data into a pandas DataFrame.
    Raises an error if the file is not found.
    """
    if not os.path.exists(path):
        raise FileNotFoundError(f"File not found: {path}")
    return pd.read_csv(path)

# === BMI Category Function ===
def bmi_category(bmi):
    """
    Categorizes BMI into Underweight, Normal, Overweight, or Obese.
    """
    if bmi < 18.5:
        return 'Underweight'
    elif bmi < 25:
        return 'Normal'
    elif bmi < 30:
        return 'Overweight'
    else:
        return 'Obese'

# === Stage 2: Transform and clean the data ===
def transform_data(df):
    """
    Cleans and transforms the insurance DataFrame:
    - Drops duplicate rows
    - Encodes 'sex' and 'smoker' as numeric
    - One-hot encodes 'region'
    - Adds a BMI category column
    """
    # Drop duplicates
    df = df.drop_duplicates()

    # Encode categorical variables
    df['sex'] = df['sex'].map({'male': 0, 'female': 1})
    df['smoker'] = df['smoker'].map({'no': 0, 'yes': 1})
    df = pd.get_dummies(df, columns=['region'], drop_first=True)

    # Add BMI category
    df['bmi_category'] = df['bmi'].apply(bmi_category)

    return df

# === Stage 3: Save cleaned data ===
def save_cleaned_data(df, path=CLEANED_FILE):
    """
    Writes the cleaned DataFrame to a CSV file without the index.
    """
    df.to_csv(path, index=False)

# === Stage 4: Quick data analysis ===
def analyze_data(df):
    """
    Prints summary statistics, BMI category counts, and correlation matrix.
    """
    print("=== Summary Statistics ===")
    print(df.describe(include='all'))

    print("\n=== BMI Category Counts ===")
    print(df['bmi_category'].value_counts())

    print("\n=== Correlation Matrix ===")
    print(df.corr(numeric_only=True))

# === Run ETL if script is executed directly ===
if __name__ == "__main__":
    print ("ETL scripts started...") 
    try:
        df = load_data()
        df_transformed = transform_data(df)
        save_cleaned_data(df_transformed)
        analyze_data(df_transformed)
    except Exception as e:
        print(f"[ERROR] {e}")
