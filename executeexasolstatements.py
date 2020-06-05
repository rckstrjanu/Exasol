#!/usr/bin/python3

import pyexasol
import sys

# GET DB CONNECTION
Con = pyexasol.connect(dsn="127.0.0.1:8899", user="sys", password ="exasol", schema ="TEST", compression=True);

# GET THE SCHEMA AND EXECUTE STATEMENTS ON TABLES
#Con.execute("OPEN SCHEMA TEST ");
#Con.execute("SELECT * FROM TEST ");

# INSERT DATA TO TABLE
#Con.execute("INSERT INTO telephonelist (name, phone_number) VALUES ('JANARDHAN','1512')");


user=str(sys.argv[1]);
password=str(sys.argv[2]);

print("user: "+user);
print("password: "+password);

# CREATE A USER IN DATABASE
Con.execute("CREATE USER "+user+" IDENTIFIED BY "+password);


#print (Con.execute("DESCRIBE TEST"))
print ("SUCCESSFULL")

