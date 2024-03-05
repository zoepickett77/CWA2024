#import statements here
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

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

#Ar2
#Question 1
#What will your wellbeing be with low values of all three factors?
print("-----------------------------------------------------------")
print("What if?..Question One")
print("Let's test what the wellbeing will be if the factor scores are very low")

#Low values for all 3 factors
sound_level = 2
light_level = 70
temp = 5

wellbeing_if_lowscores = predict_wellbeing(sound_level, light_level, temp)  
print("\n The low factors score wellbeing is", wellbeing_if_lowscores)

#What will your wellbeing be with high values for all the 3 factors?
print("-----------------------------------------------------------")
print("What if?...Question Two")
print("Let's test what the wellbeing will be if the factor scores are very high")

# High values for all 3 factors
sound_level = 200
light_level = 200
temp = 40

wellbeing_if_highscores = predict_wellbeing(sound_level, light_level, temp)  
print("\n The higher factors score wellbeing is",wellbeing_if_highscores )

#AR3 Users can view data in a graphical format 
#names of the variables and values for the chart
variable_names = ['wellbeing if lowfactors', 'wellbeing if highfactors']
values = [wellbeing_if_lowscores,wellbeing_if_highscores]

# Creating the bar chart
plt.bar(variable_names, values)

# Adding labels and title
plt.xlabel('Score of Factors')
plt.ylabel('wellbeing score')
plt.title('Bar Chart of 2 what if Predictions')

# Show the plot
plt.show()
