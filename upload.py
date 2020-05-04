import os
import ftplib

## aboudzein

def list_files(dir):
    #open ftp session
    session = ftplib.FTP('ftp_host','username','password')
    for root, dirs, files in os.walk(dir):
        # iterate throw folder tree 
        for name in files:
            file = open(os.path.join(root, name),'rb')  #open the file path 
            session.storbinary('STOR FILE' + name, file) #upload the files
            print(file) # print the file name
            file.close() # close file connection
    session.quit()

#invoke function using folders path 
list_files('./folders')