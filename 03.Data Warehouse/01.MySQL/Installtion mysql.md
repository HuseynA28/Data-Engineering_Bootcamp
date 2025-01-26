# MySQL 8.4 & DBeaver Installation Guide for CentOS 9

This guide walks you through installing MySQL 8.4 on CentOS 9, configuring a database and user, and then installing and connecting to the database via DBeaver. The instructions are written for beginners and should be easy to follow.

## Tip: Create a dedicated folder to store any scripts or notes you use during installation.

```bash
mkdir 03.Data_Warehouse
cd 03.Data_Warehouse
```

## Table of Contents
1. [MySQL Server Installation](#mysql-server-installation)
   - [Add MySQL Repository](#add-mysql-repository)
   - [Install MySQL Server](#install-mysql-server)
   - [Start and Enable Service](#start-and-enable-service)
   - [Secure Installation](#secure-installation)
2. [Database & User Creation](#database--user-creation)
   - [Access MySQL Console](#access-mysql-console)
   - [Create School Database](#create-school-database)
   - [Create Admin User](#create-admin-user)
   - [Grant Privileges and Configure Remote Access](#grant-privileges-and-configure-remote-access)
3. [DBeaver Installation](#dbeaver-installation)
   - [Install Java Runtime](#install-java-runtime)
   - [Install DBeaver](#install-dbeaver)
4. [Database Connection via DBeaver](#database-connection-via-dbeaver)
   - [Configure DBeaver Connection](#configure-dbeaver-connection)
   - [Essential Driver Properties](#essential-driver-properties)
   - [Test Connection](#test-connection)

## 1. MySQL Server Installation

### 1.1 Add MySQL Repository
By default, the MySQL 8.4 packages are not included in CentOS 9’s repositories. We need to add MySQL’s official repository first:

```bash
curl -sSLO https://dev.mysql.com/get/mysql84-community-release-el9-1.noarch.rpm
sudo rpm -ivh mysql84-community-release-el9-1.noarch.rpm
sudo dnf clean all
sudo dnf makecache
```

### 1.2 Install MySQL Server
Once the repository is added, proceed with the installation:

```bash
sudo dnf install mysql-community-server
```

### 1.3 Start and Enable Service
After installation, start the MySQL service and ensure it starts automatically on reboot:

```bash
sudo systemctl start mysqld
sudo systemctl enable mysqld
```

### 1.4 Secure Installation
When MySQL is first installed, it generates a temporary root password. To find it, run:

```bash
sudo grep 'temporary password' /var/log/mysqld.log
```

You should see an entry like:

```
[Note] A temporary password is generated for root@localhost: <random_password>
```

Use this temporary password to log in and immediately change it:

```bash
mysql -u root -p
```

Enter the temporary password when prompted.

Change the root password (replace `Vagrant?.123456` with your preferred strong password):

```sql
ALTER USER 'root'@'localhost' IDENTIFIED BY 'Vagrant?.123456';
```

Follow the prompts accordingly.

## 2. Database & User Creation

### 2.1 Access MySQL Console
To make any changes (create databases, users, etc.), you’ll need to log in as root:

```bash
mysql -u root -p
```

### 2.2 Create School Database
Inside the MySQL console, create a new database named `school_db`. We’ll use UTF8MB4 for broad character support.

```sql
CREATE DATABASE school_db
  CHARACTER SET utf8mb4
  COLLATE utf8mb4_unicode_ci;
```

### 2.3 Create Admin User
Still in the MySQL console, create a dedicated admin user that can connect from any host (`%` means any IP or domain):

```sql
CREATE USER 'school_admin'@'%'
  IDENTIFIED BY 'StrongPass!2024';
```

### 2.4 Grant Privileges and Configure Remote Access
Grant the user full privileges on all databases:

```sql
GRANT ALL PRIVILEGES ON *.* TO 'school_admin'@'%' WITH GRANT OPTION;
FLUSH PRIVILEGES;
```

Optional check: To verify the user was created successfully:

```sql
SELECT Host, User FROM mysql.user;
```

Exit MySQL:

```sql
exit;
```

Enable remote connections: By default, MySQL may only listen on localhost. To allow external connections, edit the MySQL configuration:

```bash
sudo nano /etc/my.cnf
```

Under the `[mysqld]` section, set:

```
bind-address = 0.0.0.0
```

Save and exit the file. Then restart MySQL:

```bash
sudo systemctl restart mysqld
```

Do not forget to open port 3306 in VirtualBox.

## 3. DBeaver Installation
Install DBeaver on your local computer.

## 4. Database Connection via DBeaver

Now let’s connect to `school_db` with the user `school_admin` via DBeaver.

### 4.1 Configure DBeaver Connection
1. Open DBeaver.
2. Click **Database → New Connection**.
3. Select **MySQL**.
4. Input the following parameters (adjust if your MySQL server is remote):

| Parameter | Value |
|-----------|--------|
| Server Host | localhost |
| Port | 3306 |
| Database | school_db |
| Username | school_admin |
| Password | StrongPass!2024 |

5. Click **Next** (or **Test Connection**).

### 4.2 Essential Driver Properties

In some cases, you may need to adjust driver properties. Click **Edit Driver Settings** (or **Driver Properties** in DBeaver) and add or change:

| Property | Value |
|-----------|--------|
| allowPublicKeyRetrieval | true |
| useSSL | false |
| serverTimezone | UTC |

### 4.3 Test Connection
Click **Test Connection**. If successful, you’ll see **Connected**.
