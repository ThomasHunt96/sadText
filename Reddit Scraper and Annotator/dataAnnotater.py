import pandas as pd
import csv
import re
import sys
#emotion category


def exit(index,df,emotionlist):
    newdf = df.loc[:index-1]
    print(newdf)
    print(len(emotionlist))
    newdf["emotion"] = emotionlist
    newdf.to_csv(input("please enter a filename"))

    return emotion_list


read_data = []

print("input file path...")
path = input()
df = pd.read_csv(path)

annotation_list = ['suffering', 'sadness', 'disappointment',
               'shame', 'neglect', 'sympathy', 'unclassifiable']
emotion_list = []
validinputs = ['0','1','2','3','4','5','6','exit']

for index, row in df.iterrows():
    print(df.at[index, "text"])
    
    inputstr = input("Input 0. suffering, 1. Sadness, 2. Dissappointment, 3. Shame, 4. Neglect, 5. Sympathy, 6. Unclassifiable")
    
    if inputstr == "exit":
            print("Processed ", index, "rows")
            exit(index,df,emotion_list)
            sys.exit()

    while inputstr not in validinputs:
        
        print("Error only 0-6 is allowed")
        inputstr = input("Input 0. suffering, 1. Sadness, 2. Dissappointment, 3. Shame, 4. Neglect, 5. Sympathy, 6. Unclassifiable")
    try:
        emotion_list.append(annotation_list[int(inputstr)])
    except:
        print('done')
    
df["emotion"] = emotion_list
df.to_csv(input("please enter a filename"))

