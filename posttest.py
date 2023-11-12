import pandas as pd

# membaca file
data = pd.read_csv('harga_rumah.csv') 
print (data.head()) 

#membaca file harga_rumah hanya kolom "harga"
print("Untuk kolom harga saja")
df = pd.DataFrame(data)
print(df.harga)
print(df['harga'])

#membaca fili harga_rumah tanpa kolom harga
X = df.drop(['harga'],axis=1)
print(X.head())