# Installing Hadoop 1.2.1 and Hive 0.14 on CentOS

## 1. Setting Up Your Virtual Machine with CentOS

1. **Download and Install VirtualBox**  
   - [Download VirtualBox](https://www.virtualbox.org/wiki/Downloads)

2. **Download CentOS 7 (64-bit ISO)**  
   - [Download CentOS](https://www.centos.org/download/)

3. **Create a Virtual Machine in VirtualBox**  
   - Name: `CentOS_Hadoop`
   - Type: `Linux`
   - Version: `Red Hat (64-bit)`
   - Allocate at least **2GB RAM**
   - Set virtual hard disk: **20GB minimum**

4. **Install CentOS**  
   - Start the VM and follow the CentOS installation steps.

---

## 2. Installing Java

### 2.1 Remove OpenJDK (if installed)
```bash
sudo yum remove java-1.7.0-openjdk*
```

### 2.2 Download and Install Oracle JDK 7
```bash
sudo mkdir -p /usr/local/java
cd /usr/local/java
sudo tar xvzf jdk-7u40-linux-x64.tar.gz
sudo tar xvzf jre-7u40-linux-x64.tar.gz
```

### 2.3 Set Environment Variables
Edit `/etc/profile` and append:
```bash
# Java Environment Variables
export JAVA_HOME=/usr/local/java/jdk1.7.0_40
export JRE_HOME=/usr/local/java/jre1.7.0_40
export PATH=$PATH:$JAVA_HOME/bin:$JRE_HOME/bin
```
Load the updated profile:
```bash
source /etc/profile
```

---

## 3. Installing Hadoop 1.2.1 in "03. Hadoop" Directory

### 3.1 Create Directory and Extract Hadoop
```bash
mkdir -p ~/"03. Hadoop"
cd ~/"03. Hadoop"
tar xzf hadoop-1.2.1.tar.gz
```

### 3.2 Set Hadoop Environment Variables
Edit `/etc/profile` and add:
```bash
# Hadoop Environment Variables
export HADOOP_INSTALL=~/"03. Hadoop"/hadoop-1.2.1
export PATH=$PATH:$HADOOP_INSTALL/bin
```
Load the updated profile:
```bash
source /etc/profile
```

### 3.3 Configure SSH for Hadoop
```bash
sudo yum install -y openssh-server openssh-clients rsync
sudo systemctl enable sshd
sudo systemctl start sshd
ssh-keygen -t dsa -P "" -f ~/.ssh/id_dsa
cat ~/.ssh/id_dsa.pub >> ~/.ssh/authorized_keys
chmod 600 ~/.ssh/authorized_keys
ssh localhost
```

### 3.4 Configure Hadoop
```bash
cd $HADOOP_INSTALL/conf
```
Edit the following files:

- **core-site.xml**
  ```xml
  <configuration>
    <property>
      <name>fs.default.name</name>
      <value>hdfs://localhost:9000</value>
    </property>
  </configuration>
  ```

- **hdfs-site.xml**
  ```xml
  <configuration>
    <property>
      <name>dfs.replication</name>
      <value>1</value>
    </property>
  </configuration>
  ```

- **mapred-site.xml**
  ```xml
  <configuration>
    <property>
      <name>mapred.job.tracker</name>
      <value>localhost:9001</value>
    </property>
  </configuration>
  ```

Edit `hadoop-env.sh` and add:
```bash
export JAVA_HOME=/usr/local/java/jdk1.7.0_40
```

### 3.5 Format the Namenode & Start Hadoop
```bash
$HADOOP_INSTALL/bin/hadoop namenode -format
$HADOOP_INSTALL/bin/start-all.sh
```

---

## 4. Installing Hive 0.14 in "04.Hive" Directory

### 4.1 Create Directory and Extract Hive
```bash
mkdir -p ~/"04.Hive"
cd ~/"04.Hive"
tar xzf apache-hive-0.14.0-bin.tar.gz
```

### 4.2 Set Hive Environment Variables
Edit `/etc/profile` and add:
```bash
# Hive Environment Variables
export HIVE_HOME=~/"04.Hive"/apache-hive-0.14.0-bin
export PATH=$PATH:$HIVE_HOME/bin
```
Load the updated profile:
```bash
source /etc/profile
```

### 4.3 Configure Hive to Locate Hadoop
```bash
sudo vi $HIVE_HOME/bin/hive-config.sh
```
Add the following line:
```bash
export HADOOP_HOME=~/"03. Hadoop"/hadoop-1.2.1
```

### 4.4 Create Hive Warehouse Directory in HDFS
```bash
$HADOOP_INSTALL/bin/hadoop fs -mkdir /usr/hive/warehouse
$HADOOP_INSTALL/bin/hadoop fs -chmod 777 /usr/hive/warehouse
```

### 4.5 Start Hive
```bash
hive
```
If an error occurs, run:
```bash
$HADOOP_INSTALL/bin/hadoop fs -chmod 777 /tmp/hive
```

---

## 5. Restarting Hadoop and Hive After a System Reboot

```bash
$HADOOP_INSTALL/bin/start-all.sh
hive
```

---

## Congratulations!

You have successfully set up a pseudo-distributed Hadoop and Hive environment on CentOS, with Hadoop installed in the **03. Hadoop** folder and Hive installed in the **04.Hive** folder.
