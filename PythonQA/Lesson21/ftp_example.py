import ftplib
f = ftplib.FTP("192.168.122.244", "ftpuser", "ftpuser")
files = []
f.retrlines("LIST", files.append)
print(f.retrlines("LIST"))
len(files)
print(files[0])
