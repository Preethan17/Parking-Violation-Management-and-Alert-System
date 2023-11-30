import mysql.connector
from messaging import send_to
import threading
def update_table(plate):
 search = plate.strip()
 temp=""
 for i in search:
     if i.isalnum() or i==" ":
        temp+=i
        
 search=temp


 try:
        conn = mysql.connector.connect(host='localhost', database='spark', password='pass@123', user='root')
        if conn.is_connected():
                pass
 except:
        print("connection not established")
        exit()
 crsr = conn.cursor()
 cmd1 = 'select * from vehicleusers where vehicle_no="{val}"'.format(val=search)

 crsr.execute(cmd1)

 ans = crsr.fetchone()
 if ans==None:
     return -2

 try:
        cmd = 'update vehicleusers set warning=warning+1 where vehicle_no="{val}"'.format(val=search)
        cmd2 = 'update vehicleusers set fine_due=fine_due+1000*(warning+1) where vehicle_no="{val}"'.format(val=search)
        crsr.execute(cmd2)
        crsr.execute(cmd)
        conn.commit()

 except:
        return []

 cmd3 = 'select * from vehicleusers where vehicle_no="{val}"'.format(val=search)

 crsr.execute(cmd3)

 ans1 = crsr.fetchone()
 conn.close()
 t1=threading.Thread(target=send_to,args=[ans1])
 t1.start()
 return ans1
