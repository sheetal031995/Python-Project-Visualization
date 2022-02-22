#Main python file is analytics.py

#flask is a module of Flask class. 
#pymysql module used as interpreter to connect python file to database.
#database is created through localhost phpmyadmin with the help of xampp.

from flask import Flask,render_template,request,redirect,url_for
import pymysql

#object pro of Flask class is created 
pro=Flask(__name__)

#analytics_dashboard---------->

@pro.route('/')
def index():

    try:
        #Establish connection with database, where database name = mobile.
        db=pymysql.connect(host="localhost",user="root",password="",db="mobile")
        cu=db.cursor()
        
        #Table name = management
        sql="select * from management"
        
        cu.execute(sql)
        data=cu.fetchall()
      
        return render_template('analytics_dashboard.html',d=data)
    
    except Exception:
    
        return "Error"

#Record added route-------->
#To add new record

@pro.route('/record')
def added_record():

    return render_template('create_record.html')  
    
#Store route--------->
#For storing record details from dashboard to database.

@pro.route('/store',methods=['POST','GET'])

def store():

    #Request module is used for taking data from html form to analytics.py file.
    n=request.form['brand_name']
    m=request.form['model']
    op=request.form['old_price']
    np=request.form['new_price']
    s1=request.form['sales_2019']
    s2=request.form['sales_2020']
    r=request.form['revenue']
    
    try:
        db=pymysql.connect(host="localhost",user="root",password="",db="mobile")
        cu=db.cursor()
        
        #Sql_query to insert record into "management" table of "mobile" database. 
        sql="insert into management(brand_name,model,old_price,new_price,sales_2019,sales_2020,revenue)values('{}','{}','{}','{}','{}','{}','{}')".format(n,m,op,np,s1,s2,r)
        
        cu.execute(sql)
        db.commit()
        
        return redirect('/')
        
    except Exception:

        db.rollback()
        return "Error"  
    

#Delete operation---------->

@pro.route('/delete/<rid>')  #rid is a variable which store id (record id)

def delete(rid):

    try:
        db=pymysql.connect(host="localhost",user="root",password="",db="mobile")
        cu=db.cursor()
        
        # sql_query to delete record from management table
        sql="delete from management where id={}".format(rid)
        
        cu.execute(sql)
        db.commit()

        #return "data inserted into table"
        return redirect('/')
        
    except Exception:
        
        db.rollback()
        return "Error"
        
#route for Edit operation--------------->

@pro.route('/edit/<rid>')  #rid is a variable which store id

def edit(rid):

    try:
        db=pymysql.connect(host="localhost",user="root",password="",db="mobile")
        cu=db.cursor()
        
        sql="select * from management where id={}".format(rid)
        cu.execute(sql)
        data=cu.fetchone()
        return render_template('edit_analytics.html',d=data)
        #return "Success"
        
    except Exception:
        return "Error"
        
#route for Update operation----------->

@pro.route('/update',methods=['POST','GET']) 

def update():

    rid=request.form['rid']
    n=request.form['brand_name']
    m=request.form['model']
    op=request.form['old_price']
    np=request.form['new_price']
    s1=request.form['sales_2019']
    s2=request.form['sales_2020']
    r=request.form['revenue']
    
    
    try:
        db=pymysql.connect(host="localhost",user="root",password="",db="mobile")
        cu=db.cursor()
        sql="update management SET brand_name='{}',model='{}',old_price='{}',new_price='{}',sales_2019='{}',sales_2020='{}',revenue='{}' where id='{}'".format(n,m,op,np,s1,s2,r,rid)
        cu.execute(sql)
        db.commit()
        return redirect('/')
        
    except Exception:
        db.rollback()
        return "Error"    

       
    
if __name__=='__main__':   #where main file is analytics.py.

    pro.run(debug=True)    #run() is the method of Flask class.