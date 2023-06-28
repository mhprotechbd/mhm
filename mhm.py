import os,platform
os.system('git pull')
 
mhmm=platform.architecture()[0]
if mhmm=="32bit":
    print('Sorry 32 Bit Not Supported...')
elif mhmm=="64bit":
     __import__("mhm")
