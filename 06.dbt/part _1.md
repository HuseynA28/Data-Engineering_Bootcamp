crate a python envitoment for  dbt and isntall dbt 

create  folder calle d 06.dbt
mkdir 06.dbt

and indtall python3.10
sudo yum update -y

install wget if you have not jey 

sudo yum install wget -y


install 
wget https://www.python.org/ftp/python/3.10.0/Python-3.10.0.tgz


sudo yum install python3-pip


. Install the Required Build Tools and Dependencies
On a RHEL/CentOS (or similar) system, you can install the development tools and required libraries by running:

sudo yum groupinstall "Development Tools"
sudo yum install openssl-devel bzip2-devel libffi-devel zlib-devel



./configure --enable-optimizations


Build and Install Python 3.10:

Compile the source code:

make -j 4


Then install it (using altinstall so you don’t overwrite your system’s default Python):

bash
Copy
Edit
sudo make altinstall

Check that Python 3.10 is installed correctly by running:

bash
Copy
Edit
python3.10 --version


python3.10 -m venv dbt


source dbt/bin/activate


nano ~/.bashrc
alias activate_dbt='source/home/vagrant/Python-3.10.0/dbt/bin/activate'

source ~/.bashrc


activate_dbt


now  install  snowflake adabater 
pip install dbt-snowflake==1.9.0



okay go to 06.dbt  folder 


create a folder called 

mkdir ~/.dbt

now we can creata a  project    callled dbtProject

Enter  a number (which shows the database   enter 1 ) We woudl like to airbnb  database 

the next one is snowflake annout 
go t snowfka e
the account then keep mouse on the accoutn  then copy urls account  suchs as 

https://XXXXX.XXXXX.snowflakecomputing.com

copy the just XXXXX.XXXXX past dbt 

[XXXXX.XXXXX](https://xv31384.eu-central-1.snowflakecomputing.com)


create a user called dbt_user and  grant AIRBNB to  this iser  in snowflake 


USE ROLE ACCOUNTADMIN;

CREATE ROLE IF NOT EXISTS dbt_role;
GRANT ROLE dbt_role TO ROLE ACCOUNTADMIN;

CREATE WAREHOUSE IF NOT EXISTS dbt_warehouse;
GRANT OPERATE ON WAREHOUSE dbt_warehouse TO ROLE dbt_role;


CREATE USER if not exists dbt_user
  PASSWORD='StrongPasword'
  LOGIN_NAME='dbt'
  DEFAULT_WAREHOUSE='dbt_warehouse'
  DEFAULT_ROLE=TRANSFORM
  MUST_CHANGE_PASSWORD=FALSE;

  
GRANT ROLE dbt_role to USER dbt_user;
CREATE DATABASE IF NOT EXISTS AIRBNB;
CREATE SCHEMA IF NOT EXISTS AIRBNB.AIRBNB_DATA;



GRANT ALL ON WAREHOUSE dbt_warehouse TO ROLE dbt_role; 
GRANT ALL ON DATABASE AIRBNB to ROLE dbt_role;
GRANT ALL ON ALL SCHEMAS IN DATABASE AIRBNB to ROLE dbt_role;
GRANT ALL ON FUTURE SCHEMAS IN DATABASE AIRBNB to ROLE dbt_role;
GRANT ALL ON ALL TABLES IN SCHEMA AIRBNB.AIRBNB_DATA to ROLE dbt_role;
GRANT ALL ON FUTURE TABLES IN SCHEMA AIRBNB.AIRBNB_DATA to ROLE dbt_role;


user (dev username): dbt
[1] password
[2] keypair
[3] sso
Desired authentication type option (enter a number): 1
password (dev password):
role (dev role): dbt_role
warehouse (warehouse name): dbt_warehouse
database (default database that dbt will build objects in): AIRBNB
schema (default schema that dbt will build objects in): AIRBNB_DATA
threads (1 or more) [1]: 1
12:14:30  Profile dbtProject written to /home/vagrant/.dbt/profiles.yml using target's profile_template.yml and your supplied values. Run 'dbt debug' to validate the connection.
(dbt) [vagrant@vbox 06.dbt]$ ls
dbtProject  logs
(dbt) [vagrant@vbox 06.dbt]$ cd dbtProject/
(dbt) [vagrant@vbox dbtProject]$ dbt debug


