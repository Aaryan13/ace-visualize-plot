from os import stat
import pandas as pd
import numpy as np
df=pd.read_csv("/home/aaryan/Documents/DataSets/MinWageData.csv",encoding="UTF-8")
df=pd.read_csv("/home/aaryan/Documents/DataSets/MinWageData.csv")
act_min_wage=pd.DataFrame()
for name,group in df.groupby("State"):
    if act_min_wage.empty:
        act_min_wage=group.set_index("Year")[["Department.Of.Labor.Cleaned.Low.Value.2020.Dollars"]].rename(columns={"Department.Of.Labor.Cleaned.Low.Value.2020.Dollars":name})
    else:
        act_min_wage=act_min_wage.join(group.set_index("Year")[["Department.Of.Labor.Cleaned.Low.Value.2020.Dollars"]].rename(columns={"Department.Of.Labor.Cleaned.Low.Value.2020.Dollars":name}))
min_wage_corr=act_min_wage.replace(0, np.NaN).dropna(axis=1).corr()
# print(min_wage_corr.head())        

import matplotlib.pyplot as plt
# plt.matshow(min_wage_corr)

#The plot/graph shown by this method is absolute garbage, so we need to improve that
labels=[c[:2] for c in min_wage_corr.columns]
#Sizing our plot
fig=plt.figure(figsize=(12,12))
# plt.matshow(min_wage_corr)


#  If you want to modify our graph, you can't modify plt(matplotlib) you have to modify an axis, and to have an axis
# You need to have a subplot and for a subplot you need a figure so ya its a long path     

# Now we wanna have our axes from our figure
ax=fig.add_subplot(111)
# (111) all the subplots in our figure are in a 1X1 grid and this is number one(1)
# Simply put this just means there is going to be one graph we are doing modification on
# ax.matshow(min_wage_corr, cmap=plt.cm.RdYlGn); #cmap is color of the map 

# Now we'll do some changes to our axes
# ax.set_yticklabels(labels)
# ax.set_xticklabels(labels)
# ax.matshow(min_wage_corr, cmap=plt.cm.RdYlGn);  

# Hey Matplotlib show all of the labels passed inside (labels) function in ax.set_xticklabels(labels)
# ax.set_xticks( np.arange(len(labels)))
# ax.set_yticks( np.arange(len(labels))) 

# ax.set_yticklabels(labels)
# ax.set_xticklabels(labels)

# plt.show()


# STORY TIME
# In our above dataset there amny labels and data entries which sometimes might get confusing as to what dataset belongs
# To which column, In that case we need to take help from some websites to figure out this problem
# And sometimes like in our dataset case Many Country Code(lables) are same for Different countries, this shouldn't be the case
# So we'll take the help from a website which provides such dataset for free
# NOTE: Some websites don't allow bots to use their dataset, so use websites accordingly which allows pandas library to work


# So let's take the help from a website by reading its datasets
# dfs=pd.read_html("https://www.infoplease.com/us/postal-information/state-abbreviations-and-state-postal-codes")
# We wont use the above code for our purpose reason down below
# Upon running this code we would get a big error sat=ying SSL Certificste Failed and to overcome that error we use

import requests
web=requests.get("https://www.infoplease.com/us/postal-information/state-abbreviations-and-state-postal-codes")
dfs=pd.read_html(web.text)

# Pandas Html will parse that website and return a list of dataframes based on all fo the tables it finds 
# If it finds a table it's still a list and Pandas Html module will get the datasets from that table in the form of list.


state_abbv=dfs[0]


# Now we'll save our state_abbv dataset in a csv file
state_abbv.to_csv("/home/aaryan/Documents/DataSets/State_abbv.csv")


state_abbv=pd.read_csv("/home/aaryan/Documents/DataSets/State_abbv.csv")
# print(state_abbv.head())
# Pandas believe that your index is meaningful so when you save something but 'csv' doesn't understand index 
# Now when we try to read our file suddenly it will have two of the columns as Index this is by default added by Pandas
# To our 'csv' file, so more index columns will get added as you d=save this file on and on again, which will make
# Our dataset troublesome to work with, so to solve that error we have couple of methods to do so
state_abbv.to_csv("/home/aaryan/Documents/DataSets/State_abv.csv",index=False)
state_abbv=pd.read_csv("/home/aaryan/Documents/DataSets/State_abbv.csv",index_col=0)
# print(state_abbv.head())    

#Converting above dataset to a meaningful dictionary
abbv_dict=state_abbv[["Postal Code"]].to_dict()
# print(abbv_dict)

abbv_dict=state_abbv[["Postal Code"]].to_dict()
abbv_dict=abbv_dict["Postal Code"]


# labels=[abbv_dict[c] for c in min_wage_corr.columns]
abbv_dict["Alaska"]="Alaska"
abbv_dict["Arkansas"]="Arkansas"
abbv_dict["California"]="California"
abbv_dict["Colorado"]="Colorado"
abbv_dict["Connecticut"]="Connecticut"
abbv_dict["Delaware"]="Delaware"
abbv_dict["District of Columbia"]="District of Columbia"
abbv_dict["Guam"]="Guam"
abbv_dict["Hawaii"]="Hawaii"
abbv_dict["Idaho"]="Idaho"
abbv_dict["Indiana"]="Indiana"
abbv_dict["Kentucky"]="Kentucky"
abbv_dict["Maine"]="Maine"
abbv_dict["Maryland"]="Maryland"
labels=[abbv_dict[c] for c in min_wage_corr.columns]
