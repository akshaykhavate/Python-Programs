fo = open("textfile.txt", "r")
str = fo.read(20);
print("Read String is : ", str)
position = fo.tell();
print("Current file position : ", position)
position = fo.seek(3, 0);
str = fo.read(10);
print("Again read String is : ", str)
fo.close()
