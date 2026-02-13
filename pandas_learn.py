
import pandas as pd
# data_frame=pd.DataFrame({
#     "name":["name1","name2"],
#     "age":[21,20],
#     "degree":["cse","Electronics"]
# })

# data = {
#     'Name': ['Alice', 'Bob', 'Charlie'],
#     'Age': [25, 30, 35],
#     'Country': ['USA', 'Canada', 'UK']
# }

# df = pd.DataFrame(data)
# print(df)

#metadata 
# print(df.info)
# print(df.columns)
# print(df.index)
# print(df.describe())

df:pd.DataFrame=pd.read_csv("orders.csv")
# print(type(df))
print(df.head())
print(df.tail())

print(type(df.iloc[0]))
print(df.iloc[39]["OrderID"])

new_df=df[(df["Product"]=="Laptop") | (df["Country"]=="USA")]
print(new_df[new_df["Quantity"]>10])

print(df[df["CustomerName"].str.endswith("g")])
print(df[df["Country"].isin(["USA","UAE"])])

# updation
df.loc[df["CustomerName"]=="Ali Khan","Product"]="Chair"
print(df[["CustomerName","Product"]])
df["Country"]=df["Country"].str.upper()

df.drop(39)
df.dropna(inplace=True)
df.fillna({"OrderID":0},inplace=True)
df.rename({"OrderID":"Order Id"},inplace=True)
print(df.groupby("Country")["Price"].sum())