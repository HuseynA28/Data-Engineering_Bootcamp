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

#### List Files in the Home Directory:
```bash
ls ~
```
The home directory is where your personal files and folders are stored. Use this command to see what’s in your home folder. For example, it might contain directories like `Documents`, `Downloads`, and `Pictures`.

#### List All Files (Including Hidden Files):
```bash
ls -a
```
By default, files that start with a dot (`.`) are hidden. This command reveals all files, including hidden ones, in the directory.

---

### Additional `ls` Options

The `ls` command becomes even more powerful when combined with options. Options are like modifiers that change how the command behaves.

| Option | Description |
|--------|-------------|
| `-l`   | Long format. Displays detailed file information, including permissions, ownership, size, and modification time. For example, this is helpful when you need to check who owns a file or when it was last modified. |
| `-a`   | Shows all files, including hidden ones. |
| `-h`   | Displays file sizes in human-readable formats (e.g., KB, MB) when combined with `-l`. This is especially useful for understanding file sizes at a glance. |
| `-R`   | Lists contents of directories recursively, including subdirectories. This means you can see not only the files in the current directory but also everything inside its subdirectories. |
| `-t`   | Sorts files by modification time, with the newest first. Use this to quickly find the most recently updated files. |
| `-r`   | Reverses the order of the output. For example, when combined with `-t`, it will list the oldest files first. |
| `-1`   | Lists one file per line instead of displaying them in columns. This can make the output easier to read in some cases. |
| `-d`   | Lists directories themselves, not their contents. Use this to see only the directories without diving into them. |
| `-F`   | Appends a character to filenames indicating their type (e.g., `/` for directories, `*` for executables). This gives you more context about the files at a glance. |
| `-L`   | Follows symbolic links and lists the actual file or directory they point to. Symbolic links are like shortcuts to other files or directories. |
| `-X`   | Sorts files alphabetically by their extension. For example, files ending in `.txt` will be grouped together. |

---

### Pro Tip:
You can combine multiple options to customize the output further. For example, the command:
```bash
ls -lh
```
will display the files in a long format with human-readable file sizes.

Learning these basic commands will set a strong foundation for your journey in Data Engineering. The more you practice, the more comfortable you’ll become with navigating Linux systems!

