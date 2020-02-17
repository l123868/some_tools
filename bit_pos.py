import os

data = input("本程式將協助你快速找出1所在的位置，請以0、1的形式輸入或複製stream，按下enter...>")

for i in range(len(data)):
    if data[i] ==  '1':
        print(i+1)

os.system("pause")
