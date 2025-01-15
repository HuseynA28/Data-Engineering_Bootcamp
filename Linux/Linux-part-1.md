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
- **Navigate Using Relative Paths**:
  ```bash
  cd ../Documents
  ```
  Moves to the `Documents` folder relative to the current directory.

---

## Viewing Command History

Use the `history` command to see previously executed commands:
```bash
history 5
```
Displays the last 5 commands.

To rerun a specific command:
```bash
!<command_number>
```
For example:
```bash
!42
```
Reruns the 42nd command from the history list.

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
- **Vim**: A powerful text editor.
  ```bash
  vim file.txt
  ```
  - Press `i` to enter insert mode.
  - Make changes, then press `Esc`.
  - Save and exit with `:wq`.
  - Quit without saving with `:q!`.

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
- Display content with line numbers:
  ```bash
  cat -n file.txt
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

### `tail` (Last Few Lines)
- Display last 10 lines:
  ```bash
  tail file.txt
  ```
- Display last 5 lines:
  ```bash
  tail -n 5 file.txt
  ```
- Monitor file updates in real-time:
  ```bash
  tail -f file.txt
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
- Check disk usage for all files in a directory:
  ```bash
  du -h /path/to/directory
  ```

---

## Sorting and Filtering

### Sort Files or Lines
- Reverse order:
  ```bash
  ls | sort -r
  ```
- Sort by the second column in a file:
  ```bash
  cat users | sort -k 2
  ```
- Sort numerically:
  ```bash
  sort -n numbers.txt
  ```

### Find Unique Lines
- Find unique lines:
  ```bash
  sort users.txt | uniq
  ```
- Alternative:
  ```bash
  sort -u users.txt
  ```

### Show Duplicated Values
- Find duplicated lines:
  ```bash
  sort rome.txt | uniq -d
  ```

---

## Filter Lines

### Using `grep`
- Filter lines containing a specific pattern:
  ```bash
  grep -F "pattern" file.txt
  ```
- Case-insensitive search:
  ```bash
  grep -i "pattern" file.txt
  ```
- Display line numbers with matches:
  ```bash
  grep -n "pattern" file.txt
  ```

---

## Using Environment Variables

The logic of variables in Linux is similar to other programming languages like Python. You assign values to variables for use in commands or scripts.

### Defining Variables
Assign a value to a variable:
```bash
my_name=Yourname
```
Print the value of the variable:
```bash
echo "${my_name}"
```

### Accessing System Variables
System variables can be accessed similarly:
```bash
echo "$PATH"
```
> Avoid using `echo $PATH` directly without quotes to prevent potential issues.

---

### Types of Environment Variables

#### Global Variables
Global variables are available system-wide and can be accessed by all processes or scripts started by the shell.
```bash
export MY_VAR="Hello, World"
```
Subsequent shells or scripts can access `MY_VAR` as an environment variable.

#### Local Variables
Local variables are limited to the current shell session or script.
```bash
MY_VAR="Local Variable"
echo "$MY_VAR"
```

| Aspect          | Global Variable        | Local Variable        |
|-----------------|------------------------|------------------------|
| **Scope**       | Available to all child processes | Limited to the shell session or script |
| **Declaration** | Declared with `export` | Declared without `export` |
| **Inheritance** | Inherited by subshells and processes | Not inherited |

### Listing and Managing Environment Variables

#### List All Variables
List global environment variables:
```bash
env
```

#### Access Variable Values
For example, get the current working directory:
```bash
echo "${PWD}"
```

#### Adding Directories to `PATH`
Update the `PATH` so the system can locate programs in a custom directory:
```bash
export PATH=$PATH:~/bin
```

Make the change permanent by editing `~/.bashrc`:
```bash
nano ~/.bashrc
```
Add the line:
```bash
PATH="${PATH}:/home/username/bin"
```
Reload the shell configuration:
```bash
source ~/.bashrc
```

#### Find Variables with `grep`
Search for specific variables:
```bash
env | grep PATH
```

#### Deleting Variables
Unset a variable:
```bash
unset MY_VAR
```

---

## Commit Commands

In Linux, if you type a variable name without assigning a value, the system considers it as a command. The shell will attempt to execute the "command" by searching for it in directories listed in the `PATH` environment variable:

```bash
echo "${PATH}"
/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/
```

The shell searches each directory in the `PATH` until it finds the command. If the command is not found, it either does not exist or the file/folder is not executable.

### Example: Creating and Running a Script

1. **Create a Script**
   ```bash
   nano my_script.sh
   ```
   Add the following content:
   ```bash
   #!/bin/bash
   echo "Hello, World!"
   ```
   The first line (`#!/bin/bash`) specifies the interpreter (in this case, Bash) to execute the script.

2. **Save and Exit**
   In nano, press `Ctrl + O`, then `Enter`, and then `Ctrl + X` to save and exit.

3. **Make the Script Executable**
   ```bash
   chmod +x my_script.sh
   ```

4. **Run the Script**
   ```bash
   ./my_script.sh
   ```

5. **Optional: Add to PATH**
   To execute the script from anywhere:
   ```bash
   mv my_script.sh /usr/local/bin/
   ```
   Now you can run it simply by typing:
   ```bash
   my_script.sh
   ```

---

## Commands on Files and Folders

- **Create a Directory**:
  ```bash
  mkdir my_folder
  ```
- **Create a File**:
  ```bash
  touch myfile.txt
  ```
- **Write to a File**:
  ```bash
echo "hello" > myfile.txt
  ```
- **Append Text to a File**:
  ```bash
echo "appendme" >> myfile.txt
  ```

- **Remove a File**:
  ```bash
  rm file.txt
  ```
- **Copy a File**:
  ```bash
  cp file.txt /path/to/destination/
  ```
- **Copy a Directory Recursively**:
  ```bash
  cp -R folder /path/to/destination/
  ```
- **Copy multiple files**:
  ```bash
  cp -r myfile* myfolder/
  ```
  It will copy all the files starting with `myfile` to `myfolder`.

- **Remove an Empty Directory**:
  ```bash
  rmdir empty_folder/
  ```
- **Remove a Directory and Its Contents**:
  ```bash
  rm -r folder/
  ```

- **Rename**:
  ```bash
  mv myfile yourfile
  ```
- **Rename while copying**:
  ```bash
  cp -v myfile myfolder/myfile_copy
  ```
- **Move**:
  ```bash
  mv myfile myfolder/
  ```
  Move multiple files/folders in one command:
  ```bash
  mv myfile1 myfile2 myfile3 destination_folder
  ```

### Advanced Example
To copy specific files matching patterns:
```bash
cp Purchasing/0[1-2]*/*.{pdf,xlsx} myfile
```
This command copies all `.pdf` and `.xlsx` files from subdirectories matching `01` and `02` to `myfile`.

---

By practicing these commands, you will build a strong foundation in Linux, an essential skill for Data Engineering.

