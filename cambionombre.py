import os
os.chdir('C:/Users/ferna/Desktop/pdf')
i=0
lista=['15-05-22(152452)','451-12-22(125452)']
for file in os.listdir():
    src=file
    dst=lista[i]+str(i)+".pdf"
    os. rename(src,dst)
    i+=1

print(os.listdir())    