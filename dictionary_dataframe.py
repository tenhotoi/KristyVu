# Python Pandas - Convert Nested Dictionary to Multiindex Dataframe
# https://www.tutorialspoint.com/python-pandas-convert-nested-dictionary-to-multiindex-dataframe

import pandas as pd

# Create Nested dictionary
dictNested = {'Cricket': {'Boards': ['BCCI', 'CA', 'ECB'],'Country': ['India', 'Australia', 'England']},'Football': {'Boards': ['TFA', 'TCSA', 'GFA'],'Country': ['England', 'Canada', 'Germany']
   }}

print("\nNested Dictionary...\n",dictNested)

new_dict = {}
for outerKey, innerDict in dictNested.items():
   for innerKey, values in innerDict.items():
      new_dict[(outerKey, innerKey)] = values

# converting to multiindex dataframe
print("\nMulti-index DataFrame...\n",pd.DataFrame(new_dict))

# Converting Dictionary into a dataframe:

emp_details = {'Employee': {'Dave': {'ID': '001',
                                    'Salary': 2000,
                                    'Designation':'Python Developer'},
                           'Ava': {'ID':'002',
                                    'Salary': 2300,
                                    'Designation': 'Java Developer'},
                           'Joe': {'ID': '003',
                                    'Salary': 1843,
                                    'Designation': 'Hadoop Developer'}}}
df=pd.DataFrame(emp_details['Employee'])
print(df)

XYZ_web= {'Day':[1,2,3,4,5,6], "Visitors":[1000, 700,6000,1000,400,350], "Bounce_Rate":[20,20, 23,15,10,34]}   
df= pd.DataFrame(XYZ_web)
print(df)

"""
Output:
                        Dave             Ava               Joe
ID                        001             002               003
Salary                   2000            2300              1843
Designation  Python Developer  Java Developer  Hadoop Developer

   Day  Visitors  Bounce_Rate
0    1      1000           20
1    2       700           20
2    3      6000           23
3    4      1000           15
4    5       400           10
5    6       350           34
"""
print(zip(XYZ_web['Day'], XYZ_web['Visitors'], XYZ_web['Bounce_Rate']))
"""
<zip object at 0x0000024213FDCA40>
"""
try:
   print(dict(zip(XYZ_web['Day'], XYZ_web['Visitors'], XYZ_web['Bounce_Rate'])))
except ValueError as err:
   print(err)
"""
    print(dict(zip(XYZ_web['Day'], XYZ_web['Visitors'], XYZ_web['Bounce_Rate'])))
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ValueError: dictionary update sequence element #0 has length 3; 2 is required
"""
a = XYZ_web['Day']
b = XYZ_web['Visitors']
c = XYZ_web['Bounce_Rate']
print(days := {f'Day {day}': {'Visitors': visitor, 'Bounce_Rate': rate} for day, visitor, rate in zip(a, b, c)})
"""
{1: {'Visitors': 1000, 'Bounce_Rate': 20}, 2: {'Visitors': 700, 'Bounce_Rate': 20}, 3: {'Visitors': 6000, 'Bounce_Rate': 23}, 4: {'Visitors': 1000, 'Bounce_Rate': 15}, 5: {'Visitors': 400, 'Bounce_Rate': 10}, 6: {'Visitors': 350, 'Bounce_Rate': 34}}
"""
print(f'\n {days.items()}')
"""
 dict_items([(1, {'Visitors': 1000, 'Bounce_Rate': 20}), (2, {'Visitors': 700, 'Bounce_Rate': 20}), (3, {'Visitors': 6000, 'Bounce_Rate': 23}), (4, {'Visitors': 1000, 'Bounce_Rate': 15}), (5, {'Visitors': 400, 'Bounce_Rate': 10}), (6, {'Visitors': 350, 'Bounce_Rate': 34})])
"""
# print(days[1])

for k, v in days.items():
   print('Day {} had {}\n'.format(k, v))

from string import Template

template = Template('Day $day had $contents')
for k, v in days.items():
   print(template.substitute(day = k, contents = v))

for k, v in days.items():
   print(f'Day {k} had {v}')

for k, v in days.items():
   print('Day %s had %s ' % (k, str(v)))

print(statistic := {"Department 1" : days})
print(testingDataframe := pd.DataFrame(statistic))

dict_net = {}
for outerkeys, innerdicts in XYZ_web:
   for k, v in innerDict:
      dict_net[(outerkeys, k)] = v
print(dict_net)

