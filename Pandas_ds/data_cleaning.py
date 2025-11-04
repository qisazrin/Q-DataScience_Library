
# DATA CLEANING AND EXPLORATION
import pandas as pd
import numpy as np
import warnings

# Ignore warnings for cleaner output
warnings.filterwarnings('ignore')

# 1. LOAD DATA
data = pd.read_csv(
    'https://raw.githubusercontent.com/realpython/python-data-cleaning/refs/heads/master/Datasets/BL-Flickr-Images-Book.csv'
)

# Show the first 5 rows to inspect
data.head()


# 2. DROP COLUMNS WITH MANY NaN VALUES
# Columns with many missing values make analysis difficult, so we remove them
drop = [
    'Edition Statement',
    'Corporate Author',
    'Contributors',
    'Corporate Contributors',
    'Former owner',
    'Engraver',
    'Issuance type',
    'Shelfmarks'
]
data.drop(drop, inplace=True, axis=1)


# 3. SET IDENTIFIER AS INDEX
# Check if 'Identifier' column is unique
print("Is 'Identifier' unique?", data['Identifier'].is_unique)

# Set 'Identifier' as the index for easy record access
data = data.set_index('Identifier')
data.head()


# 4. ACCESSING SPECIFIC RECORDS
# Access record with Identifier 206
record_206 = data.loc[206]
print("\nRecord 206:\n", record_206)


# 5. DATA INFO AND INSPECTION
# Quick overview of dataframe: columns, non-null counts, and data types
data.info()

# Access a range of records for 'Date of Publication' column
print("\nDate of Publication (records 1905 onwards):")
print(data.loc[1905:, 'Date of Publication'].head(10))
