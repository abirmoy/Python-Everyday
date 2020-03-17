# -*- coding: utf-8 -*-
"""
Created on Sat Dec 28 00:16:54 2019

@author: Abirmoy

"""

import os

def rename_by_order(extention, path = os.getcwd()):
  '''
  ### RENAME ACCORDING TO NUMBER ###
  # given name:       xx xx xxxxx.xxx
  # expected output:  n.xxx; n = 1 to i
  #os.rename(file_to_rename, 'new_name')  
  '''
  i=0
  with os.scandir(path) as entries:
    for entry in entries:      
      os.rename(entry, str(i) + extention)
      i += 1

    


path = ''
extention = '.mp4'
rename_by_order(extention)




# files_name = [] # STORE ALL THE FILE NAMES
# # path = '' # PATH OF THE FILES
# for entry in os.scandir(path):
#   ## FETCHING THE FILE NAMES 'path' DIRECTORY
#     if entry.is_file():
#         files_name.append(entry.name)






## RENAMING FILE FOR CONDITION BELLOW ##
# given name:       xx xx xxxxx part yy.mp4 or Database part 01.mp4
# expected output:  yy xx xx xxxxx.mp4 or o1 Database.mp4
# for item in files_name:
#   print('Before Rename', item)
#   os.rename(item, item[-6:-3] + ' ' + item[0:-11]+ '.mp4') #os.rename(file_to_rename, 'new_name')
#   print('After Rename', item[-6:-3] + ' ' + item[0:-11]+ '.mp4')








# ## RENAME FILES IF THEIR NAME STARTS WITH '('
# for item in files_name:
#   if item[0] == '(':
#     print('Before Rename', item)
#     os.rename(item, item[1:]) #os.rename(file_to_rename, 'new_name')
#     print('After Rename', item[1:])
   






## RENAMING FILE FOR CONDITION BELLOW ##
# given name:       xx xx xxxxx (5.4).mp4
# expected output:  5.4 - xx xx xxxxx.mp4
#for item in files_name:
#  os.rename(item, item[-9:-5]+ ' - ' + item[0:-10]+'.mp4') #os.rename(file_to_rename, 'new_name')
#  print(item)
#  print(item[0:-10])
#  print(item[-9:-5]+ ' - ' + item[0:-10])  
#  name_with_prefix.append(item[-8:-5]+ ' - ' + item[0:-10]+'.mp4')




#### SOME DIRECTORY RELATED (no need for this code) ####
    
## save current working directory
#saved_cwd = os.getcwd()
## change your cwd to the directory which contains files
#os.chdir(path)
## moving back to the directory you were in 
#os.chdir(saved_cwd)
    