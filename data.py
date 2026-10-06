import pandas as pd
import requests 


data={
    "name":["A","B","C"],
    "age":[20,30,24],
    "address":['pune','goa','hyd']
}


df=pd.DataFrame(data)
print(df)

response=requests.get("https://jsonplaceholder.typicode.com/users")
user_data=response.json()
print(user_data)