def main():
    f=open('textfile.txt','r')
    if f.mode=='r':
        contents=f.read()
        print(contents)
    f.close()
if __name__=="__main__":
    main()
