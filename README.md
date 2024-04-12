# House Price Prediction using ML

[![License: Creative Commons](https://img.shields.io/badge/License-CC_BY--NC_4.0-blue.svg)](https://creativecommons.org/licenses/by-nc/4.0/deed.en)

## Description

House Price Prediction using ML is a machine learning-based application that predicts house prices based on various features such as area type, size, total square footage, bathrooms, balconies, and price per square foot. This system can be used by real estate professionals and individuals to estimate house prices before making purchasing or selling decisions.

The workflow involves:
1. Loading a pre-trained Gradient Boosting Regressor model for Bangalore and Pune locations.
2. Accepting user inputs for house features and location.
3. Preprocessing the input data using label encoding for categorical features.
4. Using the ML model to predict the house price.
5. Displaying the predicted price to the user.

## Tech Stack

- **Backend:** Python Flask
- **Database:** MySQL (for user authentication and session management)
- **Machine Learning:** Scikit-learn (Gradient Boosting Regressor)
- **Frontend:** HTML, CSS
- **IDE:** Spyder
- **Python:** 3.11.5
- **Flask:** 3.0.0
- **Scikit-learn:** 1.3.2

## Demo

![Demo](/static/demo.gif)

[Download Demo Video](static/demo.mp4)

## System Flow Diagram

![System Flow Diagram](/static/System_flow.png)

## Usage

1. Clone this repository:

    ```bash
    git clone https://github.com/Sppatel111/house-price-prediction.git
    ```

2. Set up the MySQL database (for user authentication and session management) by creating a database named `house_price_prediction` and importing the necessary schema.

3. Run the Flask application:

    ```bash
    python app.py
    ```

4. Access the application in your web browser at `http://localhost:5000`.

## Contribution

Contributions to this project are welcome! Here's how you can help:

- Test the application and provide feedback on its functionality and user experience.
- Enhance the ML model by tuning hyperparameters or exploring different algorithms.
- Improve the frontend design and user interface.
- Report any bugs or issues you encounter while using the application.
- Submit pull requests with new features, optimizations, or bug fixes.

Please note that commercial use of the code or any derived work is not allowed under the [Creative Commons Attribution-NonCommercial 4.0 International License](https://creativecommons.org/licenses/by-nc/4.0/deed.en). Contributions should align with the non-commercial nature of the project.

Feel free to fork the repository, make your changes, and submit a pull request. Your contributions are appreciated!

## License

This project is licensed under the [Creative Commons Attribution-NonCommercial 4.0 International License](https://creativecommons.org/licenses/by-nc/4.0/deed.en). See the [LICENSE](LICENSE) file for details.
