import pandas as pd

inp_path = "retail_store_sales.csv"
out_path = "cleaned_store_sales.csv"

df = pd.read_csv(inp_path)
print("-------------Initial Data---------------")
df.info()

#dropping rows with empty Items
df.dropna(subset=["Item"],inplace = True)
df.info()


#Filling false in discount applied where values are null
df['Discount Applied'].fillna(False,inplace=True)

#Converting Trans Date from int to date format
df['Transaction Date'] = pd.to_datetime(df['Transaction Date'],origin='1899-12-30',unit='D')

df.to_csv(out_path,index = False)
print(df.isnull().sum().sum())