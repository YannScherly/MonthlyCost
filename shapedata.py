import pandas as pd
car_df=pd.read_csv('CarPrice.csv')
car_df.head()
car_df.shape
car_df.duplicated().sum()
car_df.drop_duplicates(inplace= True)
car_df['Brand Name']=car_df['CarName'].str.split(' ').str.slice(0,1).str.join('')
car_df['Model']=car_df['CarName'].str.split('').str.slice(2,3).str.join('')
car_df['Model name']=car_df['CarName'].str.split(' ').str.slice(2,3).str.join('')
car_df.rename(columns={'carname':'Model name'},inplace=True)
car_df.drop('Model name',axis=1,inplace=True)
car_df=car_df.iloc[:,[26,2,25,3,5,21,24]]

