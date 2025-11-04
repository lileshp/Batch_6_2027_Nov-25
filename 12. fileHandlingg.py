#file handling
'''
    file system: FAT32, NTFS, ext
    file structure: 
    file storage: 

open('fileName.extension','accessMode')
accessMode:
    r - read
    w - write
    a  - append
    rb - read binary

binary values: 0 1
binary data: image, audio, video, pdf, any document

ASCII
open('example.txt','w'): if file not exists then it will
create a new file.

open('example.txt','r'): if file not exists then it will
retrun an error FileNotFound.
    
'''
'''
file = open('example.txt','w')
file.write("Hello World")
file.close()
print(file)
'''
'''
ABsolute
relative

'''
#WRITE
file = open('..\\Practice_Code\\example.txt','w')
for i in range(201,210):
    file.write(f"Line Number {i}")    
file.close()




