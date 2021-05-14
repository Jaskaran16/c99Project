import os 
import shutil
#os.system("date")
#os.mkdir("Doggy_World")
#path1 = os.getcwd()
#print(path1)
#path2 = '/C:/Users/anjal/pythonProject/'
#result= os.path.exists(path2)
#print(result)
source = "C:/Users/anjal/pythonProject/Sample1.txt"
destination = "C:/Users/anjal/pythonProject/Doggy_World"
shutil.move(source,destination)