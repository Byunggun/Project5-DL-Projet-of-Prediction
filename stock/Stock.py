import tensorflow as tf
import numpy as np
import pandas as pd

#데이터 불러오기
all_data=pd.read_csv('D:\Python\MyGitHub\Project5-DL-Projet-of-Prediction\stock/SSUN.F.csv', skiprows=1)
data_arrayed=np.array(all_data)
print(data_arrayed)

#전처리
# xdata=xy[:,1:-3]
# ydata=xy[:,-3:]