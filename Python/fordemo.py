names=['Akshay','Salman','Sharukh']
for i in names[:]:
    print(i,len(i))
    if len(i)>6:
        names.insert(0,i)
