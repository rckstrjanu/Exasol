sudo apt-get update

sudo apt-get install openjdk-8-jdk


java -version



https://github.com/rckstrjanu/Exasol.git



https://www.exasol.com/support/secure/attachment/79637/EXAplus-6.0.15.tar.Z

tar -xzf EXAplus-6.0.15.tar.Z

CD to the directory


execute the ./exaplus

./exaplus -c localhost:8899 -u sys -P exasol

./exaplus -c 127.0.0.1:8899 -u sys -P exasol

~/Janu/EXAplus-6.0.15/exaplus -c 10.156.0.6:8899 -u sys -P exasol

-- To verify users 
SELECT * FROM SYS.EXA_ALL_USERS;

SELECT * FROM SYS.EXA_ALL_ROLES;

CREATE USER JANA IDENTIFIED BY "exasol"





 
docker build . -t exasol_image

docker run --name exasoldb -p 127.0.0.1:8899:8888 --detach --privileged --stop-timeout 120  exasol/docker-db


docker run --name exasoldb -p 8888:8888 --detach --privileged --stop-timeout 120  exasol/docker-db

sudo ufw allow 8080
   26  sudo ufw status
   27  sudo ufw allow OpenSSH
   28  sudo ufw enable


https://github.com/exasol/docker-db


CREATE TABLE telephonelist(name VARCHAR(10),phone_number VARCHAR(10),type VARCHAR(10) DEFAULT 'home',alterationtime TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
          


INSERT INTO telephonelist (name, phone_number) VALUES ('Meyer', '1234');
INSERT INTO telephonelist (name, phone_number) VALUES ('Müller','5678');
INSERT INTO telephonelist (name, type, phone_number) VALUES ('Meyer', 'work', '9999');
UPDATE telephonelist SET name='Meier', alterationtime=DEFAULT WHERE phone_number='1234';
          



---Python

python ––version

sudo apt update


sudo apt install software-properties-common

sudo add-apt-repository ppa:deadsnakes/ppa

sudo apt update


sudo apt install python3.7

python ––version


sudo apt update


sudo apt install build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev wget

cd /tmp

wget https://www.python.org/ftp/python/3.7.5/Python-3.7.5.tgz


tar –xf Python-3.7.5.tgz


cd python-3.7.5


./configure ––enable–optimizations



apt install python-pip

Link: https://phoenixnap.com/kb/how-to-install-python-3-ubuntu

python3 -m pip install pandas

python3 -m pip install pyexasol


pip install sqlalchemy-exasol    ( SRC: https://superset.incubator.apache.org/installation.html#database-dependencies)


Websocket API - https://github.com/EXASOL/websocket-api/tree/master/python

python3.6 -m pip install pyodbc

sudo apt-get install python3.6-dev
sudo apt-get install unixodbc-dev
yum install unixODBC
sudo apt-get install python3.7-dev  (SRC: https://github.com/mkleehammer/pyodbc/issues/276)
 
 
[code language="python" gutter="false"]
Con = pyexasol.connect(dsn=[IP-adress]:[port], user=[user], password = [password], schema = [schema], compression=True)
[/code]


Con = pyexasol.connect(dsn=[localhost]:[8899], user=[sys], password = [exasol], schema = [TEST], compression=True)

Con = pyexasol.connect(dsn="localhost:8899", user=sys, password ="exasol", schema ="TEST", compression=True)

Con.execute("OPEN SCHEMA TEST ");
Con.execute("SELECT * FROM TEST ");


Table:


CREATE TABLE test (SNO VARCHAR(20),NAME VARCHAR(20),MOBILE VARCHAR(20),DATE TIMESTAMP DEFAULT CURRENT_TIMESTAMP;

CREATE TABLE test (SNO VARCHAR(20),NAME VARCHAR(20),MOBILE VARCHAR(20));


INSERT INTO test (SNO,NAME,MOBILE) VALUES ("1","RAVI","15124994956");


SCHEMA : TEST
Table : test



==========================================================WORKING SCRIPT================================

>>TO LOGIN TO SCHEMA 

OPEN SCHEMA <SCHEMA_NAME>

>> TO CHECK THE DATABASE TABLES 


SELECT * FROM TABLE_NAME;

>> TO CREATE A TABLE 

CREATE TABLE test (SNO VARCHAR(20),NAME VARCHAR(20),MOBILE VARCHAR(20));

INSERT INTO test (SNO,NAME,MOBILE) VALUES ("1","RAVI","15124994956");



CREATE TABLE telephonelist(name VARCHAR(10),phone_number VARCHAR(10),type VARCHAR(10) DEFAULT 'home',alterationtime TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
          
INSERT INTO telephonelist (name, phone_number) VALUES ('Meyer', '1234');
INSERT INTO telephonelist (name, phone_number) VALUES ('Müller','5678');
INSERT INTO telephonelist (name, type, phone_number) VALUES ('Meyer', 'work', '9999');
UPDATE telephonelist SET name='Meier', alterationtime=DEFAULT WHERE phone_number='1234';


>> TO VERIFY THE USERS 

SELECT * FROM SYS.EXA_ALL_USERS;

SELECT * FROM SYS.EXA_ALL_ROLES;


>> TO CREATE THE USER 

CREATE USER JANA IDENTIFIED BY "exasol";


>> Python Script for logging into the database and executing DML, DDL etc queries.

        #!/usr/bin/python3

        import pyexasol

        # To get the connection object and connect to Exasol Database 
        Con = pyexasol.connect(dsn="127.0.0.1:8899", user="sys", password ="exasol", schema ="TEST", compression=True);

        # To Open the schema and verify the tables and the data
        #Con.execute("OPEN SCHEMA TEST ");
        #Con.execute("SELECT * FROM TEST ");

        # To Insert the data to the exasol database table
        #Con.execute("INSERT INTO telephonelist (name, phone_number) VALUES ('JANARDHAN','1512')");

        # To create a user in the database with password
        Con.execute("CREATE USER JANA IDENTIFIED BY \"exasol\"");
        #print (Con.execute("DESCRIBE TEST"))
        print ("SUCCESSFULL")
        
        
>> VERSION TWO 

USAGE: python3 <script.py> <username> <password>


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
        print ("user: ",user);
        print ("CREATE USER "+user+" IDENTIFIED BY " +password);
        # CREATE A USER IN DATABASE
        Con.execute("CREATE USER "+user+" IDENTIFIED BY "+password);


        #print (Con.execute("DESCRIBE TEST"))
        print ("SUCCESSFULL")        
        

                            >> EXASOL SETUP <<
===================================XXXXX==========================================================

PREQUISITES:

-- python >3.6

-- EXAPLUS 

-- UBUNTU 18.xx / LINUX 


STEPS TO CREATE EXASOL ENVIRONMENT : 
====================================

DOCKER FILE FOR THE EXASOL SETUP 
================================
1. To login to the exasol database we need to run the following dockerfile to setup the database.

    Dockerfile
        From exasol/docker-db
        
docker run --name exasoldb -p 127.0.0.1:8899:8888 --detach --privileged --stop-timeout 120  exasol/docker-db
        
docker build -t exasol_db .

docker run --name exasoldb -p 127.0.0.1:8899:8888 --detach --privileged --stop-timeout 120 -v %DOCKER_HOME%/exa_vol:/exa exasol/docker-db:latest

docker run --name exasol_db -p 127.0.0.1:8899:8888 --detach --privileged --stop-timeout 120 exasol/docker-db:latest

docker exec -it 15d66b8f03ca exaplus -c localhost:8888 -u sys -P exasol        

INSTALLING THE PYTHON > 3.6 Version
===================================

Uninstall existing version of python 

sudo apt purge python2.*

https://medium.com/@moreless/install-python-3-6-on-ubuntu-16-04-28791d5c2167 (USE THIS APPROACH)

1.  sudo apt update

2.  sudo apt install software-properties-common

3.  sudo add-apt-repository ppa:deadsnakes/ppa

4.  sudo apt update

5.  sudo apt install python3.7

6.  Install the python pip3 version for the python 3 (SRC:  https://phoenixnap.com/kb/how-to-install-python-3-ubuntu)

    apt install python-pip
    
    python3.7 -m pip install pip

    python3.7 -m pip install pyexasol

7.  Install the python module pandas for the python using the python pip (SRC: Link: https://phoenixnap.com/kb/how-to-install-python-3-ubuntu)
    
    python3 -m pip install pandas

    python3 -m pip install pyexasol

    pip install sqlalchemy-exasol    ( SRC: https://superset.incubator.apache.org/installation.html#database-dependencies)
    
    sudo apt-get install python3.6-dev
    
    sudo apt-get install unixodbc-dev
    
    apt-get install unixODBC

    
LOGIN PROCESS:
==============

1. Down load the following tar file from the below path to get the "EXAPLUS" setup used to connect to the database.

    SRC_LOCATION: https://www.exasol.com/support/secure/attachment/79637/EXAplus-6.0.15.tar.Z

2. unzip the tar file 
    
    tar -xzf EXAplus-6.0.15.tar.Z
    
3. CD to EXAplus-6.0.15 directory

4. To login to the DB user name and password is required.

   By default the EXAPLUS will have the default user and password as follows.
   
   user: "sys"
   password: "exasol"
   
   Use the following statement to connect to the DB from the Exasol directory where "exaplus" directory exists.
   
   ./exaplus -c 127.0.0.1:8899 -u sys -P exasol
   
   Replace the IP with the system IP / Public IP configuration and -u <user> -p <password>
   
5. To Login to the Schema execute the following commands 

   OPEN SCHEMA <NAME_OF_THE_SCHEMA>
   
6. To select the data from the table use the following command 

   SELECT * FROM <TABLE_NAME>;
   
7. To Describe the table structure use the following command.

   DESCRIBE <TABLE_NAME>;
   

    
    
/root/ExasolDocker/ExasolSetup/Exasol

    
/root/EXAplus-6.0.15


=====================================================================================================


pipeline
    {
      environment {
        build_branch = 'rckstrstestcase1'
      //repo_name = 'Hellonodejs'
        
      }
      agent {
        docker {
            image 'maven:3.3.3'
            
        }
    }
      stages
      {
        stage('SCM CHECKOUT')
        {
          steps
          {
            echo env.build_branch + 'master'
            git changelog: false, credentialsId: 'github', poll: true, url:  "https://github.com/roomoffireandice/rckstrs.git", branch: env.build_branch

          }
        }
              stage('Build the artifact')
                    {
                      steps
                      {
                        sh '/usr/bin/mvn clean install -DskipTests=true'
                      }
                    }
					
     }
	}

=====================================================================================================


    
pipeline
    {
      environment {
        build_branch = 'master'
      }
      agent { 
          node{
             label 'master'
          }
      }
      stages
      {
        stage('SCM CHECKOUT')
        {
          steps
          {
            echo env.build_branch + 'master'
            git changelog: false, credentialsId: '92543824-59b3-4df6-a8d5-5fbc7807ba95', poll: true, url:  "https://github.com/rckstrjanu/Exasol.git", branch: env.build_branch

          }
        }
              stage('Build the artifact')
                    {
                      steps
                      {
                        sh '/usr/bin/python3 /var/lib/jenkins/workspace/ExasolPipeline/executeexasolstatements.py user password'
                      }
                    }
					
     }
	}
    
=====================================================================================================


pipeline
    {
      environment {
        build_branch = 'master'
      }
      agent { 
          node{
             label 'master'
          }
      }
      stages
      {
        stage('SCM CHECKOUT')
        {
          steps
          {
            echo env.build_branch + 'master'
            git changelog: false, credentialsId: '92543824-59b3-4df6-a8d5-5fbc7807ba95', poll: true, url:  "https://github.com/rckstrjanu/Exasol.git", branch: env.build_branch

          }
        }
              stage('Build the artifact')
                    {
                      steps
                      {
                        sh 'sudo -i'
                        sh 'pwd'
                        sh 'chmod 777 executeexasolstatements.py'
                        sh '/usr/bin/python3 /var/lib/jenkins/workspace/ExasolPipeline/executeexasolstatements.py'
                      }
                    }
					
     }
	}    
    
=====================================================================================================    

pipeline
    {
      environment {
        build_branch = 'master'
      }
      agent { 
          node{
             label 'master'
          }
      }
      stages
      {
        stage('SCM CHECKOUT')
        {
          steps
          {
            echo env.build_branch + 'master'
            git changelog: false, credentialsId: '92543824-59b3-4df6-a8d5-5fbc7807ba95', poll: true, url:  "https://github.com/rckstrjanu/Exasol.git", branch: env.build_branch

          }
        }
              stage('Build the artifact')
                    {
                      steps
                      {
                        sh 'sudo -i'
                        sh 'pwd'
                        sh 'chmod 777 executeexasolstatements.py'
                        sh 'python3 /var/lib/jenkins/workspace/ExasolPipeline/executeexasolstatements.py'
                      }
                    }
					
     }
	} 
    
    
    =====================================================================================================    
    
    pipeline
    {
      environment {
        build_branch = 'master'
      }
      agent { 
          node{
             label 'master'
          }
      }
      stages
      {
        stage('SCM CHECKOUT')
        {
          steps
          {
            echo env.build_branch + 'master'
            git changelog: false, credentialsId: 'github', poll: true, url:  "https://github.com/rckstrjanu/Exasol.git", branch: env.build_branch

          }
        }
              stage('Build the artifact')
                    {
                      steps
                      {
                        sh 'sudo -i'
                        sh 'pwd'
                        sh 'chmod 777 executeexasolstatements.py'
                        sh 'python3 /var/lib/jenkins/workspace/Exasol/executeexasolstatements.py'
                      }
                    }
					
     }
	} 
    
=======================================PARAMETEISED BUILDS==============================================================        
    
    
    
   pipeline
    {
    
   parameters {
        string(name: 'PERSON', defaultValue: 'RAMU')
    }
    
      environment {
        build_branch = 'master'
      }
      agent { 
          node{
             label 'master'
          }
      }
      stages
      {
        stage('SCM CHECKOUT')
        {
          steps
          {
            echo env.build_branch + 'master'
            git changelog: false, credentialsId: 'f006dab2-4db2-447f-90f5-747e49c4b53e', poll: true, url:  "https://github.com/rckstrjanu/Exasol.git", branch: env.build_branch

          }
        }
              stage('Build the artifact')
                    {
                      steps
                      {
                        sh 'sudo -i'
                        sh 'chmod 777 executeexasolstatements.py'
                        echo "Hello ${params.PERSON}"
                        sh "python3.7 /var/lib/jenkins/workspace/Exasol/executeexasolstatements.py ${params.PERSON} exasol"
                      }
                    }
					
     }
	}     
    
    
============================PARAMETEISED BUILDS WITH USER AND PASSWORD=========================================================            
    
   pipeline
    {
    
   parameters {
        string(name: 'PERSON', defaultValue: 'RAMU')
        password(name: 'PASSWORD', defaultValue: 'exasol', description: 'Enter a password')
    }
    
      environment {
        build_branch = 'master'
      }
      agent { 
          node{
             label 'master'
          }
      }
      stages
      {
        stage('SCM CHECKOUT')
        {
          steps
          {
            echo env.build_branch + 'master'
            git changelog: false, credentialsId: 'f006dab2-4db2-447f-90f5-747e49c4b53e', poll: true, url:  "https://github.com/rckstrjanu/Exasol.git", branch: env.build_branch

          }
        }
              stage('Build the artifact')
                    {
                      steps
                      {
                        sh 'sudo -i'
                        sh 'chmod 777 executeexasolstatements.py'
                        echo "Hello ${params.PERSON}"
                        sh "python3.7 /var/lib/jenkins/workspace/Exasol/executeexasolstatements.py ${params.PERSON} ${params.PASSWORD}"
                      }
                    }
					
     }
	}     
    
============================================================================================================================

   pipeline
    {
    
   parameters {
        string(name: 'ADD_USER', defaultValue: 'RAMU')
        password(name: 'ADD_USER_PASSWORD', defaultValue: 'exasol', description: 'Enter a password')
        string(name: 'FOR_DB_USER', defaultValue: 'RAMU')
        password(name: 'DB_PASSWORD', defaultValue: 'exasol', description: 'Enter a password')
    }
    
      environment {
        build_branch = 'master'
      }
      agent { 
          node{
             label 'master'
          }
      }
      stages
      {
        stage('SCM CHECKOUT')
        {
          steps
          {
            echo env.build_branch + 'master'
            git changelog: false, credentialsId: 'f006dab2-4db2-447f-90f5-747e49c4b53e', poll: true, url:  "https://github.com/rckstrjanu/Exasol.git", branch: env.build_branch

          }
        }
              stage('Build the artifact')
                    {
                      steps
                      {
                        sh 'sudo -i'
                        sh 'chmod 777 executeexasolstatements.py'
                        echo "ADDED USER ${params.ADD_USER}"
                        echo "ADD FOR DB ${params.FOR_DB_USER}"
                        echo "LOGGED INTO DB VIA ${params.DB_PASSWORD}"
                        sh "python3.7 /var/lib/jenkins/workspace/Exasol/executeexasolstatements.py ${params.ADD_USER} ${params.ADD_USER_PASSWORD}"
                      }
                    }
					
     }
	} 
    
    ===========================WORKING WITH PARAMS FINAL======================================
    
       pipeline
    {
    
   parameters {
       
        string(name: 'ADD_USER', defaultValue: ' ')
        password(name: 'ADD_USER_PASSWORD', defaultValue: 'exasol')
        choice(name: 'ROLE', choices: ['ETL_ROLE','DATA_LAKE_ETL','NPN_WRITE READ_ONLY_ROLE','DATALAKE','DATALAKE_RB'])
        string(name: 'DB_IP', defaultValue: ' ')
        password(name: 'PASSWORD', defaultValue: 'exasol', description: 'Enter a password')
       
        
   }
    
      environment {
        build_branch = 'master'
      }
      agent { 
          node{
             label 'master'
          }
      }
      stages
      {
        stage('SCM CHECKOUT')
        {
          steps
          {
            echo env.build_branch + 'master'
            git changelog: false, credentialsId: 'f006dab2-4db2-447f-90f5-747e49c4b53e', poll: true, url:  "https://github.com/rckstrjanu/Exasol.git", branch: env.build_branch

          }
        }
              stage('Build the artifact')
                    {
                      steps
                      {
                        sh "sudo -i"
                        sh "chmod 777 executeexasolstatements.py"
                        echo "ADDED USER ${params.ADD_USER}"
                        echo "ROLES IS: ${ROLE}"
                        sh "python3.7 /var/lib/jenkins/workspace/Exasol/executeexasolstatements.py ${params.ADD_USER} ${params.ADD_USER_PASSWORD} ${params.ROLE}"
                      }
                    }
					
     }
	} 
    
    =========================================WORKING PIPELINE WITHOUT PARAMS=========================================================
    
   pipeline
    {
      environment {
        build_branch = 'master'
      }
      agent { 
          node{
             label 'master'
          }
      }
      stages
      {
        stage('SCM CHECKOUT')
        {
          steps
          {
            echo env.build_branch + 'master'
            git changelog: false, credentialsId: 'f006dab2-4db2-447f-90f5-747e49c4b53e', poll: true, url:  "https://github.com/rckstrjanu/Exasol.git", branch: env.build_branch

          }
        }
              stage('Build the artifact')
                    {
                      steps
                      {
                        sh 'sudo -i'
                        sh 'chmod 777 executeexasolstatements.py'
                        sh 'python3.7 /var/lib/jenkins/workspace/Exasol/executeexasolstatements.py exasol1 exasol ETL_ROLE'
                      }
                    }
					
     }
	} 

====================================================================================================================    
    
    
