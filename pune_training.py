import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import LabelEncoder
from sklearn.impute import SimpleImputer
import joblib

# Load the dataset
df = pd.read_csv("updated_punedataset.csv")

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
joblib.dump(model, 'pune_gbr_model.joblib') 

# Load the saved model
#loaded_model = joblib.load('gradient_boosting_regression_model.joblib')

# Make predictions using the loaded model
#y_pred_loaded = loaded_model.predict(X_test_imputed)
