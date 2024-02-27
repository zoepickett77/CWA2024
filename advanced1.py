#import statements here
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
file = pd.read_csv('advanced.csv')
print(file)
#predicted_wellbeing = predict_wellbeing(sound_min,sound_max,sound_mean)
#print("The predicted value is", predicted_wellbeing)
#defining x(independant variables effecting wellbeing) and y(dependant variable result)
#ar1
X = file[['sound_min', 'sound_max', 'sound_mean']]
Y = file['avg_wellbeing']