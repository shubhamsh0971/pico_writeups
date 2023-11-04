
![Alt text](image.png)

After downloading and decompressing the file using 'gunzip' command.

Using 'mmls' command to see the partitions.

![Alt text](image-1.png)

There are 2 Linux (0x83). I am going with the bigger one.

Listing files in root directory using 'fls' command.

![Alt text](image-2.png)

Checking files in root directory using its Inode number. 

![Alt text](image-3.png)

We can see the flag file is encrypted. Let's check the .ash_history file using 'icat' command.

![Alt text](image-4.png)

So, the flag is encypted using these commands.

First, we need to mount that disk to get that encrypted file

![Alt text](image-5.png)

Unmount the disk image

![Alt text](image-6.png)

Now, we can decrypt the flag. Remember to change the filenames in command

![Alt text](image-8.png)

