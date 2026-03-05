try:
   srcfile=open("file1","w+")
   srcfile.write("welcome to files method\n1.seek\n2.flush\n3.tell")
   srcfile.flush()
   srcfile.seek(5)
   print(srcfile.read())
   print(srcfile.tell())
except FileNotFoundError:
   print("file doesnt exist")
