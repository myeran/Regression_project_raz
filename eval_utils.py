
import numpy as np

def my_stupid_evaluation_function_01(y_test, y_pred):
    strikes = 0
    for i in range(len(y_test)):
       differnce = abs(y_test[i]-y_pred[i])/y_test[i]
       if differnce > 0.1:
            strikes +=1
    return strikes/len(y_test) 

def my_stupid_evaluation_function(y_test,y_pred):
    out = np.abs(y_test-y_pred)/ y_test
    return (out>0.1).mean()