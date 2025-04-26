import pandas as pd
df = pd.read_json("C:\\Users\\MehakSeetlani\\Downloads\\usedCars.json")

#Data frame information
Cars_Data = df.info()

#Drop Null Values 
Null_Values = df.isnull().sum()
print(Null_Values)

#Drop Duplicates
Cars_Data_Duplicate = df.drop_duplicates(inplace = True)

#Date Format 
df['adLastUpdated'] = pd.to_datetime(df['adLastUpdated'], format='mixed')
print(df.to_string())

#Extracting Columns from Dictionary
df['brand_name'] = df['brand'].apply(lambda x: x.get('name') if pd.notnull(x) else None)

#Visualization
import matplotlib.pyplot as plt

top10 = df.sort_values(by='price', ascending=False).head(10)
plt.bar(top10['model'], top10['price'])
plt.title('Car Model Price')
plt.xlabel('Model')
plt.ylabel('Price (PKR)')
plt.xticks(rotation = 90)
plt.show()
