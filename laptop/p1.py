# import lib
import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import pickle

# load the data
data = pd.read_csv("laptop_price.1.csv"  ,encoding='latin-1')
print(data)

data.drop(["laptop_ID" , "Product" , "ScreenResolution" , "Cpu" , "Gpu"   ], axis="columns" , inplace=True)
print(data.head())

# understand the data
res = data.isnull().sum()
print(res)

# features 
features = data.drop(  "Price_euros" , axis = "columns")
target = data["Price_euros"]

nfeatures = pd.get_dummies(features)
print(nfeatures)

x_train , x_test , y_train , y_test = train_test_split(nfeatures , target , random_state =1545)

model = RandomForestRegressor(n_estimators=10)
model.fit(x_train , y_train)

s1 = model.score(x_train , y_train)
s2 = model.score(x_test , y_test)
print(s1 , s2)

# save the model
f = None
try :
	f = open("re.model" , "wb")
	pickle.dump(model , f)
except Exception as e :
	print("issue" , e)
finally :
	if f is not None :
		f.close()












