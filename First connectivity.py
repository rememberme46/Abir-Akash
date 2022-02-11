import mysql.connector as mc
from tabulate import tabulate
mycon=mc.connect(host="localhost",user="root",password="nps@123",database="project")
if mycon.is_connected():
    print("connected")
    mycursor=mycon.cursor()


def disprecco():
    query=("select * from stock")
    mycursor.execute(query)
    result=mycursor.fetchall()
    table=[["ITEM CODE","ITEM NAME","QUANTITY","PRICE","DISCOUNT","DOM"]]
    for rec in result:
        table.append(list(rec))
    print(tabulate(table))

def addstockreco():
       itemcode=int(input("Enter Item Code:"))
       itemname=input("Enter Item Name:")
       qty=int(input("Enter Quantity in Stock:"))
       price=float(input("Enter Price of Item:"))
       discount=int(input("Enter Discount % Applicable:"))
       dom=int(input("Enter the DOM (YYYY-MM-DD)-:"))
       query="insert into stock values({},'{}',{},{},{},'{}')".format(itemcode,itemname,qty,price,discount,dom)
       mycursor.execute(query)
       print("Record Succesfully Inserted")
       mycon.commit()

def delstockreco():
       itemd=int(input("Enter Item Code to be Deleted -:"))
       query="select * from stock where itemcode="+str(itemd)
       mycursor.execute(query)
       result=mycursor.fetchone()
       deltable=[["ITEMCODE","ITEMNAME","QUANTITY","PRICE","DISCOUNT","DOM"]]
       if result!=None:
           deltable.append(list(result))
           print(tabulate(deltable))
           ans=input("Do you want to Delete(Y/N)?:")
           if ans=="y" or ans=="Y":
               query="delete from stock where itemcode="+str(itemd)
               print("Data Deleted")
       mycursor.execute(query)
       mycon.commit()
           

def searchreco():
    try:
        n=(input("Enter Item name for searching -:"))
        query="Select * from stock where itemname='%s'"%(n)
        mycursor.execute(query)
        result=mycursor.fetchone()
        table=[["ITEMCODE","ITEMNAME","QUANTITY","PRICE","DISCOUNT","DOM"]]
        if result!=None:
            table.append(list(result))
            print("Record Found And Is Available")
            print(tabulate(table))
            mycursor.execute(query)
            mycon.commit()
    except:
        if result==None:
            print("Record Not Available")


def modifystockreco():
       try:
              query=("select * from stock")
              mycursor.execute(query)
              result=mycursor.fetchall()
              table=[["ITEMCODE","ITEMNAME","QUANTITY","PRICE","DISCOUNT","DOM"]]
              for rec in result:
                     table.append(list(rec))
              print(tabulate(table))
              modtable=[["ITEMCODE","ITEMNAME","QUANTITY","PRICE","DISCOUNT","DOM"]]
              find=int(input("Enter Item Code For Modifying -:"))
              query="select * from stock where itemcode="+str(find)
              mycursor.execute(query)
              result=mycursor.fetchone()
              if result!=None:
                     print("What Do you Want to Modify?")
                     print("1.Item Name")
                     print("2.Quantity")
                     print("3.Price")
                     print("4.Discount")
                     print("5.DOM")
                     ch=int(input("Enter Your Choice -:"))
                     if ch==1:
                         i1=input("Enter New Item Name -:")
                         query="update stock set itemname='{}' where itemcode={}".format(i1,find)
                     elif ch==2:
                         i2=int(input("Enter New Quantity -:"))
                         query="update stock set qty={} where itemcode={}".format(i2,find)
                     elif ch==3:
                         i3=int(input("Enter New Price -:"))
                         query="update stock set price={} where itemcode={}".format(i3,find)
                     elif ch==4:
                         i4=int(input("Enter New Discount -:"))
                         query="update stock set itemname={} where itemcode={}".format(i4,find)
                     elif ch==5:
                         i5=int(input("Enter New DOM -:"))
                         query="update stock set dom='{}' where itemcode={}".format(i5,find)
                        
              mycursor.execute(query)
              print("Record Modified")
              query="select * from stock where itemcode="+str(find)
              mycursor.execute(query)
              result=mycursor.fetchone()
              modtable.append(list(result))
              print(tabulate(modtable))
              mycon.commit()
       except:
              if result==None:
                     print("Record Not Available")

while True:
       print("=====SHOPPING MALL STOCK MENU=====")
       print("--Select Your Choice--")
       print("1.Display Stock Record")
       print("2.Add Stock Record")
       print("3.Modify Stock Record")
       print("4.Delete Stock Record")
       print("5.Search Stock Record")
       print("6.Exit")
       ch=int(input("Enter Your Choice:"))
       if ch==1:
           disprecco()
       elif ch==2:
           addstockreco()
       elif ch==3:
            modifystockreco()
       elif ch==4:
            delstockreco()
       elif ch==5:
            searchreco()
       elif ch==6:
            break
       else:
            print("Invalid Choice")
else:
    print("Invalid Choice")

       
                            

