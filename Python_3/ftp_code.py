from ftplib import FTP
ip= "138.47.99.64"
port= 21
username= "anonymous"
password= ""
folder= "/"
# gives timeout after certain time
use_passive= True

ftp = FTP()
ftp.connect (ip, port)
ftp.login(username, password)
ftp.set_pasv(use_passive)

# changing the driectory
ftp.cwd(folder)
files = []
# append the directory files to empty list
ftp.dir(files.append)

ftp.quit()

for f in files:
    print(f)