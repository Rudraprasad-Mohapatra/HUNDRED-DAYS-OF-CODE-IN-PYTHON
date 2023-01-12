import os
# folders=os.listdir("data")



# for folder in folders:
#     print(folder)

#OutPut will be:
"""
Code Of Day-1
Code Of Day-10 
Code Of Day-100
Code Of Day-11 
Code Of Day-12 
Code Of Day-13 
Code Of Day-14 
Code Of Day-15
Code Of Day-16
Code Of Day-17
Code Of Day-18
Code Of Day-19
Code Of Day-2
Code Of Day-20
Code Of Day-21
Code Of Day-22
Code Of Day-23
Code Of Day-24
Code Of Day-25
Code Of Day-26
Code Of Day-27
Code Of Day-28
Code Of Day-29
Code Of Day-3
Code Of Day-30
Code Of Day-31
Code Of Day-32
Code Of Day-33
Code Of Day-34
Code Of Day-35
Code Of Day-36
Code Of Day-37
Code Of Day-38
Code Of Day-39
Code Of Day-4
Code Of Day-40
Code Of Day-41
Code Of Day-42
Code Of Day-43
Code Of Day-44
Code Of Day-45
Code Of Day-46
Code Of Day-47
Code Of Day-48
Code Of Day-49
Code Of Day-5
Code Of Day-50
Code Of Day-51
Code Of Day-52
Code Of Day-53
Code Of Day-54
Code Of Day-55
Code Of Day-56
Code Of Day-57
Code Of Day-58
Code Of Day-59
Code Of Day-6
Code Of Day-60
Code Of Day-61
Code Of Day-62
Code Of Day-63
Code Of Day-64
Code Of Day-65
Code Of Day-66
Code Of Day-67
Code Of Day-68
Code Of Day-69
Code Of Day-7
Code Of Day-70
Code Of Day-71
Code Of Day-72
Code Of Day-73
Code Of Day-74
Code Of Day-75
Code Of Day-76
Code Of Day-77
Code Of Day-78
Code Of Day-79
Code Of Day-8
Code Of Day-80
Code Of Day-81
Code Of Day-82
Code Of Day-83
Code Of Day-84
Code Of Day-85
Code Of Day-86
Code Of Day-87
Code Of Day-88
Code Of Day-89
Code Of Day-9
Code Of Day-90
Code Of Day-91
Code Of Day-92
Code Of Day-93
Code Of Day-94
Code Of Day-95
Code Of Day-96
Code Of Day-97
Code Of Day-98
Code Of Day-99 """


# print(folders ,type (folders),end="\n")
#OutPut will be:
"""
['Code Of Day-1', 'Code Of Day-10', 'Code Of Day-100', 'Code Of Day-11', 'Code Of Day-12', 'Code Of Day-13', 'Code Of Day-14', 'Code Of Day-15', 'Code Of Day-16', 'Code Of Day-17', 'Code Of Day-18', 'Code Of Day-19', 'Code Of Day-2', 'Code Of Day-20', 'Code Of Day-21', 'Code Of Day-22', 'Code Of Day-23', 'Code Of Day-24', 'Code Of Day-25', 'Code Of Day-26', 'Code Of Day-27', 'Code Of Day-28', 'Code Of Day-29', 'Code Of Day-3', 'Code Of Day-30', 'Code Of Day-31', 'Code Of Day-32', 'Code Of Day-33', 'Code Of Day-34', 'Code Of Day-35', 'Code Of Day-36', 'Code Of Day-37', 'Code Of Day-38', 'Code Of Day-39', 'Code Of Day-4', 'Code Of Day-40', 'Code Of Day-41', 'Code Of Day-42', 'Code Of Day-43', 'Code Of Day-44', 'Code Of Day-45', 'Code Of Day-46', 'Code Of Day-47', 'Code Of Day-48', 'Code Of Day-49', 'Code Of Day-5', 'Code Of 
Day-50', 'Code Of Day-51', 'Code Of Day-52', 'Code Of Day-53', 'Code Of Day-54', 'Code Of Day-55', 'Code Of Day-56', 'Code Of Day-57', 'Code Of Day-58', 'Code Of Day-59', 'Code Of Day-6', 'Code Of Day-60', 'Code Of Day-61', 'Code Of Day-62', 'Code Of Day-63', 'Code Of Day-64', 
'Code Of Day-65', 'Code Of Day-66', 'Code Of Day-67', 'Code Of Day-68', 'Code Of Day-69', 'Code Of Day-7', 'Code Of Day-70', 'Code Of Day-71', 'Code Of Day-72', 'Code Of Day-73', 'Code Of Day-74', 'Code Of Day-75', 'Code Of Day-76', 'Code Of Day-77', 'Code Of Day-78', 'Code Of 
Day-79', 'Code Of Day-8', 'Code Of Day-80', 'Code Of Day-81', 'Code Of Day-82', 'Code Of Day-83', 'Code Of Day-84', 'Code Of Day-85', 'Code Of Day-86', 'Code Of Day-87', 'Code Of Day-88', 'Code Of Day-89', 'Code Of Day-9', 'Code Of Day-90', 'Code Of Day-91', 'Code Of Day-92', 'Code Of Day-93', 'Code Of Day-94', 'Code Of Day-95', 'Code Of Day-96', 'Code Of Day-97', 'Code Of Day-98', 'Code Of Day-99'] <class 'list'>

"""

#If we want to see all the files inside all the folders one by one
# for folder in folders:
#     print(folder,"-",os.listdir(f"data/{folder}"))

print(os.getcwd()) #to get the current working directory
os.chdir("G:\movies_ashish")#for changing dirctory
print(os.getcwd()) #after changing the current directory to "G:\movies_ashish"
# delete a file
os.remove("G:\HUNDRED-DAYS-OF-CODE-\data\Code Of Day-1")

"""
Using the os module in python
To use the os module to delete a file, we import it, then use the remove() function provided by the module to delete the file. It takes the file path as a parameter. You can not just delete a file but also a directory using the os module.
"""