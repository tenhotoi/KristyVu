# https://www.geeksforgeeks.org/how-to-make-a-table-in-python/
# pip install tabulate

# import module
from tabulate import tabulate
 
# assign data
mydata = [
    ["Nikhil", "Delhi"],
    ["Ravi", "Kanpur"],
    ["Manish", "Ahmedabad"],
    ["Prince", "Bangalore"]
]
 
# create header
head = ["Name", "City"]
 
# display table
print(tabulate(mydata, headers=head, tablefmt="grid"))