#<얼거리>
#파일 불러오기
#전처리
#+decoding-문자
# #train&test data 구분
###<그래프정의>
#+x,y,w,b
#+cost
#+optimizer-adam
#+hf : Relu->Sigmoid (다중 신경망)
#+Learning-Rate
#+epoch
#Queue Runners
###<그래프실행>
#BackPropagation
#Drop-Out
#정확도

#시각화
#+시간에 따른 점-animation(cf.https://www.kaggle.com/ash316/terrorism-around-the-world)

########################################################################################################################
import tensorflow as tf
import numpy as np
import pandas as pd

#to upload the data of refugees
data=pd.read_csv('D:\Python\MyGitHub\Project5-DL-Projet-of-Prediction\\refugee-data/time_series.csv')
data_arrayed=np.array(data)
print(data_arrayed)

#전처리
