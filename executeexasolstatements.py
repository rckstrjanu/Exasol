#!/usr/bin/python3

import pyexasol
import sys

connectedip=str(sys.argv[1]);
user=str(sys.argv[2]);
password=str(sys.argv[3]);
role=str(sys.argv[4])
print("user: "+user);
print("password: "+password);

# GET DB CONNECTION
Con = pyexasol.connect(dsn= connectedip+":8888", user="sys", password ="exasol", schema ="TEST", compression=True);

#user=str(sys.argv[2]);
#password=str(sys.argv[3]);
#role=str(sys.argv[4])
#print("user: "+user);
#print("password: "+password);

# CREATE A USER IN DATABASE
Con.execute("CREATE USER "+user+" IDENTIFIED BY "+password);
print("user created");

#Con.execute("CREATE ROLE "+role);
#print("Role created");

Con.execute("GRANT "+role+ " TO "+user);
print("Role "+role+" has been assigned to user: "+user);

print ("SUCCESSFULL");

