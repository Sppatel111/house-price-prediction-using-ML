import pandas as pd
import numpy as np

banglore_df = pd.read_csv("dataset/Bangalore  house data.csv")
pune_df = pd.read_csv("dataset/Pune house data.csv")



# Treating Banglore Dataset
print("Dataset banglore:")
print(banglore_df.head())
print(banglore_df.columns)
print(banglore_df['area_type'].unique())

# column area_type
print(banglore_df['area_type'].value_counts())

# availability
print(banglore_df['availability'].value_counts())

# size(BHK)
print(banglore_df['size(BHK)'].value_counts())

# find null
print(banglore_df.isnull().sum())

# drop society
df2 = banglore_df.drop(['society'], axis='columns')
print(df2.shape)

# drop null location 
print(df2.dropna(subset = ['location'], how ='all', inplace= True))


# Replace 'bedrooms' with 'BHK' in the 'size(BHK)' column
df2['size(BHK)'] = df2['size(BHK)'].str.replace('Bedroom', 'BHK')
print(df2['size(BHK)'])

#function to BHK   
def remove_bhk(text):
    if isinstance(text, str):
        return int(text.split()[0])
    elif isinstance(text, float) and not np.isnan(text):
        return int(text)
    else:
        return None
    
# Apply the function to the 'size(BHK)' column
df2['size(BHK)'] = df2['size(BHK)'].apply(remove_bhk)


# Fill null values with the average value
df2['size(BHK)'] = df2['size(BHK)'].astype(str).fillna('2 BHK')
df2['bath'].fillna(df2['bath'].mean(), inplace=True)
df2['balcony'].fillna(df2['balcony'].mean(), inplace=True)



# For total_sqft
def convert_sqft_to_num(x):
    tokens = x.split('-')
    if len(tokens) == 2:
        return (float(tokens[0]) + float(tokens[1])) / 2
    try:
        return float(x)
    except:
        return None

df2['total_sqft'] = df2['total_sqft'].apply(convert_sqft_to_num)
df2 = df2[df2['total_sqft'].notnull()]

# Add new feature called price per square feet
df2['price_per_sqft'] = df2['price'] * 100000 / df2['total_sqft']
print(df2)

df2_stats = df2['price_per_sqft'].describe()
print(df2_stats)

print(df2.isnull().sum())

# Save the updated dataset
df2.to_csv('updated_bangaloredataset.csv', index=False)



'''
# Treating Pune Dataset
print("Dataset banglore:")
print(pune_df.head())
print(pune_df.columns)
print(pune_df['area_type'].unique())

# column area_type
print(pune_df['area_type'].value_counts())

# availability
print(pune_df['availability'].value_counts())

# size(BHK)
print(pune_df['size(BHK)'].value_counts())

# find null
print(pune_df.isnull().sum())

# drop society
df2 = pune_df.drop(['society'], axis='columns')
print(df2.shape)

# drop null location 
print(df2.dropna(subset = ['location'], how ='all', inplace= True))


# Replace 'bedrooms' with 'BHK' in the 'size(BHK)' column
df2['size(BHK)'] = df2['size(BHK)'].str.replace('Bedroom', 'BHK')
print(df2['size(BHK)'])

#function to BHK   
def remove_bhk(text):
    if isinstance(text, str):
        return int(text.split()[0])
    elif isinstance(text, float) and not np.isnan(text):
        return int(text)
    else:
        return None
    
# Apply the function to the 'size(BHK)' column
df2['size(BHK)'] = df2['size(BHK)'].apply(remove_bhk)


# Fill null values with the average value
df2['size(BHK)'] = df2['size(BHK)'].astype(str).fillna('2 BHK')
df2['bath'].fillna(df2['bath'].mean(), inplace=True)
df2['balcony'].fillna(df2['balcony'].mean(), inplace=True)



# For total_sqft
def convert_sqft_to_num(x):
    tokens = x.split('-')
    if len(tokens) == 2:
        return (float(tokens[0]) + float(tokens[1])) / 2
    try:
        return float(x)
    except:
        return None

df2['total_sqft'] = df2['total_sqft'].apply(convert_sqft_to_num)
df2 = df2[df2['total_sqft'].notnull()]

# Add new feature called price per square feet
df2['price_per_sqft'] = df2['price'] * 100000 / df2['total_sqft']
print(df2)

df2_stats = df2['price_per_sqft'].describe()
print(df2_stats)

print(df2.isnull().sum())

# Save the updated dataset
df2.to_csv('updated_punedataset.csv', index=False)

'''