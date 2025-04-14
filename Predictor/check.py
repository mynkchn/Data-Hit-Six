import joblib
import numpy as np
import pandas as pd
import math

model=joblib.load('D:\\Cricket Data Analysis\\Model\\model.pkl')
input=pd.DataFrame([[3,2]],columns=['4s','6s'])
prediction=model.predict(input)
print(f'If a batsman hit a 3 fours and 2 sixes average he would achieve is {math.floor(prediction[0])}')