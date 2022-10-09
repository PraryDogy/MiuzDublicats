import os


file1 = '/Volumes/Untitled/0O3A0216.png'
file2 = '/Users/evlosh/Desktop/0O3A0216.png'


print(int(os.stat(file1).st_birthtime), int(os.stat(file1).st_mtime), int(os.path.getsize(file1)))
print(int(os.stat(file2).st_birthtime), int(os.stat(file2).st_mtime), int(os.path.getsize(file2)))