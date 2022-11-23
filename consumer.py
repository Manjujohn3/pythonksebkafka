import mysql.connector

from kafka import KafkaConsumer

import json

import ast



try:

    mydb = mysql.connector.connect(host = 'localhost', user = 'root', password = '',database = 'ksebdb')

except mysql.connector.Error as e:

    print("MySql error",e)



mycursor = mydb.cursor()



bootstrap_server = ["localhost:9092"]



topic = "kseb"



consumer = KafkaConsumer(topic, bootstrap_servers = bootstrap_server)




for i in consumer:

    # print(str(i.value.decode()))

    data_info = ast.literal_eval(i.value.decode())

    print(data_info)

    print(type(data_info))

    user = data_info.get("consumerid")

    unit = data_info.get("unit")

    print(user)

    print(unit)



    sql = "INSERT INTO `usages`( `consumerid`, `unit`, `date`) VALUES(%s,%s,now())"

    data = (user,unit)

    mycursor.execute(sql,data)

    mydb.commit()