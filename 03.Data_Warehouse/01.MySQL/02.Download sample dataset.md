# MySQL Data Warehouse Setup Guide

## Step 1: Navigate to the Data Warehouse Directory
If the `03.Data_Warehouse` directory does not exist, create it. Then, navigate to it using the following command:

```bash
cd 03.Data_Warehouse
```

## Step 2: Download the Sample Database
Download the `mysqlsampledatabase.sql` file into the `03.Data_Warehouse` folder using `wget`:

```bash
wget https://raw.githubusercontent.com/HuseynA28/Data-Engineering_Bootcamp/refs/heads/main/datasets/mysqlsampledatabase.sql
```

## Step 3: Load the Sample Database into MySQL
Ensure that the file path is correct before executing the following command:

```bash
source /home/vagrant/03.Data_Warehouse/mysqlsampledatabase.sql
```

## Step 4: Create a New User
Create a new MySQL user called `data_engineer` with a secure password:

```sql
CREATE USER 'data_engineer' IDENTIFIED BY 'Engineer?.123456';
```

## Step 5: Grant Database Privileges
Grant full access to all databases for the `data_engineer` user:

```sql
GRANT ALL PRIVILEGES ON *.* TO 'data_engineer'@'%' WITH GRANT OPTION;
FLUSH PRIVILEGES;
```

## Step 6: Verify User Creation
To confirm that the user has been created and has the correct access permissions, execute:

```sql
SELECT Host, User FROM mysql.user;
```

## Step 7: Exit MySQL
After verifying the setup, exit the MySQL session:

```bash
exit;
```

---

