import pandas as pd

product = ['p1', 'p2', 'p3']
firmware = ['fw1', 'fw2', 'fw3']
version = ['1', '2', '3', '4']

df = pd.DataFrame(
[[4, 7, 10],
[5, 8, 11],
[6, 9, 12]], 
index=product, 
columns=firmware)

print(df)