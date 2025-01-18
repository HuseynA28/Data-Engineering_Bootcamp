# Hadoop Part 1: Installing and Uploading Titanic Dataset

Welcome to **Hadoop Part 1**! In this section, we will install the dataset and work with it in Hadoop. Let’s get started.


Create the Parent Directory:

bash
Copy
Edit
hdfs dfs -mkdir -p /user/centos9
This command creates the /user/centos9 directory in HDFS, including any necessary parent directories.

Create the datasets Directory:

bash
Copy
Edit
hdfs dfs -mkdir /user/centos9/datasets
After creating the parent directory, this command creates the datasets directory within /user/centos9.

Verify the Directory Structure:

bash
Copy
Edit
hdfs dfs -ls /user/centos9

## Step 1: Create a Folder for Datasets

First, create a folder named `datasets` in the `/home/centos9/` directory. Then navigate to this folder:

```bash
mkdir -p /home/centos9/datasets
cd /home/centos9/datasets
```

## Step 2: Download the Titanic Dataset

Download the Titanic dataset using the `wget` command:

```bash
wget https://raw.githubusercontent.com/HuseynA28/Data-Engineering_Bootcamp/refs/heads/main/datasets/titanic.csv
```

This will download the **titanic.csv** file into your `datasets` folder.

## Step 3: Create a Directory in HDFS

To store and process datasets in Hadoop, create a directory in HDFS:

```bash
hdfs dfs -mkdir /user/centos9/datasets
```

This command creates a new directory named `datasets` in your HDFS user directory.

## Step 4: Upload Dataset to HDFS

Now, upload the downloaded `titanic.csv` file from your local file system to HDFS using:

```bash
hdfs dfs -put /home/centos9/datasets/titanic.csv /user/centos9/datasets/
```

This command copies the `titanic.csv` file from your local machine to HDFS inside the `datasets` directory.

## Step 5: Verify the Upload

To ensure the file has been successfully uploaded, list the contents of the `datasets` directory in HDFS:

```bash
hdfs dfs -ls /user/centos9/datasets/
```

You should see the `titanic.csv` file in the output.

---



