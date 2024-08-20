
# import python sytem and process utilities
import psutil as ps
# import time library
import time
# import ODBC library
import pyodbc as py

# Creating connection using pyodbc
con = py.connect(
    r'Driver={SQL Server};'
    r'Server=NASRULKHAIR\SQLEXPRESS;'
    r'Database=liveSystemsProject;'
    r'Trusted_Connection=yes;'
)

#Creating SQL cursor using connection above
cursor =con.cursor()

# Creating never ending loop for the live sytems
while True:
    cpu_usage = ps.cpu_percent()  #use psutils to get the CPU information
    
    print(cpu_usage)
    time.sleep(1)