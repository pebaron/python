# %%
import numpy as np

# %%
"""
# Python lists
"""

# %%
"""
## Common use case
"""

# %%
l = [1,2,3,4]

# %%
# most common use case:

l = []
n = 100
for a in range(1, n):
  for b in range(a, n):
    for c in range(a, n):
      if a**2 + b**2 == c**2:
        l.append([a,b,c])

# %%
len(l)

# %%
len = 5

# %%
l[:4]

# %%


# %%
list

# %%
l2 = list("abcd")

# %%
l2

# %%
#

# %%
"""
## Interesting problem
"""

# %%
# typical error

# %%
# x= list(np.random.randn(10**3))

# %%
# x[0]

# %%
list = [1,2,3]

# %%
y= list(np.random.randn(10**3))

# %%
measument = [ [1, 2.5, "Adam"], [2, 3.5, "Klaudia"] ]

# %%
measument[0][0] + measument[0][2]

# %%
0.1 + 0.2 == 0.3

# %%
"""
# Numpy
"""

# %%
"""
## Numpy vs list
"""

# %%
def fun(x):
  return x**137 - x**2

# %%
x1 = np.array([range(10)])

# %%
fun(x1)

# %%
x2 = np.geomspace(1e-5, 1e5, num=100)

# %%
x2

# %%
cond = x2 > 1e-3

# %%
x2[cond]

# %%
!pip install random-pesel 

# %%
from random_pesel import RandomPESEL
pesel = RandomPESEL()

# Generate random PESEL number
pesel.generate()

# %%
# Generate random PESEL number
pesel.generate()

# %%
from tqdm import tqdm

# %%
pesel_list = []
for _ in tqdm(range(10000000)):
  current_pesel = pesel.generate()
  pesel_list.append(int(current_pesel))

# %%
len(pesel_list)

# %%
pesel_list[13]

# %%
pesel_list[13] % 1000

# %%
pesel_list[13] % 1000 == 137

# %%
%time filtered_list = [x for x in pesel_list if x % 1000 == 137]

# %%
len(filtered_list)

# %%
100 * len(filtered_list) / len(pesel_list)

# %%
pesel_ndarray = np.asarray(pesel_list)

# %%
%time filtered_ndarray = pesel_ndarray[pesel_ndarray % 1000 == 137]

# %%
len(filtered_ndarray)

# %%
%time x = np.random.randint(low=1, high=100000, size=10000000)

# %%
n = 40000000
year = np.random.randint(low=00, high=99, size=n)
month = np.random.randint(low=1, high=12, size=n)
day = np.random.randint(low=1, high=30, size=n)
ser_1 = np.random.randint(low=0, high=9, size=n)
ser_2 = np.random.randint(low=0, high=9, size=n)
ser_3 = np.random.randint(low=0, high=9, size=n)
sex = np.random.randint(low=0, high=1, size=n)

day[month == 1] = np.random.randint(low=1, high=31, size=n)

# checksum
control = (year//10) + 3*(year%10)
control += 7*(month//10) + 9*(month%10)
control += (day//10) + 3*(day%10)
control += 7*(ser_1//10) + 9*(ser_1%10)
control += (ser_2//10) + 3*(ser_2%10)
control += 7*(ser_3//10) + 9*(ser_3%10)
control += (sex//10) + 3*(sex%10)

control = (10 - (control % 10)) % 10

pesel_db = 1000000000*year + 10000000*month + 100000*day + 10000*ser_1 + 1000*ser_2 + 100*ser_3 + 10 * sex + control

# %%
pesel_db[1]

# %%
%time filtered_ndarray = pesel_db[pesel_db % 1000 == 137]

# %%
pesel_list2 = pesel_db.tolist()

# %%
%time filtered_list = [x for x in pesel_list2 if x % 1000 == 137]

# %%
pesel_db.nbytes // 1000000

# %%
%time res = np.unique(pesel_db, return_counts=True)

# %%
res

# %%
