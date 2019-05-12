import sys as sys
import os


def read_files(path_to_file):
    """
Algorithm:
    Read_Flies(file_name)
Purpose:
    To put all the characters into a list
Pre-Condition:
    :param file_name: A name of a file
Post-Condition:
    None
Return:
    a list contains all characters fom the file
    """
    f = open(path_to_file, 'r')
    lst = []
    for line in f:  # This is for every line in the file
        for t in line:  # This is for every single character on the line
            lst.append(t)
    f.close()
    return sorted(lst)


def create_dictionary(a_list):
    """
Algorithm:
    Create_dictionary(a_list)
Purpose:
    To put all the characters from a list to a dictionary
Pre-Condition:
    :param alist: A list contains all characters from the file
Post-Condition:
    None
Return:
    a dictionary contains all characters fom the a list
    """
    dic = {}
    sub_dic = {}
    dic['size'] = 0
    dic['data'] = None
    if a_list is None:
        return dic
    for t in a_list:
        if t not in sub_dic:
            sub_dic[str(t)] = 1
            dic['size'] += 1
        else:
            sub_dic[str(t)] += 1
    dic['data'] = sub_dic
    return dic


def iterating_txts():
    global_dic = {}     # this dic contains all files' dics | key=file name, value = single file dic
    all_files = os.listdir('./TXTs')
    prefix_path = './TXTs/'

    for file_name in all_files:
        if file_name[-4:] in ['.txt', '.TXT']:
            file_path = prefix_path + file_name     # use file path to call previous functions
            characters_list = read_files(file_path)
            dic = create_dictionary(characters_list)    # dic for a single txt file
            global_dic[file_name] = dic
    return global_dic


# Here, I am going to print put the dictionary to see the mapping between character and its occurrence in the file
print("### iterating...")
DIC = iterating_txts()
for file_name in DIC.keys():
    print("/// Name=" + file_name)
    print(DIC.get(file_name))
    print("/// dic for this file is over")
    print()
print("###")
