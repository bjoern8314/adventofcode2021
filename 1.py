import numpy as np
import pandas as pd 
doc = pd.read_csv("numbers_task1.csv")
for x in np.array(doc):
    try:
        if prev < x:
            prev = x
            print("increased")
        else:
            print("decreased")
            prev = x
    except:
        print("(N/A - no previous measurement)")
        prev = x

