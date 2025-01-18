Now will will leann some comment in Hadoop. Hadoop command are very similar to linux  command 
For example if you want to create  a folder  then type
hdfs dfs -mkdir /bootcamp

# Hadoop Part 1: HDFS Commands and Dataset Management

Welcome to **Hadoop Part 1**! In this section, we will install a dataset and explore basic HDFS commands. Let’s get started.

## Step 1: Start Hadoop

First, navigate to the Hadoop working directory and start all services:

```bash
cd hadoop-hdfs/play/
start-all.sh
```

## Step 2: List HDFS Root Directory

To check existing directories in HDFS, run:

````bash
[train@localhost big_data]$ cd hadoop-hdfs/play/

[train@localhost play]$ start-all.sh

## 1. ls lists 
```
[train@localhost play]$ hdfs dfs -ls /
Found 2 items
drwxrwxr-x   - train supergroup          0 2020-08-26 06:22 /tmp
drwxr-xr-x   - train supergroup          0 2020-08-22 08:40 /user
```

`/user` is home directory of users like `/home` in linux. In this case our hdfs home is `/user/train`

## 2. mkdir 
`[train@localhost play]$ hdfs dfs -mkdir /user/train/play-hdfs-commands`  

Now sort and see newly created folder.
```
[train@localhost play]$ hdfs dfs -ls -t /user/train
Found 10 items
drwxr-xr-x   - train supergroup          0 2020-09-15 04:49 /user/train/play-hdfs-commands
drwxr-xr-x   - train supergroup          0 2020-08-26 18:25 /user/train/.sparkStaging
drwxr-xr-x   - train supergroup          0 2020-08-26 18:14 /user/train/write_to_kafka
drwxr-xr-x   - train supergroup          0 2020-08-26 14:56 /user/train/read_from_kafka
drwxr-xr-x   - train supergroup          0 2020-08-26 11:31 /user/train/exactly_once_guarantee
drwxr-xr-x   - train supergroup          0 2020-08-25 20:47 /user/train/wordCountCheckpoint
drwxr-xr-x   - train supergroup          0 2020-08-22 08:15 /user/train/datasets
drwxr-xr-x   - train supergroup          0 2020-08-21 11:53 /user/train/output_data
drwxr-xr-x   - train supergroup          0 2020-07-23 22:07 /user/train/myHDFSFolder
-rw-r--r--   1 train supergroup       4556 2020-07-23 21:53 /user/train/copied.csv
```

## 3. put  
put copies files and folders from lokal to hdfs.  

# 4. mv  
move hdfs files/folder to another directory.

## 5. cp  
copies hdfs files/folders to another directory.

## 6. chown
changes ownership of file/folder.

## 7. chmod
changes access rights of file/folder.

## 8. get
downloads a file/folder form hdfs to local.

## 9. du
shows size of folder.

## 10. rm
deletes file/folder from hdfs.  
For folders `-r`  
For skipping trash `-skipTrash`  

## 11. head, tail, cat to read files.

## 12. hdfs environment variables  
```
[train@localhost play]$ hdfs envvars

JAVA_HOME='/usr/lib/jvm/java-1.8.0-openjdk-1.8.0.262.b10-0.el7_8.x86_64/jre/'
HADOOP_HDFS_HOME='/opt/manual/hadoop/'
HDFS_DIR='share/hadoop/hdfs'
HDFS_LIB_JARS_DIR='share/hadoop/hdfs/lib'
HADOOP_CONF_DIR='/opt/manual/hadoop/etc/hadoop'
HADOOP_TOOLS_HOME='/opt/manual/hadoop/'
HADOOP_TOOLS_DIR='share/hadoop/tools'
HADOOP_TOOLS_LIB_JARS_DIR='share/hadoop/tools/lib'
```

## 13. health check  
```
[train@localhost play]$ hdfs fsck /user/train
Connecting to namenode via http://localhost:9870/fsck?ugi=train&path=%2Fuser%2Ftrain
FSCK started by train (auth:SIMPLE) from /127.0.0.1 for path /user/train at Tue Sep 15 05:19:32 TRT 2020

Status: HEALTHY
 Number of data-nodes:  1
 Number of racks:               1
 Total dirs:                    249
 Total symlinks:                0

Replicated Blocks:
 Total size:    1001184061 B
 Total files:   4223
 Total blocks (validated):      4222 (avg. block size 237135 B)
 Minimally replicated blocks:   4222 (100.0 %)
 Over-replicated blocks:        0 (0.0 %)
 Under-replicated blocks:       0 (0.0 %)
 Mis-replicated blocks:         0 (0.0 %)
 Default replication factor:    1
 Average block replication:     1.0
 Missing blocks:                0
 Corrupt blocks:                0
 Missing replicas:              0 (0.0 %)

Erasure Coded Block Groups:
 Total size:    0 B
 Total files:   0
 Total block groups (validated):        0
 Minimally erasure-coded block groups:  0
 Over-erasure-coded block groups:       0
 Under-erasure-coded block groups:      0
 Unsatisfactory placement block groups: 0
 Average block group size:      0.0
 Missing block groups:          0
 Corrupt block groups:          0
 Missing internal blocks:       0
FSCK ended at Tue Sep 15 05:19:32 TRT 2020 in 281 milliseconds


The filesystem under path '/user/train' is HEALTHY
```

## 14. Fix underreplicated blocks
- Collect underreplicated blocks as a list into a file
```
hdfs fsck / | grep 'Under replicated' | awk -F':' '{print $1}' >> /tmp/under_replicated_files
```
- Fix to replication 1
```
for hdfsfile in `cat /tmp/under_replicated_files`; do echo "Fixing $hdfsfile :" ;  hadoop fs -setrep 1 $hdfsfile; done
```


````

Expected output:

```
Found 2 items
drwxrwxr-x   - centos9 supergroup          0 2024-01-18 06:22 /tmp
drwxr-xr-x   - centos9 supergroup          0 2024-01-18 08:40 /user
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
wget https://raw.githubusercontent.com/HuseynA28/Data-Engineering_Bootcamp/refs/heads/main/datasets/titanic.csv
```

Now, upload the dataset to HDFS:

```bash
hdfs dfs -put /home/centos9/datasets/titanic.csv /user/centos9/datasets/
```

Verify the upload:

```bash
hdfs dfs -ls /user/centos9/datasets/
```

## Step 5: Basic HDFS Commands

### 1. Copy Files to HDFS

```bash
hdfs dfs -put <local-path> <hdfs-path>
```

### 2. Move Files in HDFS

```bash
hdfs dfs -mv <source> <destination>
```

### 3. Copy Files in HDFS

```bash
hdfs dfs -cp <source> <destination>
```

### 4. Change File/Folder Ownership

```bash
hdfs dfs -chown user:group <path>
```

### 5. Modify Access Permissions

```bash
hdfs dfs -chmod <permissions> <path>
```

### 6. Download Files from HDFS

```bash
hdfs dfs -get <hdfs-path> <local-path>
```

### 7. Check Folder Size

```bash
hdfs dfs -du -h <path>
```

### 8. Delete Files/Folders from HDFS

For files:

```bash
hdfs dfs -rm <path>
```

For folders:

```bash
hdfs dfs -rm -r <path>
```

To skip trash:

```bash
hdfs dfs -rm -skipTrash <path>
```

### 9. Read Files in HDFS

```bash
hdfs dfs -cat <path>
```

### 10. HDFS Environment Variables

To check your environment variables:

```bash
hdfs envvars
```

Example output:

```
JAVA_HOME='/usr/lib/jvm/java-1.8.0-openjdk/'
HADOOP_HDFS_HOME='/opt/manual/hadoop/'
HDFS_DIR='share/hadoop/hdfs'
```

### 11. Check HDFS Health

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

### 12. Fix Under-Replicated Blocks

To list under-replicated blocks:

```bash
hdfs fsck / | grep 'Under replicated' | awk -F':' '{print $1}' >> /tmp/under_replicated_files
```

To fix replication:

```bash
for hdfsfile in `cat /tmp/under_replicated_files`; do echo "Fixing $hdfsfile :" ;  hadoop fs -setrep 1 $hdfsfile; done
```

## Summary of Commands

| Command                                | Description                       |
| -------------------------------------- | --------------------------------- |
| `hdfs dfs -ls /`                       | List directories in HDFS root     |
| `hdfs dfs -mkdir <path>`               | Create a new directory in HDFS    |
| `hdfs dfs -put <local> <hdfs>`         | Upload files to HDFS              |
| `hdfs dfs -mv <source> <dest>`         | Move files in HDFS                |
| `hdfs dfs -cp <source> <dest>`         | Copy files in HDFS                |
| `hdfs dfs -chown user:group <path>`    | Change file ownership             |
| `hdfs dfs -chmod <permissions> <path>` | Change file permissions           |
| `hdfs dfs -get <hdfs> <local>`         | Download files from HDFS          |
| `hdfs dfs -du -h <path>`               | Show directory size               |
| `hdfs dfs -rm <path>`                  | Delete files/folders from HDFS    |
| `hdfs dfs -cat <path>`                 | Read files in HDFS                |
| `hdfs envvars`                         | Show Hadoop environment variables |
| `hdfs fsck /user/centos9`              | Check HDFS health                 |
| `hadoop fs -setrep 1 <path>`           | Fix under-replicated blocks       |

Now you are ready to manage files and directories in Hadoop efficiently! 🚀



