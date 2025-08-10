import pandas as pd
import numpy as np
from plot import file 
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV

fil = None

def hemIndx():
    global fil
    fil = file().copy()

    pressure = fil["Labchart_LBNP"]
    peakPressure = pressure.max()
    hemorrhage_index = pressure / peakPressure

    fil["hemorrhage_index"] = hemorrhage_index
    fil["hemorrhage_index"] = fil["hemorrhage_index"].clip(lower=0, upper=1)

def model():
    #calculate hemmoragin index using HR / CO / SV / SVR 
    global fil
    features = ["Labchart_HR", "Labchart_CO", "Labchart_SV", "Labchart_SVR"]
    x = fil[features]
    #print(f"x: {x.shape}")
    y = fil["hemorrhage_index"]
    
    x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2, random_state=101)

    #build random forest with hyper paramters
    n_estimators = [int(x) for x in np.linspace(10,80,10)] #number of trees to test
    max_features = ['sqrt', 'log2']                        #use log2 of all features / use sqrt of total features 
    max_depth = [2,4]                                      #max number of levels in tree
    min_samples_split = [2,5]                              #min number of samples required to split a node
    min_samples_leaf = [1,2]                               #min number of samples per leaf node
    bootstrap = [True, False]

    param_grid = {'n_estimators': n_estimators,
               'max_features': max_features,
               'max_depth': max_depth,
               'min_samples_split': min_samples_split,
               'min_samples_leaf': min_samples_leaf,
               'bootstrap': bootstrap}
    
    rfModel = RandomForestClassifier(random_state=101)
    rfGrid = GridSearchCV(estimator = rfModel, param_grid=param_grid, cv = 3, verbose = 0, n_jobs = 4)  #test every combo

    rfGrid.fit(x_train,y_train)

    print (f"Train Accuracy: {rfGrid.score(x_train,y_train):.3f}")
    print (f"Test Accuracy: {rfGrid.score(x_test,y_test):.3f}")