# import sys as sys
# import textract
# actual_file_name = sys.argv[1]
#
#
# def read_PDF_files(pdf_file_path):
#     """
# Algorithm:
#     Read_Flies(file_name)
# Purpose:
#     To put all the characters into a list
# Pre-Condition:
#     :param file_name: A name of a file
# Post-Condition:
#     None
# Return:
#     a list contains all characters fom the file
#     """
#     text = textract.process(pdf_file_path, method='pdfminer')
#     print text
#
#
# def create_dictionary(a_list):
#     """
# Algorithm:
#     Create_dictionary(a_list)
# Purpose:
#     To put all the characters from a list to a dictionary
# Pre-Condition:
#     :param alist: A list contains all characters from the file
# Post-Condition:
#     None
# Return:
#     a dictionary contains all characters fom the a list
#     """
#     dic = {}
#     sub_dic = {}
#     dic['size'] = 0
#     dic['data'] = None
#     if a_list is None:
#         return dic
#     for t in a_list:
#         if t not in sub_dic:
#             sub_dic[str(t)] = 1
#             dic['size'] += 1
#         else:
#             sub_dic[str(t)] += 1
#     dic['data'] = sub_dic
#     return dic
#
#
#
# # dic = create_dictionary(characters_list)
#
# # Here, I am going to print put the dictionary to see the mapping between character and its occurrence in the file
# # print "### dictionary..."
# # print read_PDF_files(actual_file_name)
# # print "###"
