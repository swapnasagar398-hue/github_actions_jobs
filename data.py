import pandas as pd

data={
    "name":["A","B","C"],
    "age":[20,30,24],
    "address":['pune','goa','hyd']
}


df=pd.DataFrame(data)
print(df)