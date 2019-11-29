
In [1]:
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
In [2]:
df = pd.read_csv('BlackFriday.csv')
In [3]:
df.info()

<class 'pandas.core.frame.DataFrame'>
RangeIndex: 537577 entries, 0 to 537576
Data columns (total 12 columns):
User_ID                       537577 non-null int64
Product_ID                    537577 non-null object
Gender                        537577 non-null object
Age                           537577 non-null object
Occupation                    537577 non-null int64
City_Category                 537452 non-null object
Stay_In_Current_City_Years    537577 non-null object
Marital_Status                537577 non-null int64
Product_Category_1            537577 non-null int64
Product_Category_2            370591 non-null float64
Product_Category_3            164278 non-null float64
Purchase                      537577 non-null int64
dtypes: float64(2), int64(5), object(5)
memory usage: 49.2+ MB
In [4]:
df.describe()In [6]:
dfCopy = df.drop(['User_ID','Product_ID','Stay_In_Current_City_Years'],axis=1,inplace=False)
In [7]:
dfCopy.head(3)
Out[7]:

In [8]:
df.head()
In [9]:
df['City_Category'] = df['City_Category'].fillna('city')
In [10]:
df.head()
In [11]:
df['City_Category'] = df['City_Category'].map({
    'A':'Metro Cities',
    'B':'Small Towns',
    'C':'Villages'
})
In [12]:
df.head()
In [13]:
df.rename(columns={
    'Product_Category_1':'Baseball Caps',
    'Product_Category_2':'Wine Tumblers',
    'Product_Category_3':'Pet Raincoats'
})
Out[13]:

In [14]:
df.head(5)
In [15]:
df['Marital_Status'] = df['Marital_Status'].map({
    0:'Unmarried',
    1:'Married'
})
In [16]:
df.head(7)
In [20]:
ax = sns.countplot(data=df,x='Product_Category_1',hue='Gender',palette='Set1')
ax.set(title='Product Category 1',xlabel='Category 1',ylabel='No. of users')
plt.show()

 
In [21]:
ax = sns.countplot(data=df,x='Product_Category_2',hue='Gender',palette='viridis')
ax.set(title='Product Category 2',xlabel='Category 2',ylabel='No. of users')
plt.show()

 
In [22]:
ax = sns.countplot(data=df,hue='Gender',x='City_Category',palette='Set2')
ax.set(title='City Category',xlabel='City',ylabel='No. of users')
plt.show()

 
