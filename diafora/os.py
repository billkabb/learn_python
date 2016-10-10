#os module video78
import os


os.system() # Executing a shell command
os.stat()   # Get the status of the file
os.environ() # Get the users environment
os.chdir() #move focus to a different dir
os.getcwd() # curent working dir
os.getgid() # group id
os.getuid()# user id
os.getpid()# get process id
os.getlogin() # get user logged
os.access() # check read permissions
os.chmod() #
os.chown() #change owner and group id
os.umask(mask) # set the curent numeric mask
os.getsize() # get the file size
os.path.getmtime() # get the modify time
os.path.getatime() # get the access time
os.environ() # get the user environment
os.uname() # get the operating system
os.chroot(path) # change the root directory of the curent process to path
os.listdir(path) # list dir
os.getloadavg() 
os.path.exists()# check if a path exists
os.walk() # print all dirs and subdirs
os.mkdir(path) # make a dir
os.makedirs(path) # recursive dir creation
os.remove(path) # delete file
os.removedirs(path) # remove dirs recursively
os.rename(src,dst)
os.rmdir(path) #remove directory

