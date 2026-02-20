#createing a file 
f = open("helo.txt","r")
data = f.read()
print(data)
print(type(data))

#Writing a file
f = open("helo.txt","a")
f.write("then we do dbms")
f.close()

#with syntax
with open("helo.txt","r") as f:
    data=f.read()
    print(data)

#f.write a file
with open("helo.txt","w") as f:
    f.write("new name")

#Creatina file and add data init
with open("hello.txt","w")as f:
    f.write("hi every one \n how are you\nI am fine\n What are you doing")
    
#waf that replace occrance of "are" with "is" \n above file.
with open("hello.txt","r")as f:
    data = f.read()

new_data= data.replace("are","is")
print(new_data)
    
with open("hello.txt","w")as f:
    f.write(new_data)
