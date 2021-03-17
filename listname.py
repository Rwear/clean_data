# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 10:00:53 2021

@author: Rwear
"""



'''
# E:\graduate\CED_Dataset\original-microblog
# import os
# def allDir(path):
#     f=[]
#     for root,dirs,files in os.walk(path):
#         for filespath in files:
#             print(os.path.join(root,filespath))
#             f.append(os.path.join(root,filespath))

#     print(f)
#     return(f)
'''

# import os
# import os.path

# A = open('original_weibo_content.txt','r')
# a = list(A)
# print(a)
# A.close()
# B = open('rumor_report.txt','r')
# b = list(B)
# print(b)
# B.close()

# A_C = 'E:\graduate\CED_Dataset\original-microblog'
# F_R = 'E:\graduate\CED_Dataset\rumor-repost'
# T_R = 'E:\graduate\CED_Dataset\non-rumor-repost'
# F = open('F_data.txt','w')
# for A_N in os.listdir(A_C):
#     for F_N in os.listdir(F_R):
#         if A_N == F_N:
#             A = open('A_N','w')
#             F.write(A[])
            
# import os

# def checkPath(path):

#     for dirname, dirnames, filenames in os.walk(path):

#         for filename in filenames:

#             print (filename)

# pathList = ["E:\graduate\CED_Dataset\rumor-repost", "E:\graduate\CED_Dataset\original-microblog"]

# file_object = open('rumomr_repostre.txt','w')
# for path in pathList:

#     checkPath(path)

# print ("done")
        
#打开两个文件并放入列表中
'''  评论处理

获得数据的名称
# E:\graduate\CED_Dataset\original-microblog
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

提取评论以及id
将数据变成dataframe然后写入csv
import json
import collections
import pandas as pd

with open("non_rumomr_repost.txt", "r") as f: 
    R_R=f.read().splitlines()


with open("original_weibo_content.txt", "r") as f: 
    O_W_C=f.read().splitlines()

rumor_comment=pd.DataFrame(columns={"id":"","comment":""},index=[0])
C = dict()  
L = dict()
for line in R_R:
    filename = line
    
    with open('E:/graduate/CED_Dataset/non-rumor-repost/'+filename,encoding="UTF-8") as h:
        # print(h)
        s = json.load(h)
        # print(type(len(s)))
        # C = dict()  
        # L = dict()
        #获取最长的三个评论
        for i in range(len(s)):
            C[i]=s[i]['text']
            L[i]=len(C[i])
        k = collections.Counter(L)
        high = k.most_common(3)
        
        # print(high)
        for i in range(3):
            temp = {"comment": C[high[i][0]],"id" : filename}
            rumor_comment=rumor_comment.append(temp,ignore_index=True)

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
    
rumor_comment.to_csv('E:/graduate/non_rumomr_comment.csv')
# with open('E:/graduate/rumor_comment.csv','w') as R:
#     R.write(rumor_comment)

'''

import json
import collections
import pandas as pd

with open("rumomr_repost.txt", "r") as f: 
    R_R=f.read().splitlines()

with open("original_weibo_content.txt", "r") as f: 
    O_W_C=f.read().splitlines()
 
news_content = pd.DataFrame(columns={"id":"","content":"","labels":""},index=[0])
C = dict()  
F = dict()
L = dict()

for line in O_W_C:
    filename = line
    
    with open('E:/graduate/CED_Dataset/original-microblog/'+filename,encoding="UTF-8") as h:
        # print(h)
        s = json.load(h)
        # print(type(len(s)))
        # C = dict()  
        # L = dict()
        # print(s['text'])
        # print(filename)
        # print(s['user']['verified'])
        # for i in range(len(s)):
        #     C[i]=s['text']
        #     print(C[i])
        #     F[i]=s[i]['user']['verified']
        #     print(F[i])
        #     L[i]=len(C[i])
        
        # print(high)
        # i=1
        # i=i+1
        # print(i)
        if filename in R_R:
            temp = {"comment":s['text'],"id":filename,"labels":'True'}
            news_content=news_content.append(temp,ignore_index=True)
            
        else:
            temp = {"comment":s['text'],"id":filename,"labels":'False'}
            news_content=news_content.append(temp,ignore_index=True)
        # print(rumor_comment)
        # break
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
    
news_content.to_csv('E:/graduate/news_content.csv')















