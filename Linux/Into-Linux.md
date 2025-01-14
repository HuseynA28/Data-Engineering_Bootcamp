# Intro to Linux for Data Engineering

Linux is a well-known open-source operating system widely used by companies as a server due to its stability and reliability. Many popular platforms, such as Android, are developed on Linux. For Data Engineering, you don't need to learn advanced Linux kernel functions. However, mastering basic commands is essential. Installing a Linux OS, such as Ubuntu, is a great starting point. Go for it!

---

## Getting Started with Linux Commands

Linux commands allow you to interact with the operating system through a terminal, a text-based interface where you type commands to perform tasks. Though it might seem intimidating initially, it is powerful and efficient once you get the hang of it.

### Listing Files and Directories

One of the most common tasks is viewing files and folders in your system. The `ls` command is particularly useful.

#### Basic `ls` Command
```bash
ls
```
Displays all files and directories in the current working directory.

#### List Files in the Root Directory
```bash
ls /
```
Shows all files and directories in the root directory (`/`).

#### List Files in the Home Directory
```bash
ls ~
```
Displays the contents of your home directory, such as `Documents`, `Downloads`, and `Pictures`.

#### List All Files (Including Hidden Files)
```bash
ls -a
```
Reveals all files, including hidden ones (files starting with a dot `.`).

### Additional `ls` Options
The `ls` command becomes more powerful with options. Here are some common ones:

| Option | Description |
|--------|-------------|
| `-l`   | Long format. Displays detailed file information, including permissions, ownership, size, and modification time. |
| `-a`   | Shows all files, including hidden ones. |
| `-h`   | Displays file sizes in human-readable formats (e.g., KB, MB). |
| `-R`   | Lists contents of directories recursively, including subdirectories. |
| `-t`   | Sorts files by modification time, with the newest first. |
| `-r`   | Reverses the order of the output. |
| `-1`   | Lists one file per line. |
| `-d`   | Lists directories themselves, not their contents. |
| `-F`   | Appends a character to filenames indicating their type (e.g., `/` for directories, `*` for executables). |
| `-L`   | Follows symbolic links to list the actual file or directory. |
| `-X`   | Sorts files alphabetically by their extension. |

#### Combining Options
Combine multiple options to customize the output:
```bash
ls -lh
```
Displays files in a long format with human-readable file sizes.

---

## Understanding File Details in Linux

Using the `ls -l` command, you get detailed information about files. Example:
```bash
-rw-r--r--  1 root root  0 Jan  2 15:48 output.txt
```

### Breakdown:
1. **`-rw-r--r--`**: File permissions.
   - `-`: Regular file.
   - `rw-`: Owner has read and write permissions.
   - `r--`: Group has read permission.
   - `r--`: Others have read permission.
2. **`1`**: Number of hard links.
3. **`root root`**: Owner and group of the file.
4. **`0`**: File size in bytes.
5. **`Jan  2 15:48`**: Last modification date and time.
6. **`output.txt`**: File name.

---

## Navigating Directories with `cd`

The `cd` (change directory) command lets you navigate through folders.

### Examples:
- **Root Directory**:
  ```bash
  cd /
  ```
- **Parent Directory**:
  ```bash
  cd ..
  ```
- **Home Directory**:
  ```bash
  cd ~
  ```
- **Specific Path**:
  ```bash
  cd /home/user/Desktop
  ```

---

## Viewing Command History

Use the `history` command to see previously executed commands:
```bash
history 5
```
Displays the last 5 commands.

---

## Using Aliases

Aliases let you create shortcuts for commands.
- **Temporary Alias**:
  ```bash
  alias folder_list='ls'
  ```
  Typing `folder_list` will run the `ls` command.
- **Permanent Alias**:
  Add the alias to `~/.bashrc`:
  ```bash
  nano ~/.bashrc
  ```
  Add:
  ```bash
  alias folder_list='ls'
  ```
  Save and reload:
  ```bash
  source ~/.bashrc
  ```

---

## File Editing and Standard Streams

### File Editors
- **Nano**: Simple text editor.
  ```bash
  nano file.txt
  ```

### Redirection Operators
- **Overwrite**:
  ```bash
  echo "hello" > output.txt
  ```
- **Append**:
  ```bash
  echo "new line" >> output.txt
  ```

---

## Viewing File Content

### `cat` (Concatenate and Display Files)
- Display content:
  ```bash
  cat file.txt
  ```
- Combine files:
  ```bash
  cat file1.txt file2.txt > combined.txt
  ```

### `less` (View Files Page by Page)
- Open a file:
  ```bash
  less file.txt
  ```
  - **Navigation**:
    - Forward search: `/search_term`
    - Backward search: `?search_term`
    - Quit: `q`

### `head` (First Few Lines)
- Display first 10 lines:
  ```bash
  head file.txt
  ```
- Display first 5 lines:
  ```bash
  head -n 5 file.txt
  ```

### `wc` (Word Count)
- Count lines, words, and characters:
  ```bash
  wc file.txt
  ```
- Options:
  - `-l`: Count lines.
  - `-w`: Count words.
  - `-c`: Count bytes.

### `du` (Disk Usage)
- Check disk usage:
  ```bash
  du file.txt
  ```
- Human-readable format:
  ```bash
  du -h file.txt
  ```

---


## Using environmental variables 

What are environment variables: Used to store configuration information and settings . Environment variables are written in uppercase letters
We can list all of them with the following command:
env
Example (to be preferred):

echo "${PWD}"
echo "${USER}"
echo "${PATH}"
We can also use:

echo "$PATH"
We should avoid:

echo $PATH
