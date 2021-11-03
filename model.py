from sklearn.linear_model import SGDRegressor
from sklearn.datasets import load_boston
from sklearn.datasets import make_regression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.preprocessing import scale
import matplotlib.pyplot as plt

import csv
import random
import math
recent_price=[403.15,388.14,386.76,382.41,386.42,396.29,353.53]
recent_tik_tok=[407,234,208,517,868,221,223,]
x=[]
y=[]
with open('ETH-CNY.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            #print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            #print(f'date = {row[0]} High = {row[2]} Low = {row[3]} Volume = {row[6]}.')
            date=row[0]
            volume=row[6]
            tik_tok=row[7]
            price=random.randrange(math.ceil(float(row[3])),math.floor(float(row[2])))
            #dynamic
            #x.append([float(tik_tok),float(volume),recent_price[0],recent_price[1],recent_price[2],recent_price[3],recent_price[4],recent_price[5],recent_price[6]])
            #tik-tok
            #x.append([float(tik_tok),float(volume),recent_tik_tok[0],recent_tik_tok[1],recent_tik_tok[2],recent_tik_tok[3],recent_tik_tok[4],recent_tik_tok[5],recent_tik_tok[6]])
            #combined
            x.append([float(tik_tok),float(volume),recent_price[0],recent_price[1],recent_price[2],recent_price[3],recent_price[4],recent_price[5],recent_price[6],recent_tik_tok[0],recent_tik_tok[1],recent_tik_tok[2],recent_tik_tok[3],recent_tik_tok[4],recent_tik_tok[5],recent_tik_tok[6]])
            y.append(float(price))
            recent_price.pop()
            recent_price.append(price)
            recent_tik_tok.pop()
            recent_tik_tok.append(tik_tok)
            line_count += 1
    #print(f'Processed {line_count} lines.')

#print (x)
#print (y)

# x is the feature [[feature a, feature b, feature c],[],[]...]
# y is the real value

#    First, we'll generate random regression data with make_regression() function. The dataset contains 30 features and 1000 samples.
# x, y = make_regression(n_samples=100, n_features=3)
# print(x)
# print(y)

# Replace with my own data if possible
# First read different feature you find in feature folder

# Then read the price

# To improve the model accuracy we'll scale both x and y data then, split them into train and test parts. Here, we'll extract 15 percent of the samples as test data.
x = scale(x)
y = scale(y)
xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size=.15)

#    Next, we'll define the regressor model by using the SGDRegressor class. Here, we can use default parameters of the SGDRegressor class.
sgdr = SGDRegressor()
print(sgdr)

sgdr.fit(xtrain, ytrain)

score = sgdr.score(xtrain, ytrain)
print("R-squared:", score)

cv_score = cross_val_score(sgdr, x, y, cv=10)
print("CV mean score: ", cv_score.mean())

ypred = sgdr.predict(xtest)
print(ypred)

mse = mean_squared_error(ytest, ypred)
print("MSE: ", mse)
print("RMSE: ", mse**(1/2.0))

x_ax = range(len(ytest))
plt.plot(x_ax, ytest, linewidth=1, label="original")
plt.plot(x_ax, ypred, linewidth=1.1, label="predicted")
plt.title("y-test and y-predicted data")
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend(loc='best',fancybox=True, shadow=True)
plt.grid(True)
plt.show()