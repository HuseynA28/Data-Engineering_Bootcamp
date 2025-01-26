# MySQL 8.4 & DBeaver Installation Guide for CentOS 9

## Table of Contents
1. [MySQL Server Installation](#1-mysql-server-installation)  
   - [1.1 Add MySQL Repository](#11-add-mysql-repository)
   - [1.2 Install MySQL Server](#12-install-mysql-server)
   - [1.3 Start and Enable Service](#13-start-and-enable-service)
   - [1.4 Secure Installation](#14-secure-installation)
2. [Database & User Creation](#2-database--user-creation)  
   - [2.1 Access MySQL Console](#21-access-mysql-console)
   - [2.2 Create School Database](#22-create-school-database)
   - [2.3 Create Admin User](#23-create-admin-user)
   - [2.4 Grant Privileges](#24-grant-privileges)
3. [DBeaver Installation](#3-dbeaver-installation)  
   - [3.1 Install Java Runtime](#31-install-java-runtime)
   - [3.2 Install DBeaver](#32-install-dbeaver)
4. [Database Connection](#4-database-connection)  
   - [4.1 Configure DBeaver Connection](#41-configure-dbeaver-connection)
   - [4.2 Essential Driver Properties](#42-essential-driver-properties)
   - [4.3 Test Connection](#43-test-connection)

---

## 1. MySQL Server Installation

### 1.1 Add MySQL Repository
```bash
curl -sSLO https://dev.mysql.com/get/mysql84-community-release-el9-1.noarch.rpm
sudo rpm -ivh mysql84-community-release-el9-1.noarch.rpm
sudo dnf clean all
sudo dnf makecache
```

### 1.2 Install MySQL Server
```bash
sudo dnf install mysql-community-server
```

### 1.3 Start and Enable Service
```bash
sudo systemctl start mysqld
sudo systemctl enable mysqld
```

### 1.4 Secure Installation
```bash
sudo mysql_secure_installation
```
Follow these responses:

- Change password? → **Y**
- Password strength: 100 → **Y**
- Remove anonymous users? → **Y**
- Disallow root remote login? → **N**
- Remove test DB? → **Y**
- Reload privileges? → **Y**

---

## 2. Database & User Creation

### 2.1 Access MySQL Console
```bash
mysql -u root -p
```

### 2.2 Create School Database
```sql
CREATE DATABASE school_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

### 2.3 Create Admin User
```sql
CREATE USER 'school_admin'@'localhost' IDENTIFIED BY 'StrongPass!2024';
```

### 2.4 Grant Privileges
```sql
GRANT ALL PRIVILEGES ON school_db.* TO 'school_admin'@'localhost';
FLUSH PRIVILEGES;
EXIT;
```

---

## 3. DBeaver Installation

### 3.1 Install Java Runtime
```bash
sudo dnf install java-21-openjdk

```

### 3.2 Install DBeaver

#### Method A: Official RPM Package
```bash
wget https://dbeaver.io/files/dbeaver-ce-latest-stable.x86_64.rpm
sudo dnf install ./dbeaver-ce-*.x86_64.rpm
```

#### Method B: Manual Tarball Install
```bash
wget https://dbeaver.io/files/dbeaver-ce-latest-linux.gtk.x86_64.tar.gz
tar -xvzf dbeaver-ce-*.tar.gz -C ~/ 
~/dbeaver/dbeaver &
```

---

## 4. Database Connection

### 4.1 Configure DBeaver Connection
1. Launch **DBeaver** from applications menu.
2. Click **Database → New Connection**.
3. Select **MySQL** icon.
4. Configure parameters:

| Parameter   | Value         |
|------------|--------------|
| Server Host | localhost    |
| Port       | 3306         |
| Database   | school_db    |
| Username   | school_admin |
| Password   | StrongPass!2024 |

### 4.2 Essential Driver Properties
Under **Driver Properties** tab:

| Property               | Value   |
|------------------------|---------|
| allowPublicKeyRetrieval | true   |
| useSSL                 | false  |
| serverTimezone         | UTC    |

### 4.3 Test Connection
Click **Test Connection** → Should show "Connected".

---


