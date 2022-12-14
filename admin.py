import mysql.connector
from datetime import date
from tabulate import tabulate
mydb= mysql.connector.connect(host = 'localhost' , user = 'root' , password = '' , database = 'ksebdb')
mycursor = mydb.cursor()

while True:
    
    print("Select an option")
    print("1 Add consumer")
    print("2 search consumer")
    print("3 delete consumer")
    print("4 update consumer")
    print("5 view all consumer")
    print("6 Generate bill")
    print("7 view bill")
    print("8 Top 2 high bill")
    print("9 exit")

    choice = int(input("Enter an option: "))
    if(choice==1):
        print("add consumer selected")
        consumerid= input("enter the id:")
        name = input("enter the name:")
        address = input("enter the address:")
        phone = input("enter the number:")
        emailid = input("enter the email:")
        sql = 'INSERT INTO `consumer`(`consumerid`, `name`, `address`, `phone`, `email`) VALUES (%s,%s,%s,%s,%s)'
        data = (consumerid,name,address,phone,emailid)
        mycursor.execute(sql,data)
        mydb.commit()
        print("value inserted succesfully") 

    elif(choice==2):
        print("search consumer selected")
        search = input("enter the consumerid, name ,phone number : ")
        sql = "SELECT `consumerid`, `name`, `address`, `phone`, `email` FROM `consumer` WHERE `consumerid`= '"+search+"' OR `name`='"+search+"' OR `phone`= '"+search+"'"
        mycursor.execute(sql)
        result = mycursor.fetchall()
        for i in result:
             print(i) 
        
    elif(choice==3):
        print("delete consumer selected")
        consumerid = input("enter the id: ")
        sql = 'DELETE FROM `consumer` WHERE consumerid='+consumerid
        mycursor.execute(sql)
        mydb.commit()
        print("data deleted successfully")
    
    
    elif(choice==4):
        print("update consumer selected")
        consumerid= input("enter the id:")
        name = input("enter the name to be updated:")
        address = input("enter the address to be updated:")
        phone = input("enter the number to be updated:")
        emailid = input("enter the email to be updated:")
        sql = "UPDATE `consumer` SET `name`='"+name+"',`address`='"+address+"',`phone`='"+phone+"',`email`='"+emailid+"' WHERE `consumerid` = " +consumerid
        mycursor.execute(sql)
        mydb.commit()
        print("updated succusfully")

    elif(choice==5):
        print("view all consumer selected")
        sql = 'SELECT * FROM `consumer`'
        mycursor.execute(sql)
        result =  mycursor.fetchall()
        for i in result:
            print(i)


    elif(choice==6):
        print("generate bill selected")
        dates = date.today()
        year = dates.year
        month = dates.month
        sql="DELETE FROM `bills` WHERE `month`='"+str(month)+"' AND `year`= '"+str(year)+"'"
        mycursor.execute(sql)
        mydb.commit()
       
        sql="SELECT `id` FROM `consumer`"
        mycursor.execute(sql)
        result=mycursor.fetchall()
        for i in result:
            a=i[0]
            print(a)
          
            sql="SELECT SUM(unit) FROM `usages` WHERE `consumerid`='"+str(a)+"' AND MONTH(date)='"+str(month)+"' AND YEAR(date)='"+str(year)+"' "
            mycursor.execute(sql)
            result=mycursor.fetchone()
            unit=(result[0])
            print(result)
            #print(i)
            total_bill=int(str(result[0])) * 5
            print(total_bill)
            #date= datetime.today().strftime('%Y-%m-%d')
            sql="INSERT INTO `bills`(`consumerid`, `month`, `year`, `bill`, `paidstatus`, `billdate`, `totalunit`,`duedate`) VALUES (%s,%s,%s,%s,%s,now(),%s,now()+interval 14 day)"
            data = (str(a),str(month),str(year),total_bill,'0',unit)
            mycursor.execute(sql,data)
            mydb.commit()
            print("Bill inserted successfully.")
    

    elif(choice==7):
        print("view billselected")
        print("view billselected")
        sql = "SELECT c.name,c.address, b.`month`, b.`year`, b.`paidstatus`, b.`billdate`, b.`totalunit`, b.`bill` FROM `bills` b JOIN consumer c ON b.consumerid=c.id"
        mycursor.execute(sql)
        result = mycursor.fetchall()
        print(tabulate(result,headers=['name','address','month','year', 'paidstatus','billdate','totalunit','bill'],tablefmt = "psql"))
    

        
    elif(choice==8):
        print('Top 2 high bill')
        print('Top 2 high bill')
        sql = "SELECT * FROM `bills` ORDER BY `bill` DESC LIMIT 2"
        mycursor.execute(sql)
        result = mycursor.fetchall()
        print(tabulate(result,headers=['id', 'consumerid', 'month', 'year', 'bill', 'paidstatus', 'billdate',  'totalunit','duedate'])) 
        
    elif(choice==9):
        break