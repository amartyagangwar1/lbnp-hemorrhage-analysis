import pandas as pd
import matplotlib.pyplot as plt

'''
create function to select what data chart to use, should return the possbile values to plot
create function to plot one thing vs another, with optional smoothing
'''
df = None

def select():
    inp = ""
    while True:
        inp = input("What LBNP Standard CSV would you like to plot: ")
        try:
            df = pd.read_csv(fr"{inp}")
            break
        except FileNotFoundError:
            print("Invalid File Selected. Please try again!")         
    print("Sucess!")

    options = df.columns.drop(['Time','Labchart_LBNP', 'Time (s)'])
    print("Your available plot options are: ")
    for col in options:
        print(f"- {col}")




#df = pd.read_csv(r"data\GoldStandards_H24013_03.csv") #create data frame by reading csv
'''
#fill in missing values
df.ffill(inplace=True)  #carry last know value forward
df.bfill(inplace=True)  #carry next known value backward for any remaining missing values

print(df.columns)

#create figure and axis to plot left y axis
fig, ax1 = plt.subplots()
#df['Labchart_SV'] = df['Labchart_SV'].rolling(window=10).mean()
ax1.plot(df['Time (s)'], df['Labchart_SV'], color='blue')      #REPLACE TO PLOT SOMETHING ELSE
ax1.set_xlabel('Time (s)')
ax1.set_ylabel('PLACEHOLDER', color='blue')                                #CHANGE LABEL

#create second y axis to plot LBNP
ax2 = ax1.twinx()
ax2.plot(df['Time (s)'], df['Labchart_LBNP'], color='red')
ax2.set_ylabel('LBNP Pressure', color='red')

#set title / grid / cleanup
plt.title('PLACEHOLDER & LBNP Pressure Over Time')                         #CHANGE LABEL
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
fig.tight_layout()

#print plot
plt.show()
'''