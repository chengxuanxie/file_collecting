#coding:utf-8
import os 
import shutil
import glob
destdir=r'J:\med'
srcdir='J:\迅雷下载'
type_list=['rmvb','avi','mp4','wmv']
print('desdir: '+destdir)
print('srcdir: '+srcdir)

'''return a list containing all the files in file_dir'''
def all_file(file_dir):
    file_list=[]
    name_list=os.listdir(file_dir)
    for each_f in name_list:
        if os.path.isfile(os.path.join(file_dir,each_f)):
            file_list.append(os.path.join(file_dir,each_f))
        elif os.path.isdir(os.path.join(file_dir,each_f)):
            newdir=os.path.join(file_dir,each_f)
            file_list.extend(all_file(newdir))
    return file_list 


'return all the dir in file_dir'
def all_dir(file_dir):
    dir_list=[]
    name_list=os.listdir(file_dir)
    for each_f in name_list:
        if os.path.isfile(os.path.join(file_dir,each_f)):
            pass
        elif os.path.isdir(os.path.join(file_dir,each_f)):
            newdir=os.path.join(file_dir,each_f)
            dir_list.append(newdir)
            dir_list.extend(all_dir(newdir))
    return dir_list 
    
'''return a list containing all the files of some certain types'''
def select_type(file_list,type_list):
    selected_list=[]
    for each_file in file_list:
        if each_file.split('.')[-1] in type_list:
            selected_list.append(each_file)
    return selected_list

def print_list(a_list):
    for each_l in a_list:
        print(each_l)


selected_list=select_type(all_file(srcdir),type_list)
print_list(selected_list)
flag=0

for each_file in selected_list:
    print('start moving file: '+each_file)
    print(flag)
    if 0==flag:
        print('sure to move '+each_file+'to '+destdir+' ?(y/n/a)')
        move=input()
    else :
        move=r'y'
    print(move)
    if 'y' in move or 'Y' in move:
        print('moving '+each_file)
        shutil.copy(each_file,destdir)
        print(each_file+' moved')
    elif 'a' or 'A' in move:
        flag=1
        print('moving '+each_file)
        shutil.copy(each_file,destdir)
        print(each_file+' moved')                   
    else:
        selected_list.remove(each_file)
for each_file in selected_list:
    os.remove(each_file)
    print(each_file+'removed')
print('remove complete')


all_dirs=all_dir(srcdir)
targetdir=[]
for each_dir in all_dirs:
    if 'Thz.la' in each_dir:
        targetdir.append(each_dir)
    else:
        print(each_dir+' remained')
        pass
print('')
print(targetdir)
for each_dir in targetdir:
    shutil.rmtree(each_dir)
    print(each_dir+' removed')










            
    
