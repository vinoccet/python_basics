
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

df=pd.read_csv("orders.csv")
print(df.head())
