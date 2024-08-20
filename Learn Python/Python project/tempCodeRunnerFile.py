
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
cursor = con.cursor()

# Creating never ending loop for the live sytems
while True:
    cpu_usage = ps.cpu_percent()  # get the CPU information
    memory_usage = ps.virtual_memory()[2] # get memory usage information system (in %)

    cpu_intterupts = ps.cpu_stats()[1]
    cpu_calls = ps.cpu_stats()[3]
    
    memory_used = ps.virtual_memory()[3]
    memory_free =ps.virtual_memory()[4] # get memory used statistics from the system
    
    # get some useful internet usage information
    bytes_sent = ps.net_io_counters()[0]
    bytes_received = ps.net_io_counters()[1]
    
    # get disk information
    disk_usage = ps.disk_usage('/')[3]
    
    # inserting the informations collected to SQL Server Database
    cursor.execute('insert into Performance values (GETDATE(),'    # to enter current date and current time
                   + str(cpu_usage) + ','
                   + str(memory_usage) + ','
                   + str(cpu_intterupts) + ','
                   + str(cpu_calls) + ','
                   + str(memory_used) + ','
                   + str(memory_free) + ','
                   + str(bytes_sent) + ','
                   + str(bytes_received) + ','
                   + str(disk_usage) +')'
                   )
    
    #use connection.commit function to finalize the insert command into database
    con.commit()
    print(memory_usage)
    time.sleep(1)