# Intro to Linux for Data Engineering

Linux is a well-known open-source system used by most companies as a server due to its stability and reliability. Many popular platforms, such as Android, are developed on the Linux operating system. For Data Engineering, you don't need to learn advanced Linux kernel functions. However, learning some basic commands is sufficient. If you'd like to install a Linux OS such as Ubuntu, it would be a great decision. Go for it!

---

## Getting Started with Linux Commands

Linux commands are tools that allow you to interact with the operating system through a terminal. The terminal is a text-based interface where you can type commands to perform various tasks. This might sound intimidating at first, but once you get the hang of it, you'll find it very powerful and efficient.

### Listing Files and Directories

One of the most common tasks you'll perform is viewing the files and folders in your system. For this, the `ls` command is incredibly useful.

#### Basic `ls` Command:

```bash
ls
```

This command displays all files and directories in the current working directory. For example, if you're in your `Documents` folder, it will show you the contents of that folder.

#### List Files in the Root Directory:

```bash
ls /
```

The root directory (`/`) is the top-most directory in Linux. Running this command will display all the files and directories located at the root level of your file system.

#### List Files in the Home Directory:# Intro to Linux for Data Engineering&#xD;

####



Linux is a well-known open-source system used by most companies as a server due to its stability and reliability. Many popular platforms, such as Android, are developed on the Linux operating system. For Data Engineering, you don't need to learn advanced Linux kernel functions. However, learning some basic commands is sufficient. If you'd like to install a Linux OS such as Ubuntu, it would be a great decision. Go for it!



\---



\## Getting Started with Linux Commands



Linux commands are tools that allow you to interact with the operating system through a terminal. The terminal is a text-based interface where you can type commands to perform various tasks. This might sound intimidating at first, but once you get the hang of it, you'll find it very powerful and efficient.



\### Listing Files and Directories



One of the most common tasks you'll perform is viewing the files and folders in your system. For this, the \`ls\` command is incredibly useful.



\#### Basic \`ls\` Command:

\`\`\`bash

ls

\`\`\`

This command displays all files and directories in the current working directory. For example, if you're in your \`Documents\` folder, it will show you the contents of that folder.



\#### List Files in the Root Directory:

\`\`\`bash

ls /

\`\`\`

The root directory (\`/\`) is the top-most directory in Linux. Running this command will display all the files and directories located at the root level of your file system.



\#### List Files in the Home Directory:

\`\`\`bash

ls \~

\`\`\`

The home directory is where your personal files and folders are stored. Use this command to see what’s in your home folder. For example, it might contain directories like \`Documents\`, \`Downloads\`, and \`Pictures\`.



\#### List All Files (Including Hidden Files):

\`\`\`bash

ls -a

\`\`\`

By default, files that start with a dot (\`.\`) are hidden. This command reveals all files, including hidden ones, in the directory.



\---



\### Additional \`ls\` Options



The \`ls\` command becomes even more powerful when combined with options. Options are like modifiers that change how the command behaves.



\| Option | Description |

\|--------|-------------|

\| \`-l\`   | Long format. Displays detailed file information, including permissions, ownership, size, and modification time. For example, this is helpful when you need to check who owns a file or when it was last modified. |

\| \`-a\`   | Shows all files, including hidden ones. |

\| \`-h\`   | Displays file sizes in human-readable formats (e.g., KB, MB) when combined with \`-l\`. This is especially useful for understanding file sizes at a glance. |

\| \`-R\`   | Lists contents of directories recursively, including subdirectories. This means you can see not only the files in the current directory but also everything inside its subdirectories. |

\| \`-t\`   | Sorts files by modification time, with the newest first. Use this to quickly find the most recently updated files. |

\| \`-r\`   | Reverses the order of the output. For example, when combined with \`-t\`, it will list the oldest files first. |

\| \`-1\`   | Lists one file per line instead of displaying them in columns. This can make the output easier to read in some cases. |

\| \`-d\`   | Lists directories themselves, not their contents. Use this to see only the directories without diving into them. |

\| \`-F\`   | Appends a character to filenames indicating their type (e.g., \`/\` for directories, \`\*\` for executables). This gives you more context about the files at a glance. |

\| \`-L\`   | Follows symbolic links and lists the actual file or directory they point to. Symbolic links are like shortcuts to other files or directories. |

\| \`-X\`   | Sorts files alphabetically by their extension. For example, files ending in \`.txt\` will be grouped together. |



\---



\### Pro Tip:

You can combine multiple options to customize the output further. For example, the command:

\`\`\`bash

ls -lh

\`\`\`

will display the files in a long format with human-readable file sizes.



Learning these basic commands will set a strong foundation for your journey in Data Engineering. The more you practice, the more comfortable you’ll become with navigating Linux systems!



\---



\## Understanding File Details in Linux



When you list files in a long format using the \`ls -l\` command, you get detailed information about each file. Here is an example output:

\`\`\`bash

-rw-r--r--  1 root root         0 Jan  2 15:48 outout.txt

-rw-r--r--  1 root root        12 Jan  5 00:09 output.txt

-rw-r--r--  1 root root        15 Jan  2 15:42 output.txx

-rwxr-xr-x  1 root root    169360 Jan  2 15:09 romeo.txt

drwx------  3 root root      4096 Nov 29 19:22 snap

\`\`\`



Let’s break down the first line:

\`\`\`bash

-rw-r--r--  1 root root         0 Jan  2 15:48 outout.txt

\`\`\`



\### Explanation:

1\. \*\*\`-rw-r--r--\`\*\*: This represents the file's permissions.

&#x20;  \- The first character indicates the type of file:

&#x20;    \- \`-\` means it is a regular file.

&#x20;    \- \`d\` means it is a directory.

&#x20;    \- \`l\` means it is a symbolic link.

&#x20;  \- The next three characters (\`rw-\`) indicate the owner's permissions:

&#x20;    \- \`r\`: Read permission.

&#x20;    \- \`w\`: Write permission.

&#x20;    \- \`-\`: No execute permission.

&#x20;  \- The next three characters (\`r--\`) indicate the group’s permissions.

&#x20;  \- The last three characters (\`r--\`) indicate permissions for others.



2\. \*\*\`1\`\*\*: This is the number of hard links to the file.



3\. \*\*\`root root\`\*\*: These are the owner and group of the file.



4\. \*\*\`0\`\*\*: This is the size of the file in bytes.



5\. \*\*\`Jan  2 15:48\`\*\*: This is the last modification date and time of the file.



6\. \*\*\`outout.txt\`\*\*: This is the name of the file.



By understanding these details, you can gather important information about files, such as their type, size, permissions, and last modification date.



\---



\## Navigating Directories with \`cd\`



The \`cd\` command (short for "change directory") allows you to navigate between folders in your file system.



\### Absolute Path:

An absolute path specifies the complete path to a file or directory from the root directory (\`/\`).



\#### Example:

\`\`\`bash

cd /home/huseyn/Desktop

\`\`\`

This command navigates directly to the \`Desktop\` folder using the full path from the root directory.



\### Relative Path:

A relative path specifies the location of a file or directory in relation to the current working directory.



\#### Example:

\`\`\`bash

cd \~/Desktop

\`\`\`

The \`\~\` symbol is shorthand for the home directory. This command navigates to the \`Desktop\` folder relative to the user's home directory.



With \`cd\`, you can move efficiently through your directory structure, whether using absolute or relative paths.



\`cd /\`      move to root directory &#x20;

\`cd ..\`     move one level upper directory &#x20;

\`cd ../..\`  move two level upper directory &#x20;

\`cd \~\`      move to home directory &#x20;



\##  Look at the hisory at command line&#x20;

history {number of the last commed comat }

if you type history  5  it fill print the last commed 5 comand&#x20;



\## alias

Alias is used give  new name some commadn you can yous the alias . Such as I want ls give new name folder\_list

alias folder\_list='ls' / When i type folder\_list teh it do the same as ls . But it temporal  it will be deleted after the session ends.

If you would like to save and use use always&#x20;

alias will be removed with session. If you need a constant alias you need to edit \~/.bashrc file



nano \~/.bashrc

add alias command to file and save it after that enter source command

source \~/.bashrc



\# File Editing and Standard Streams







\- nano\* - A simple text editor for creating or editing files.



\- Open or create a file: \`nano file.txt\`

-Write to File (\`>\`): - Overwrites the content of a file.



&#x20;Write text to a file: \`echo "hello" > output.txt\`

\- Save command output to a file: \`ls > output.txt\`

Append to File (\`>>\`):- Adds content to the end of a file.



\- Append text to a file: \`echo "new line" >> output.txt\`





\## \`cat\` (Concatenate and Display Files)



-Command:\`cat file.txt\`

&#x20;   \- Used to view the content of a file, concatenate multiple files, or create a file.



&#x20;      &#x20;

&#x20;       \`\`\`bash

&#x20;       cat file1.txt file2.txt > combined.txt

&#x20;      &#x20;

&#x20;       \`\`\`

&#x20;      &#x20;

&#x20;   \- \*\*Common Use Cases:\*\*

&#x20;       \- Displaying file content.

&#x20;       \- Combining multiple files into one.

&#x20;       \- Creating a new file by redirecting input.



\---



&#x20;\`less\` (View Files One Page at a Time)



\- Command:\*\* \`less file.txt\`

&#x20;   \- Opens a file for reading, allowing navigation through it one page or line at a time.

&#x20;   \- \*\*Advantages over \`cat\`:\*\*

&#x20;       \- Does not load the entire file into memory, making it ideal for large files.

&#x20;   \- \*\*Navigation Shortcuts:\*\*

&#x20;       \- \*\*Forward Search:\*\* \`/\` followed by the search term.

&#x20;       \- \*\*Backward Search:\*\* \`?\` followed by the search term.

&#x20;       \- Press \`q\` to quit.



\---



\## \`head\` (Display the First Few Lines of a File)



\- \*\*Command:\*\* \`head file.txt\`

&#x20;   \- Displays the first 10 lines of a file by default.

&#x20;   \- \*\*Options:\*\*

&#x20;       \- \`n [number]\`: Specify the number of lines to display.

&#x20;           \- \*\*Example:\*\* \`head -n 5 file.txt\` (displays the first 5 lines).



\---



\## \`wc\` (Word Count and Statistics)



\- \*\*Command:\*\* \`wc file.txt\`

&#x20;   \- Displays the number of lines, words, and characters in a file.

&#x20;   \- \*\*Options:\*\*

&#x20;       \- \`wc -l file.txt\`: Counts the number of lines.

&#x20;       \- \`wc -w file.txt\`: Counts the number of words.

&#x20;       \- \`wc -c file.txt\`: Counts the number of bytes.

&#x20;       \- \`wc -m file.txt\`: Counts the number of characters (useful for multibyte characters).



\---



\## \`du\` (Disk Usage of a File or Directory)



\- \*\*Command:\*\* \`du romeo.txt\`

&#x20;   \- Displays the disk usage of the file or directory.

&#x20;   \- \*\*Options:\*\*

&#x20;       \- \`du -h romeo.txt\`: Shows disk usage in a human-readable format (e.g., KB, MB).tories like `Documents`, `Downloads`, and `Pictures`.

#### List All Files (Including Hidden Files):

```bash
ls -a
```

By default, files that start with a dot (`.`) are hidden. This command reveals all files, including hidden ones, in the directory.

---

### Additional `ls` Options

The `ls` command becomes even more powerful when combined with options. Options are like modifiers that change how the command behaves.

| Option | Description                                                                                                                                                                                                       |
| ------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `-l`   | Long format. Displays detailed file information, including permissions, ownership, size, and modification time. For example, this is helpful when you need to check who owns a file or when it was last modified. |
| `-a`   | Shows all files, including hidden ones.                                                                                                                                                                           |
| `-h`   | Displays file sizes in human-readable formats (e.g., KB, MB) when combined with `-l`. This is especially useful for understanding file sizes at a glance.                                                         |
| `-R`   | Lists contents of directories recursively, including subdirectories. This means you can see not only the files in the current directory but also everything inside its subdirectories.                            |
| `-t`   | Sorts files by modification time, with the newest first. Use this to quickly find the most recently updated files.                                                                                                |
| `-r`   | Reverses the order of the output. For example, when combined with `-t`, it will list the oldest files first.                                                                                                      |
| `-1`   | Lists one file per line instead of displaying them in columns. This can make the output easier to read in some cases.                                                                                             |
| `-d`   | Lists directories themselves, not their contents. Use this to see only the directories without diving into them.                                                                                                  |
| `-F`   | Appends a character to filenames indicating their type (e.g., `/` for directories, `*` for executables). This gives you more context about the files at a glance.                                                 |
| `-L`   | Follows symbolic links and lists the actual file or directory they point to. Symbolic links are like shortcuts to other files or directories.                                                                     |
| `-X`   | Sorts files alphabetically by their extension. For example, files ending in `.txt` will be grouped together.                                                                                                      |

---

### Pro Tip:

You can combine multiple options to customize the output further. For example, the command:

```bash
ls -lh
```

will display the files in a long format with human-readable file sizes.

Learning these basic commands will set a strong foundation for your journey in Data Engineering. The more you practice, the more comfortable you’ll become with navigating Linux systems!

---

## Understanding File Details in Linux

When you list files in a long format using the `ls -l` command, you get detailed information about each file. Here is an example output:

```bash
-rw-r--r--  1 root root         0 Jan  2 15:48 outout.txt
-rw-r--r--  1 root root        12 Jan  5 00:09 output.txt
-rw-r--r--  1 root root        15 Jan  2 15:42 output.txx
-rwxr-xr-x  1 root root    169360 Jan  2 15:09 romeo.txt
drwx------  3 root root      4096 Nov 29 19:22 snap
```

Let’s break down the first line:

```bash
-rw-r--r--  1 root root         0 Jan  2 15:48 outout.txt
```

### Explanation:

1. **`-rw-r--r--`**: This represents the file's permissions.

   - The first character indicates the type of file:
     - `-` means it is a regular file.
     - `d` means it is a directory.
     - `l` means it is a symbolic link.
   - The next three characters (`rw-`) indicate the owner's permissions:
     - `r`: Read permission.
     - `w`: Write permission.
     - `-`: No execute permission.
   - The next three characters (`r--`) indicate the group’s permissions.
   - The last three characters (`r--`) indicate permissions for others.

2. **`1`**: This is the number of hard links to the file.

3. **`root root`**: These are the owner and group of the file.

4. **`0`**: This is the size of the file in bytes.

5. **`Jan  2 15:48`**: This is the last modification date and time of the file.

6. **`outout.txt`**: This is the name of the file.

By understanding these details, you can gather important information about files, such as their type, size, permissions, and last modification date.

---

## Navigating Directories with `cd`

The `cd` command (short for "change directory") allows you to navigate between folders in your file system.

### Absolute Path:

An absolute path specifies the complete path to a file or directory from the root directory (`/`).

#### Example:

```bash
cd /home/huseyn/Desktop
```

This command navigates directly to the `Desktop` folder using the full path from the root directory.

### Relative Path:

A relative path specifies the location of a file or directory in relation to the current working directory.

#### Example:

```bash
cd ~/Desktop
```

The `~` symbol is shorthand for the home directory. This command navigates to the `Desktop` folder relative to the user's home directory.

With `cd`, you can move efficiently through your directory structure, whether using absolute or relative paths.

