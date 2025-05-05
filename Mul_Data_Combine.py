from itertools import count
import pandas as pd
import numpy as np
unemp_county=pd.read_csv("/home/aaryan/Documents/DataSets/Unem_county_US.csv")
# print(unemp_county.head())
df=pd.read_csv("/home/aaryan/Documents/DataSets/MinWageData.csv", encoding="UTF-8")
act_min_wage=pd.DataFrame()
for name,group in df.groupby("State"):
    if act_min_wage.empty:
        act_min_wage=group.set_index("Year")[["Department.Of.Labor.Cleaned.Low.Value.2020.Dollars"]].rename(columns={"Department.Of.Labor.Cleaned.Low.Value.2020.Dollars":name})
    else:
        act_min_wage=act_min_wage.join(group.set_index("Year")[["Department.Of.Labor.Cleaned.Low.Value.2020.Dollars"]].rename(columns={"Department.Of.Labor.Cleaned.Low.Value.2020.Dollars":name}))
# print(act_min_wage.head())
act_min_wage=act_min_wage.replace(0,np.NaN).dropna(axis=1)
# print(act_min_wage.head())

#Now we wanna take the minimum wage(act_min_wage) and we wanna add that to a new column in our unemployment county dataset(unemp_county)
#The way we can do that is by creating a new in unemp_county dataset and then mapping the values to the column in unemp_county

#And there are multiple ways of doing this, so first of we will take a look at Number one example
#We'll create a function to do this
def get_min_wage(year,state):
    try:
        #We are tyring to get minimum wage by year and state 
        #We would capture the year and state as a reference to the specific column
        return act_min_wage.loc[year][state]
    except:
        return np.NaN
# print(get_min_wage(2015,"Colorado"))

#Now we have min_wage, we will map this to our dataset by creating a new column
#We can a function to a list or an array using map
#NOTE: This is an inefficient way of doing this, but this will always work

# Here we go.....
#Take our dataset with the new column to be added and '=' to map(column_name,parameters)
#In this case map function will have (get_min_wage,unemp_county['Year'],unemp_county['State']) as parameters
#NOTE: We have to convert this into a list before mapping coz python3 works like this
#Also this takes an eternity to complete, glad I am on Ubuntu.
# unemp_county['min_wage']=list(map(get_min_wage,unemp_county["Year"],unemp_county["State"]))


#Now time to load our another dataset as we want to combine tow datasets together
pres16=pd.read_csv("/home/aaryan/Documents/DataSets/US_Prez_Elec.csv")
# print(pres16.head())
#This gives us the output of how many people for whom in US Elections for Prez with their representative state
#For now we'll focus on Donald Trump, so our focus would be how many people voted in that county for Donald Trump 
#And what is the Minimum Wage and Unemployment rate for that county 
# we would also like to check correlation and covariance relation between Unemployment and Minimum Wage rate in that county
#In their relationship with people voting for Trump


#Let's find out size of our unemp_county dataframe
# print(len(unemp_county))

# Now we want to filter unemp_county dataframe down to just 2015 February, so we'll name this as county_2015
# Syntax: variable_name = dataframe to filter[() & ()] with conditions inside these round brackets, here we go....
county_2015 = unemp_county.copy()[(unemp_county['Year'] == 2015) & (unemp_county['Month'] == 'February')]

# Just checking out how many states are there in our pres16 dataset
# print(pres16['st'].unique())

# Now we need to convert our full State Name into a Postal code, for our easiness
# For doing that we already have a dataset file which has all the postal codes
# We just need to use it and combine it with our pres16 dataset
# state_abbv variable name used coz its just abbreviation for State Postal Codes
state_abbv=pd.read_csv("/home/aaryan/Documents/DataSets/State_abbv.csv",index_col=0)
# print(state_abbv.head())

# Now we just want the state abbreviation of postal codes, so no need to have extra useless columns in our datframe
# For printing just the columns we need from our dataframe, below is the syntax to do it
state_abbv=state_abbv[["Postal Code"]]

# Now we have to convert this into a dictionary to merge it with our other datasets
# So we are gonna create a dictionary name state_abbv_dict which will have the dataframe in the dictionary format
# We dont need the index column, hence we mention in square brackets which column we want from our dataframe obv with ''

state_abbv_dict=state_abbv.to_dict()['Postal Code']
# print(state_abbv_dict)

# Now we got the Dictionary to map to our county_2015 dataset
# Just mapping the values to that column which we got(state_abbv_dict) to county_2015
# The syntax to do that is below
county_2015['State']=county_2015['State'].map(state_abbv_dict)

# Now we want to merge county_2015 to pres16 dataset, and we will merge them together on the basis of State and County
# First we will just rename the columns in our pres16 dataset, the sytx to do this is below
pres16.rename(columns={"county":"County","st":"State"},inplace=True)

# Now we'll set two indexes as we want to compare and correlate our dataset on the basis of State and County
for df in[county_2015,pres16]:
    df.set_index(["County","State"],inplace=True)


pres16=pres16[pres16['cand']=="Donald Trump"]
pres16=pres16[["pct"]]
pres16.dropna(inplace=True)
# print(pres16.head())


all_together=county_2015.merge(pres16,right_index = True,left_index = True)
all_together.dropna(inplace=True)
print(all_together.head())
# print(all_together.cov())
