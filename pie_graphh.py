#Draw pie chart with column (brand_name and revenue)of "management" table of "mobile" Database.

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
rdf=df.loc[0:6,"revenue"]
bdf=df.loc[0:6,"brand_name"]
l=df.loc[0:6,"brand_name"]

#Pass list of explode(e) value for highlighting perticular section.
e=[0,0.1,0,0,0,0.3,0]

#Set color sequentially for every section of pie chart.
colors=['orange','blue','green','yellow','pink','cyan','red']

# figure.figsize(width,height)in inches used to change the size of graph.
plt.figure(figsize=(5,6))    

#Draw pie chart using plt.pie
#autopct = to display % occupied by each section. here .2f%% meand upto 2 decimal point.
plt.pie(rdf,labels=l,explode=e,autopct="%.2f%%",shadow=True,colors=colors)

#set title to Graph
plt.title("GLOBAL SMARTPHONE PROFIT SHARE BASED ON REVENUE",color="blue",fontsize="large")

#set legend for describing the elements of graph
plt.legend(loc="upper left",title="BRAND NAME",facecolor="c",fontsize="small")       #c=cyan color

plt.show()