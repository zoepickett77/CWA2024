#import statements here
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

def predict_wellbeing(sound_level, light_level, temperature):
    df = pd.DataFrame([[sound_level, light_level, temperature]], columns=['sound_intensity', 'light_intensity', 'temp'])
    return model.predict(df)[0]

file = pd.read_csv('advanced.csv')
print(file)
#ar1
#defining x(independent variables affecting wellbeing) and y(dependent variable result)
factors = file[['sound_intensity', 'light_intensity', 'temp']]
wellbeing = file['avg_wellbeing']
factors_train, factors_test, wellbeing_train, wellbeing_test = train_test_split(factors, wellbeing, test_size=0.2, random_state=0)

# Creating the Linear Regression model
model = LinearRegression()

# Fitting the model with the training data
model.fit(factors_train, wellbeing_train)

# Predicting mood scores for the test set
wellbeing_pred = model.predict(factors_test)

print("model completed")

print("Multiple Linear Regression Model Complete!")



print("Please enter the following questions")
sound = int(input("Enter sound level. Can be any integer from 0-255: "))
light = int(input("Enter light intensity. Can be any integer from 1-255: "))
temp = float(input("Enter the temperature. Can be anything from 1-40: "))

predicted_wellbeing = predict_wellbeing(sound, light, temp)  
print("\nThe Predicted Wellbeing Score for the values entered is", predicted_wellbeing)
