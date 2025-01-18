# Installing Hadoop on CentOS: A Step-by-Step Guide

Hadoop is an open-source framework for distributed data storage and processing. Follow this guide to install and configure Hadoop on CentOS.

## Step 1: Install Java Development Kit (JDK)

Hadoop requires Java to run. Install the latest OpenJDK:

```bash
sudo yum update -y && sudo yum install -y java-11-openjdk-devel
```

Verify the installation:

```bash
java -version
```

## Step 2: Install SSH

Hadoop uses SSH (Secure Shell) for communication between nodes. Install and enable it:

```bash
sudo yum install -y openssh-server openssh-clients
sudo systemctl enable sshd
sudo systemctl start sshd
```

To check the SSH service status:

```bash
sudo systemctl status sshd
```

## Step 3: Create a Hadoop User

To manage Hadoop efficiently, create a dedicated user:

```bash
sudo useradd -m -d /home/centos9 -s /bin/bash centos9
```

Set a password for the centos9 user:

```bash
sudo passwd centos9
```

Give Hadoop sudo privileges (optional):

```bash
sudo usermod -aG wheel hadoop
```

## Step 4: Switch to the Hadoop User

```bash
su - hadoop
```

## Step 5: Configure SSH (Password-less Access)

Generate an SSH key for the Hadoop user:

```bash
ssh-keygen -t rsa -b 4096
```

Press Enter for the default location (~/.ssh/id_rsa). Press Enter again if you don’t want a passphrase.

Add the generated key to authorized keys:

```bash
cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys
chmod 640 ~/.ssh/authorized_keys
```

Verify SSH connection:

```bash
ssh localhost
```

If prompted, type `yes` to continue.

## Step 6: Install Hadoop

Download the latest Hadoop version:

```bash
wget https://dlcdn.apache.org/hadoop/common/hadoop-3.3.6/hadoop-3.3.6.tar.gz
```

Extract the downloaded file:

```bash
tar -xvzf hadoop-3.3.6.tar.gz
```

Move it to a simpler location:

```bash
mv hadoop-3.3.6 hadoop
```

## Step 7: Configure Environment Variables

Edit the `~/.bashrc` file:

```bash
nano ~/.bashrc
```

Add the following lines at the end:

```bash
export JAVA_HOME=/usr/lib/jvm/java-11-openjdk
export HADOOP_HOME=/home/hadoop/hadoop
export HADOOP_INSTALL=$HADOOP_HOME
export HADOOP_MAPRED_HOME=$HADOOP_HOME
export HADOOP_COMMON_HOME=$HADOOP_HOME
export HADOOP_HDFS_HOME=$HADOOP_HOME
export HADOOP_YARN_HOME=$HADOOP_HOME
export HADOOP_COMMON_LIB_NATIVE_DIR=$HADOOP_HOME/lib/native
export PATH=$PATH:$HADOOP_HOME/sbin:$HADOOP_HOME/bin
export HADOOP_OPTS="-Djava.library.path=$HADOOP_HOME/lib/native"
```

Save the file (`Ctrl + X`, then `Y`, then `Enter`).

Apply the changes:

```bash
source ~/.bashrc
```

Now, edit `hadoop-env.sh`:

```bash
nano $HADOOP_HOME/etc/hadoop/hadoop-env.sh
```

Find the line that starts with `export JAVA_HOME` and update it to:

```bash
export JAVA_HOME=/usr/lib/jvm/java-11-openjdk
```

## Step 8: Configure Hadoop

Create directories for Hadoop storage:

```bash
mkdir -p ~/hadoopdata/hdfs/{namenode,datanode}
```

Edit `core-site.xml`

```bash
nano $HADOOP_HOME/etc/hadoop/core-site.xml
```

Add:

```xml
<configuration>
    <property>
        <name>fs.defaultFS</name>
        <value>hdfs://localhost:9000</value>
    </property>
</configuration>
```

Edit `hdfs-site.xml`

```bash
nano $HADOOP_HOME/etc/hadoop/hdfs-site.xml
```

Add:

```xml
<configuration>
    <property>
        <name>dfs.replication</name>
        <value>1</value>
    </property>
    <property>
        <name>dfs.namenode.name.dir</name>
        <value>file:///home/hadoop/hadoopdata/hdfs/namenode</value>
    </property>
    <property>
        <name>dfs.datanode.data.dir</name>
        <value>file:///home/hadoop/hadoopdata/hdfs/datanode</value>
    </property>
</configuration>
```

Edit `mapred-site.xml`

```bash
nano $HADOOP_HOME/etc/hadoop/mapred-site.xml
```

Add:

```xml
<configuration>
    <property>
        <name>mapreduce.framework.name</name>
        <value>yarn</value>
    </property>
</configuration>
```

Edit `yarn-site.xml`

```bash
nano $HADOOP_HOME/etc/hadoop/yarn-site.xml
```

Add:

```xml
<configuration>
    <property>
        <name>yarn.nodemanager.aux-services</name>
        <value>mapreduce_shuffle</value>
    </property>
</configuration>
```

## Step 9: Format Hadoop NameNode

Before starting Hadoop, format the NameNode:

```bash
hdfs namenode -format
```

## Step 10: Start Hadoop

Start all Hadoop services:

```bash
start-dfs.sh
start-yarn.sh
```

Check if services are running:

```bash
jps
```

You should see:

- NameNode
- DataNode
- ResourceManager
- NodeManager
- SecondaryNameNode

## Step 11: Access Hadoop Web UI

Find your system’s IP:

```bash
ip addr show
```

Then, open these URLs in your browser:

- Hadoop NameNode UI: `http://your-ip:9870`
- YARN Resource Manager UI: `http://your-ip:8088`

Replace `your-ip` with your actual IP address.

## Step 12: Test Hadoop HDFS

Create directories in HDFS:

```bash
hdfs dfs -mkdir /test1
hdfs dfs -mkdir /logs
```

List HDFS directories:

```bash
hdfs dfs -ls /
```

Move files to HDFS:

```bash
hdfs dfs -put /var/log/* /logs/
```

Check if files are stored:

```bash
hdfs dfs -ls /logs/
```

## Step 13: Stop Hadoop

When finished, stop Hadoop services:

```bash
stop-dfs.sh
stop-yarn.sh
```

## Conclusion

You have successfully installed and configured Hadoop on CentOS! 🎉

Now, you can use Hadoop for big data storage and processing. Let me know if you need further guidance! 🚀
