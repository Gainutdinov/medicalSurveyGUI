import os
import datetime
import shutil

d = datetime.date(2012, 12, 14).strftime('%d_%m_%Y')

name="Marat"
surname="Gainutdinov"
middleName="Mubarahanovich"

fileName='simple.doc'

#path = os.getcwd()+'\\'+name+'_'+surname+'_'+middleName+'_'+d
newFolderName=name+'_'+surname+'_'+middleName+'_'+d
path = os.path.join(os.curdir , newFolderName)
newFileName=str(fileName.split('.')[0]+'_'+d+'.'+fileName.split('.')[1])
print(newFileName)

def copy_rename(old_file_name, new_file_name, new_folder_name):
    src_dir= os.curdir
    dst_dir= os.path.join(os.curdir , newFolderName)
    src_file = os.path.join(src_dir, old_file_name)
    shutil.copy(src_file,dst_dir)
    
    dst_file = os.path.join(dst_dir, old_file_name)
    new_dst_file_name = os.path.join(dst_dir, new_file_name)
    os.rename(dst_file, new_dst_file_name)


#print(d)
#print(type(d))

print(path)
try:  
    os.mkdir(path)
    print('----------------')
    copy_rename(fileName, newFileName, newFolderName)
except OSError:  
    print ("Creation of the directory %s failed" % path)
else:  
    print ("Successfully created the directory %s " % path)


