f = open("myfile.txt", 'r')
text = f.read()
print(text)
f.close()

with open('myfile.txt', 'a') as f:
  f.write("Hey I am inside with")
  
write = open("myfile2.txt", 'w')
tect = write.write("Samyam is a bad ass leader.")
print(tect)
write.close()
