
# import python sytem and process utilities
import psutil as ps
# import time library
import time
# import ODBC library
import pyodbc as py

# Creating connection using pyodbc
con = py.connect('Driver={SQL Server};'
                     'Server=NASRULKHAIR\SQLEXPRESS;'
                     'Database=liveSystemsProject,'
                     'Trusted_Conenction=yes;')

#Creating SQL cursor using connection above
cursor =con.cursor()

# Creating never ending loop for the live sytems
while 1==1:
    cpu_usage = ps.cpu_percent()  #use psutils to get the CPU information
    
    print(cpu_usage)
    time.sleep(1)