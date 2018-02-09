f=open('textfile.txt','w+')
for i in range(10):
    f.write("this is line %d\r\n" %(i+1))
f.close()
