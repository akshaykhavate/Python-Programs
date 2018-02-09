def main():
    f=open("textfile.txt","a+")
    for i in range(11,13):
        f.write("Appended line %d\r\n" %(i+1))
    f.close()
if __name__=="__main__":
    main()
