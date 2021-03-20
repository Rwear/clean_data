# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 10:28:21 2021

@author: Rwear
"""

# with open("original_weibo_content.txt", "r") as f: 
#     O_W_C=f.read().splitlines()
 
# news_content = pd.DataFrame(columns={"id":"","content":"","labels":""},index=[0])
# C = dict()  
# F = dict()
# L = dict()

# for line in O_W_C:
#     filename = line

#     with open('E:/graduate/one/'+filename,encoding="UTF-8") as h:
# import pandas as pd
# import json

# with open("E:/graduate/one/rumomr_repost.txt", "r") as f: 
#     R_R=f.read().splitlines()

# news_content = pd.DataFrame(columns={"id":"","content":"","labels":""},index=[0])
# C = dict()  
# F = dict()
# L = dict()

# for line in R_R:
#     filename = line
#     with open('E:/graduate/CED_Dataset/rumor-repost/'+filename,encoding="UTF-8") as h:
#         s = json.load(h)
#         # print(s['text'])
#         # print(type(s))
        

# import os
# import os.path
# path = 'E:\\graduate\\CED_Dataset\\non-rumor-repost'
#
# 地址需要\\不能\
# 

# print(os.listdir(path))
# file_object = open('non_rumomr_repost.txt','w')

# for parent,dirnames,filenames in os.walk(path):
#     for filename in filenames:
#         print(filename)
#         file_object.write(filename+ '\n')
# file_object.close()

# # 提取评论以及id
# # 将数据变成dataframe然后写入csv
# import json
# import collections
# import pandas as pd

# with open("E:/graduate/one/rumomr_repost.txt", "r") as f: 
#     R_R=f.read().splitlines()


# with open("E:/graduate/one/original_weibo_content.txt", "r") as f: 
#     O_W_C=f.read().splitlines()

# rumor_comment=pd.DataFrame(columns={"id":"","comment":""},index=[0])
# C = dict()  
# L = dict()
# for line in R_R:
#     filename = line
    
#     with open('E:/graduate/CED_Dataset/rumor-repost/'+filename,encoding="UTF-8") as h:
#         # print(h)
#         s = json.load(h)
#         # print(type(len(s)))
#         # C = dict()  
#         # L = dict()
#         #获取最长的三个评论
#         # for i in range(len(s)):
#         #     C[i]=s[i]['text']
#         #     L[i]=len(C[i])
#         # k = collections.Counter(L)
#         # high = k.most_common(3)
        
#         # # print(high)
#         # for i in range(3):
#         #     temp = {"comment": C[high[i][0]],"id" : filename}
#         #     rumor_comment=rumor_comment.append(temp,ignore_index=True)

#         # print(rumor_comment)

# # from collections import Counter   
# # k = Counter(my_dict)
# # # 3 highest values
# # high = k.most_common(3)
            
# # # print m.items()
# # items = m.items()
# # items.sort(key=lambda x:x[1])
# # print items[len(items) - 1]

#         # print(L)
#         # print(C[178])
    
#     # print('-----------------------------------------')
    
# rumor_comment.to_csv('E:/graduate/one/rumomr_comment.csv')
# # with open('E:/graduate/rumor_comment.csv','w') as R:
# #     R.write(rumor_comment)

import json
import collections
import pandas as pd

with open("E://graduate//one//non_rumomr_repost.txt", "r") as f: 
    R_R=f.read().splitlines()


with open("E://graduate//one//original_weibo_content.txt", "r") as f: 
    O_W_C=f.read().splitlines()

rumor_comment=pd.DataFrame(columns={"id":"","comment":""},index=[0])
C = dict()  
L = dict()
for line in R_R:
    filename = line
    print(filename)
    break
    # with open('E://graduate//CED_Dataset//non-rumor-repost//'+filename,encoding="UTF-8") as h:
    #     # print(h)
    #     s = json.load(h)
    #     print(s)
    #     # print(type(len(s)))
    #     # C = dict()  
    #     # L = dict()
    # #     #获取最长的三个评论
    #     for i in range(len(s)):
    #         C[i]=s[i]['text']
    #         L[i]=len(C[i])
    #     k = collections.Counter(L)
    #     high = k.most_common(3)
        
    #     # print(high)
    #     for i in range(3):
    #         temp = {"comment": C[high[i][0]],"id" : filename}
    #         rumor_comment=rumor_comment.append(temp,ignore_index=True)

        # print(rumor_comment)

# from collections import Counter   
# k = Counter(my_dict)
# # 3 highest values
# high = k.most_common(3)
            
# # print m.items()
# items = m.items()
# items.sort(key=lambda x:x[1])
# print items[len(items) - 1]

        # print(L)
        # print(C[178])
    
    # print('-----------------------------------------')
    
# rumor_comment.to_csv('E://graduate//one//non_rumomr_comment.csv')
# with open('E:/graduate/rumor_comment.csv','w') as R:
#     R.write(rumor_comment)