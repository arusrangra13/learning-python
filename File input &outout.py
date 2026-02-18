#createing a file 
f = open("helo.txt","r")
data = f.read()
print(data)
print(type(data))

#Writing a file
f = open("helo.txt","a")
f.write("then we do dbms")
f.close()
