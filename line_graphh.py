#Draw line Graph with column (old_price and new_price) of "management" table of "mobile" Database.

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

#Acessing all rows of perticular column using loc[start:stop:step,"column name"] & store into respective variable.
pdf=df.loc[0:6,"old_price"]    
ndf=df.loc[0:6,"new_price"]   
mdf=df.loc[0:6,"model"]        

name=["Old","New"]

# figure.figsize(width,height)in inches used to change the size of graph.
plt.figure(figsize=(8,6))          

#Draw line graph with plt.plot, ms=marker size, mec=marker edge color, mfc=marker face color.

#1st line having marker icon = Diamond(D), line type =dashed & dotted(-.), color=black(k)
plt.plot(mdf,pdf,"D-.k",ms=7,mec="k",mfc="orange")      

#2nd line having marker icon = Circle(o), line type =dashed & dotted(-.), color=red(r), c=cyan color
plt.plot(mdf,ndf,"o-.r",ms=9,mec="k",mfc="c")

#set label for x and y axis
plt.xlabel("MODEL NAME",color="r",fontsize="large")
plt.ylabel("MODEL PRICE (IN Rupees)",color="r",fontsize="large")

#set title to Graph
plt.title("SMARTPHONE PRICE RECORD",color="blue",fontsize="large")

#set current xticks location 
plt.xticks(rotation=10)

#add grid lines to the plot
plt.grid(linewidth=0.4)

#set legend for describing the elements of graph
plt.legend(name,loc="upper right",title="PRICE",fontsize="large",facecolor="y")      # y=yellow color

plt.show()
