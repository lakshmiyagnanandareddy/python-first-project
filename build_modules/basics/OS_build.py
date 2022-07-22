import os


print(os.getcwd())  # getcwd()- gives the path of the current working directory.
os.chdir('C:/Users/Admin/PycharmProjects/pythonProject/build_modules/') # chdir()-is used to change the path of current working directory.
print(os.getcwd())
print(os.listdir()) # listdir()-it will gives the list of the directories.
os.makedirs('sys.py')   # makedirs()- it will creates the new directories.
os.removedirs('sys.py') # removedirs()- it will removes the directory.os.
os.chdir('C:/Users/Admin/PycharmProjects/pythonProject/build_modules/basics')
os.rename("OS_build.py", "os_build.py")    # it will renames the directory.
print(os.stat(os.getcwd())) # stat()- it will give the details of the directory.
# os.walk will move as the tree from the starting directory.
for dirpath, dirnames, filenames in os.walk(top='C:/Users/Admin/PycharmProjects/pythonProject/build_modules/'):
    print("current path :", dirpath)
    print("directories :", dirnames)
    print("file name :", filenames)
    print()
print(os.environ.get("HOME"))
print(os.path.basename('C:/Users/Admin/PycharmProjects/pythonProject/build_modules/basics'))
print(os.path.dirname('C:/Users/Admin/PycharmProjects/pythonProject/build_modules/basics'))
print(os.path.exists('C:/Users/Admin/PycharmProjects/pythonProject/build_modules/basics'))  # it returns true, if it really exits.
print(os.path.split('C:/Users/Admin/PycharmProjects/pythonProject/build_modules/basics/_ast.py'))   # it spilts the basename.
print(os.path.splitext('C:/Users/Admin/PycharmProjects/pythonProject/build_modules/basics/_ast.py'))    # it gives the type of file_name.
