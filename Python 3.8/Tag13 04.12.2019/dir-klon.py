
import os, stat, sys, time
cur_dir = os.getcwd()
print(cur_dir)

show_hidden = False
show_system = False


if len(sys.argv) > 1:
  if sys.argv[1][0] == "/" and sys.argv[1].count("H") == 1:
    show_hidden = True
  if sys.argv[1][0] == "/" and sys.argv[1].count("S") == 1:
    show_system = True

############### Datei Auflistung ##################
os.system("cls")
print(" ")
print( os.getcwd())
print(" ")
print("Verzeichnis von " + os.getcwd())
print(" ")


for file in os.scandir("."):
    time.strftime("%d.%m.%Y %H:%S")
    do_print = False
    if show_hidden and file.stat().st_file_attributes & stat.FILE_ATTRIBUTE_HIDDEN:
        do_print = True

    if show_system and file.stat().st_file_attributes & stat.FILE_ATTRIBUTE_SYSTEM:
        do_print = True

    elif not show_hidden and not show_system:
        if file.stat().st_file_attributes & stat.FILE_ATTRIBUTE_HIDDEN == 0:
            do_print = True

    if do_print:
        c_time = time.asctime(time.localtime(file.stat().st_ctime))
        is_dir = ""    

        if file.stat().st_file_attributes & stat.FILE_ATTRIBUTE_DIRECTORY != 0:
            is_dir = "<DIR>"

        #print(time.strftime('%Y', time.localtime(file.stat()c_time)))
        print(f"{c_time:20} {is_dir:10} {file.name:>30}")

        print("__________Kurze_Pause__________")
        time.sleep(5)


'''
test1=os.stat(".")
test1.st_file_attributes
test1.st_file_attributes & (stat.FILE_ATTRIBUTE_HIDDEN | stat.FILE_ATTRIBUTE_READONLY)
test1.st_file_attributes & attr = attr
'''
