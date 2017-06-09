import peewee as pw
db=pw.MySQLDatabase("assets",
                    host="172.16.1.86",
                    port=3306,
                    user="admin",
                    passwd="admin")
depts=["Computer Engineering","Chemical Engineering",
           "Civil Engineering","Mechanical Engineering",
           "Instrumentation & Control","Information Technology",
           "Electrical Engineering","Electronics & Communication",
           "Admin"]

access=""
for items in depts:
   access+=(items+"\n")

db.execute_sql("""insert into authentication values('admin','admin','%s');"""%(access))
