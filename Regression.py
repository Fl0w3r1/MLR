import numpy as np
import matplotlib as mpl
import pandas as pd

dataset = pd.read_csv("regression.csv")
X = dataset.iloc[:,:-1]
y = dataset.iloc[:,4]

eisodima = pd.get_dummies(X["eisodima"],drop_first=True)

X = X.drop("eisodima",axis=1)

X = pd.concat([X,eisodima],axis=1)

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

y_pred = regressor.predict(X_test)

from sklearn.metrics import r2_score
score = r2_score(y_test,y_pred)