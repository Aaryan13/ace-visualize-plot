# import pandas as pd
# df=pd.read_csv("/home/aaryan/Documents/avocado.csv")
# albany_df=df[df["region"]=="Albany"]
# albany_df.set_index("Date")

#25 MA Line Chart Application
# albany_25MA=albany_df["AveragePrice"].rolling(25).mean().plot()

#Sorting our date index 
# albany_df.sort_index(inplace=True)

#We'll create a separate column just for 25MA Moving Price
# albany_df["25MA_Price"]=albany_df["AveragePrice"].rolling(25).mean()
# print(albany_df.head())

#Now we'll remove the NaN valued from our 25MA column as first few columns won't be having value of 25MA
# print(albany_df.dropna().head()) 

#Printing out our values as a set datatype
# print(list(set(df['region'].values.tolist())))

#Printing out all the unique values and not the repetitive one
# print(df['region'].unique())

#Finally plotting out graph properly this time
# graph_df=pd.DataFrame()
# for region in df['region'].unique():
#     print(region)


#     if graph_df.empty:
#         graph_df=region_df[[f'{region}price25ma']] #Double Square Brackets coz we want this to be Dataframe and not a series
#     else:
    #join() function is used to join 2 different databases based on their index
    #NOTE: The Index reference should be same from the dataframe to copy and the dataframe that gets copied
        # graph_df=graph_df.join(region_df[f'{region}price25ma'])
    #f'{region}price25ma' we use this statement as the type column has 2 separate datasets and we want to print out only 1 column
    #This 2 different columnns from type dataset causes the RAM to explode, so we'll specify which type we want 
import pandas as pd
df=pd.read_csv("/home/aaryan/Documents/avocado.csv")
df=df.copy()[df['type']=='organic']
df['Date']=pd.to_datetime(df['Date'])
df.sort_values(by="Date",ascending=True,inplace=True)
graph_df=pd.DataFrame()
# for region in df['region'].unique():
#     print(region)


#     if graph_df.empty:
#         graph_df=region_df[[f'{region}price25ma']] #Double Square Brackets coz we want this to be Dataframe and not a series
#     else:
#         graph_df=graph_df.join(region_df[f'{region}price25ma'])
graph_df.plot()

