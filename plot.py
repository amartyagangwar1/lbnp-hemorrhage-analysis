import pandas as pd
import matplotlib.pyplot as plt

#Updated 8/8/25 @ 6:47

df = None
options = []

def select(filepath=None):
    global df, options

    if filepath is None:
        inp = ""
        while True:
            inp = input("What LBNP Standard CSV would you like to plot: ")
            try:
                df = pd.read_csv(fr"{inp}")
                break
            except FileNotFoundError:
                print("Invalid File Selected. Please try again!")         
        print("Sucess! \n")
    else:
        df = pd.read_csv(filepath)
    choices()

def choices():
    global options, df
    options = df.columns.drop(['Time','Labchart_LBNP', 'Time (s)']).tolist()
    print("Your available plot options are: ")
    i = 0
    for col in options:
        print(f"{i}: {col}")
        i += 1


def plot(selected_Index = None):
    global df, options

    if selected_Index is None:
        inp = ""
        while True:
            inp = input("What index would you like to plot: ")
            try:
                indx = int(inp)
                if indx >= 0 and indx <= (len(options) -1):
                    inp = options[indx]
                    break
                else:
                    raise ValueError
            except:
                print("Invalid Input. Please try again using a valid index number!")   
    else:
        inp = options[selected_Index]


    #fill in missing values
    df.ffill(inplace=True)  #carry last know value forward
    df.bfill(inplace=True)  #carry next known value backward for any remaining missing values

    #create figure and axis to plot left y axis
    fig, ax1 = plt.subplots()
    ax1.plot(df['Time (s)'], df[inp], color='blue')      
    ax1.set_xlabel('Time (s)')
    ax1.set_ylabel(inp, color='blue')                                

    #create second y axis to plot LBNP
    ax2 = ax1.twinx()
    ax2.plot(df['Time (s)'], df['Labchart_LBNP'], color='red')
    ax2.set_ylabel('LBNP Pressure', color='red')

    #set title / grid / cleanup
    plt.title(f"{inp} & LBNP Pressure Over Time")                         
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)
    fig.tight_layout()

    #print plot
    plt.show()
    