#Draw bar Graph with column (brand_name and sales done in 2019 & in 2020) of "management" table of "mobile" Database.

#main module = matplotlib, sub module = pyplot
#pymysql = to make connection between line_graphh.py file to "mobile" database 

import matplotlib.pyplot as plt       
import numpy as np
import pandas as pd
import pymysql             
           
#db is variable which stores data came from "management" table of database "mobile".
#Here to fetch data from database to .py file use read_sql_query with 2 parameter(sql_query, connection between .py & database)

db=pd.read_sql_query("select * from management",pymysql.connect(host="localhost",user="root",password="",db="mobile"))

#db is passed as a parameter for storing data from .py file to dataframe & then store into df variable.
df=pd.DataFrame(db)
print(df)

#Acessing all rows of perticular column using loc[start:stop:step,"column name"] & store that into respective variable.
bdf=df.loc[0:6,"brand_name"]
sdf=df.loc[0:6,"sales_2019"]
s1df=df.loc[0:6,"sales_2020"]
name=["2019","2020"]

# figure.figsize(width,height)in inches used to change the size of graph.
plt.figure(figsize=(10,6))      

x=np.arange(len(bdf))      # numpy arange() return ndarray of specific range, here it return, [0,1,2,3,4,5,6] store in x.
w=0.3                      # default width=0.8

#Draw 1st bar with plt.bar
plt.bar(x,sdf,width=w,color="orange")

#Used list comprehension for representing 2nd bar next to 1st bar.
x1=[i+w for i in x]            

#Draw 2nd bar next to 1st bar
plt.bar(x1,s1df,width=w,color="g")

#set current xticks location
plt.xticks(x+w/2,bdf)          # add w/2 with x value for change xtick position, x= center of the x coordinate value.

#set label for x and y axis
plt.xlabel("BRAND NAME",color="r",fontsize="large")
plt.ylabel("SALES (2019-2020)",color="r",fontsize="large")

#set title to Graph
plt.title("GLOBAL SMARTPHONE MARKET SALES",color="blue",fontsize="large")

#add grid lines to the plot
plt.grid(linewidth=0.2)

#set legend for describing the elements of graph.
plt.legend(name,loc="upper right",title="SALES",fontsize="large",facecolor="c")     # c=cyan color

plt.show()
