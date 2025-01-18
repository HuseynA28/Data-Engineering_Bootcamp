# Hadoop Part 1: HDFS Commands and Dataset Management

Welcome to **Hadoop Part 1**! In this section, we will install a dataset and explore basic HDFS commands. Let’s get started.

## Introduction to Hadoop Commands

Hadoop commands are very similar to Linux commands. If you are already familiar with Linux, you will find Hadoop commands easy to understand. For example, creating a directory in Hadoop is similar to Linux:

```bash
hdfs dfs -mkdir /bootcamp
```

This command creates a directory named `bootcamp` in the HDFS file system.

## Step 1: Start Hadoop

First, navigate to the Hadoop working directory and start all services:

```bash
start-all.sh
```

To start only HDFS and YARN separately:

```bash
start-dfs.sh
start-yarn.sh
```

To stop all services:

```bash
stop-all.sh
```

## Step 2: List HDFS Root Directory

To check existing directories in HDFS, run:

```bash
hdfs dfs -ls /
```

Expected output:

```
Found 2 items
drwxrwxr-x   - centos9 supergroup          0 2025-01-18 06:22 /tmp
drwxr-xr-x   - centos9 supergroup          0 2025-01-18 08:40 /user
```

The `/user` directory is the home directory for users, similar to `/home` in Linux. Your HDFS home is `/user/centos9`.

## Step 3: Create a Directory in HDFS

To create a new directory inside your HDFS home:

```bash
hdfs dfs -mkdir /user/centos9/play-hdfs-commands
```

You can now sort and check the newly created folder:

```bash
hdfs dfs -ls -t /user/centos9
```

## Step 4: Upload Dataset to HDFS

Download the Titanic dataset locally:

```bash
mkdir -p /home/centos9/datasets
cd /home/centos9/datasets
wget https://raw.githubusercontent.com/HuseynA28/Data-Engineering_Bootcamp/main/datasets/titanic.csv
```

Now, upload the dataset to HDFS:

```bash
hdfs dfs -put /home/centos9/datasets/titanic.csv /user/centos9/datasets/
```

Verify the upload:

```bash
hdfs dfs -ls /user/centos9/datasets/
```

You can also copy the file from Hadoop HDFS to your local folder with `get`:

```bash
hdfs dfs -get /user/centos9/datasets/titanic.csv .
```

## Step 5: Common HDFS Commands Explained

| Command | Description | Example |
|---------|-------------|---------|
| `hdfs dfs -ls <path>` | List files and directories in HDFS | `hdfs dfs -ls /user/centos9/` |
| `hdfs dfs -mkdir <path>` | Create a new directory in HDFS | `hdfs dfs -mkdir /user/centos9/new_folder` |
| `hdfs dfs -put <local> <hdfs>` | Upload files to HDFS | `hdfs dfs -put localfile.txt /user/centos9/` |
| `hdfs dfs -get <hdfs> <local>` | Download files from HDFS | `hdfs dfs -get /user/centos9/file.txt .` |
| `hdfs dfs -mv <source> <dest>` | Move files in HDFS | `hdfs dfs -mv /user/centos9/file1 /user/centos9/archive/` |
| `hdfs dfs -cp <source> <dest>` | Copy files in HDFS | `hdfs dfs -cp /user/centos9/file1 /user/centos9/copy/` |
| `hdfs dfs -rm <path>` | Delete files/folders from HDFS | `hdfs dfs -rm /user/centos9/file.txt` |
| `hdfs dfs -rm -r <path>` | Delete a directory from HDFS | `hdfs dfs -rm -r /user/centos9/old_folder` |
| `hdfs dfs -du -h <path>` | Show directory size | `hdfs dfs -du -h /user/centos9/` |
| `hdfs dfs -cat <path>` | Read a file in HDFS | `hdfs dfs -cat /user/centos9/file.txt` |
| `hdfs dfs -tail <path>` | View the last 1KB of a file | `hdfs dfs -tail /user/centos9/file.txt` |
| `hdfs dfs -head <path>` | View the first 1KB of a file | `hdfs dfs -head /user/centos9/file.txt` |
| `hdfs dfs -touchz <path>` | Create an empty file | `hdfs dfs -touchz /user/centos9/newfile.txt` |
| `hdfs dfs -test -e <path>` | Check if a file exists | `hdfs dfs -test -e /user/centos9/file.txt && echo Exists` |
| `hdfs dfsadmin -report` | Show HDFS cluster report | `hdfs dfsadmin -report` |
| `hdfs fsck <path>` | Check HDFS health | `hdfs fsck /user/centos9` |

## Step 6: Check HDFS Health

To check the status of your HDFS file system, run:

```bash
hdfs fsck /user/centos9
```

Expected output:

```
Status: HEALTHY
Number of data-nodes:  1
Missing blocks: 0
Corrupt blocks: 0
```

## Step 7: Fix Under-Replicated Blocks

Sometimes, blocks in HDFS may become under-replicated. You can fix them by setting the replication factor to 1:

```bash
hdfs fsck / | grep 'Under replicated' | awk -F':' '{print $1}' >> /tmp/under_replicated_files
```

To set replication:

```bash
for hdfsfile in $(cat /tmp/under_replicated_files); do echo "Fixing $hdfsfile :" ; hdfs dfs -setrep 1 $hdfsfile; done
```

