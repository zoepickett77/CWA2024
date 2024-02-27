#import statements here
import pandas as pd
from statistics import mean
import csv
import serial
from time import sleep
#function to give a remark on my mood based on avg_mood value
def interpret_mood(avg_mood):
    if avg_mood >= 9:
        return "Excellent mood today, thank god"
    elif avg_mood <  5:
        return "Middlin today, thanks for asking"
    elif 5 <= avg_mood < 9:
        return "Improving thanks."
    else:
        return "Not really sure, not enough info \n"
    #Take them in as integers, as all inputs default to strings
social_wellbeing = int(input("On a scale of 1-10 from bad to good, how is your social well-being?"))
phone_anxiety = int(input("On a scale of 1-10 from addicted to unatached, how is your phone anxiety?"))
study_wellbeing = int(input("On a scale of 1-10 from struggling in school to confident in school, how is your study wellbeing ?"))
avg_wellbeing = round(mean([social_wellbeing,phone_anxiety,study_wellbeing]),2)

print("My Average mood today is ", avg_wellbeing)
df = pd.read_csv('newsound.csv')
#df = pd.read_csv('zpsound.csv')
print(df)

# Convert 'Timestamp' column to datetime, is it necessary
sound_min = df['sound'].min()
sound_max = df['sound'].max()
sound_mean = df['sound'].mean()
#VALIDATION OF DATA BR2
if not isinstance(sound_min, float):
    sound_min = float(sound_min)
if not isinstance(sound_max, float):
    sound_max = float(sound_max)
if not isinstance(sound_mean, float):
    sound_mean = float(sound_mean)
    
print (sound_min,sound_max,sound_mean, avg_wellbeing)
f = open("br1newfile.csv", "a", newline='')
colh = csv.writer(f)
#colh.writerow(["sound_min", "sound_max", "sound_mean", "avg_wellbeing"])
colh.writerow([sound_min, sound_max, sound_mean, avg_wellbeing])
f.close()

print("I have added the following data to the data file BR1-3_results.csv")
print([sound_min, sound_max, sound_mean, avg_wellbeing])
print("")
f.close()
