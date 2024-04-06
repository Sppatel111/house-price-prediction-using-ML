import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import LabelEncoder
from sklearn.impute import SimpleImputer
import joblib

# Load the dataset
df = pd.read_csv("dataset/updated_bangaloredataset.csv")

# Encode categorical variables
label_encoder = LabelEncoder()
df['area_type'] = label_encoder.fit_transform(df['area_type'])

# Select features and target variable
X = df[['area_type', 'size(BHK)', 'total_sqft', 'bath', 'balcony', 'price_per_sqft']]
y = df['price']



# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=43)

# Initialize the SimpleImputer with strategy='mean'
imputer = SimpleImputer(strategy='mean')

# Fit the imputer on the training data and transform both training and testing data
X_train_imputed = imputer.fit_transform(X_train)
X_test_imputed = imputer.transform(X_test)

# Initialize the Gradient Boosting Regression model
model = GradientBoostingRegressor()

# Train the model
model.fit(X_train_imputed, y_train)

# Make predictions
y_pred = model.predict(X_test_imputed)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error:", mse)

# Calculate R-squared (R2) score
r2 = r2_score(y_test, y_pred)
print("R-squared (R2) Score:", r2)

# Make predictions on the testing set
y_pred_test = model.predict(X_test_imputed)

# Create a DataFrame to compare the actual and predicted values
results_df = pd.DataFrame({'Actual Price': y_test, 'Predicted Price': y_pred_test})
print(results_df)


# Save the model
joblib.dump(model, 'bangalore_gbr_model.joblib') 

# Load the saved model
#loaded_model = joblib.load('gradient_boosting_regression_bmodel.joblib')

# Make predictions using the loaded model
#y_pred_loaded = loaded_model.predict(X_test_imputed)

import matplotlib.pyplot as plt

# Visualize the dataset
plt.figure(figsize=(10, 6))

# Scatter plot for each feature against the target variable
plt.scatter(df['area_type'], df['price'], alpha=0.5, label='Area Type')
plt.xlabel('Area type')
plt.ylabel('Price')
plt.title('Area type vs Price')
plt.legend()
plt.show()

plt.scatter(df['size(BHK)'], df['price'], alpha=0.5, label='Size (BHK)')
plt.xlabel('Area type')
plt.ylabel('Price')
plt.title('Area type vs Price')
plt.legend()
plt.show()

plt.scatter(df['total_sqft'], df['price'], alpha=0.5, label='Total Sqft')
plt.xlabel('Total sqft')
plt.ylabel('Price')
plt.title('Total sqft vs Price')
plt.legend()
plt.show()

plt.scatter(df['bath'], df['price'], alpha=0.5, label='Bath')
plt.xlabel('Bath')
plt.ylabel('Price')
plt.title('Bath vs Price')
plt.legend()
plt.show()

plt.scatter(df['balcony'], df['price'], alpha=0.5, label='Balcony')
plt.xlabel('Balcony')
plt.ylabel('Price')
plt.title('Balcony vs Price')
plt.legend()
plt.show()

plt.scatter(df['price_per_sqft'], df['price'], alpha=0.5, label='Price per Sqft')
plt.xlabel('Price per sqft')
plt.ylabel('Price')
plt.title('Price per sqft vs Price')
plt.legend()
plt.show()



# Create a scatter plot comparing actual prices against predicted prices
plt.figure(figsize=(8, 6))
plt.scatter(y_test, y_pred_test, alpha=0.5, color='blue')
plt.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], color='red', linestyle='--')
plt.title('Actual vs Predicted Prices')
plt.xlabel('Actual Price')
plt.ylabel('Predicted Price')
plt.grid(True)
plt.show()



