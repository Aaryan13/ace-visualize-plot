import pandas as pd

#We use encoding here because pandas has some problems with encoding datasets other than UTF-8, using Encoding solve the error
df=pd.read_csv("/home/aaryan/Documents/DataSets/MinWageData.csv", encoding="latin")


#We can use pandas to convert the encoding of our Data File to UTF-8
df.to_csv("/home/aaryan/Documents/DataSets/Minwage.csv", encoding="UTF-8")
df=pd.read_csv("/home/aaryan/Documents/DataSets/Minwage.csv")
# print(df)


#Grouping State Column in Our DataSets
grp=df.groupby("State")
# print(grp.get_group("Alabama").set_index("Year").head(5))


#Now we'll iterate over our group one by one
act_min_wage=pd.DataFrame()
for name,group in df.groupby("State"):
    if act_min_wage.empty:
        act_min_wage=group.set_index("Year")[["Department.Of.Labor.Cleaned.Low.Value.2020.Dollars"]].rename(columns={"Department.Of.Labor.Cleaned.Low.Value.2020.Dollars":name})
    else:
        act_min_wage=act_min_wage.join(group.set_index("Year")[["Department.Of.Labor.Cleaned.Low.Value.2020.Dollars"]].rename(columns={"Department.Of.Labor.Cleaned.Low.Value.2020.Dollars":name}))
# print(act_min_wage.head())


#Describing the over all infos in each columns
# print(act_min_wage.describe())


#Correlating our state columnn to our state row 
# print(act_min_wage.corr().head())


#Printing out all the states which has "..." as input under Table_Data Column
issue_df=df[df["Department.Of.Labor.Cleaned.Low.Value.2020.Dollars"]==0]
# print(issue_df.head())


#Checking out all the states which has "..." as input under Table_Data Column
# print(issue_df["State"].unique())


#Now we need Numpy coz we'll add NaN data Type wherever the entry is missing from the Dataset
import numpy as np
#dropna(axis=1) will get rid of columns with NaN values
#dropna(axis=0) will get rid of rows with NaN values
act_min_wage.replace(0, np.NaN).dropna(axis=1).corr()
# print(act_min_wage.head())


#
min_wage_corr=act_min_wage.replace(0, np.NaN).dropna(axis=1).corr()
for problem in issue_df["State"].unique():
    if problem in min_wage_corr.columns:
        print("Missing Something")
grouped_issues=issue_df.groupby("State")
# print(grouped_issues.get_group("Alabama").head())


print(grouped_issues.get_group("Alabama")["Department.Of.Labor.Cleaned.Low.Value.2020.Dollars"].sum())


for state,data in grouped_issues:
    if data["Department.Of.Labor.Cleaned.Low.Value.2020.Dollars"].sum() != 0:
        print("We Missed Something")