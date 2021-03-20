# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 11:00:38 2021

@author: Rwear
"""
# import pandas as pd
# import os
# import os.path
# import json
# import collections
# # f2 = pd.read_csv('data/rumor_comment.csv')
# C = dict()  
# L = dict()
# path = "E://graduate//CED_Dataset//rumor-repost//2_yBmepBtUB_2279086572.json"
# # E:/graduate/CED_Dataset/rumor_repost/0_yBmepBtUB_2279086572.json
# # print(os.listdir(path))
# with open(path,'r',encoding = 'utf-8') as f:
#     s = json.load(f)
    # for i in range(len(s)):
    #     C[i]=s[i]['text']
    #     L[i]=len(C[i])
    # k = collections.Counter(L)
    # high = k.most_common(3)

# file_object = open(r'E:\graduate\CED_Dataset\rumor-repost\0_yBmepBtUB_2279086572.json','w')


'''
清洗获得无重复的数据
'''
import json
import collections
import pandas as pd

# with open("E://graduate//one//original_weibo_content.txt", "r") as f: 
#     R_R=f.read().splitlines()
    
#     # print(type(f))
#     # if R_R == "0_yBmepBtUB_2279086572.json":
#     #     print("e")
        


# with open("E://graduate//one//original_weibo_content.txt", "r") as f: 
#     O_W_C=f.read().splitlines()

# news_content=pd.DataFrame(columns={"id":"","content":"","labels":""},index=[0])
# # C = dict()  
# # L = dict()
# for line in O_W_C:
#     filename = line
# #     print(filename)

#     with open("E://graduate//CED_Dataset//original-microblog//"+filename,'r',encoding = 'utf-8') as f:
#         s = json.load(f)
#         # print(f)
#         # break
#         # C = dict()  
#         # L = dict()
        
#         if filename in O_W_C:
#             temp = {"content":s['text'],"id":filename,"labels":'True'}
#             news_content=news_content.append(temp,ignore_index=True)
            
#         else:
#             temp = {"content":s['text'],"id":filename,"labels":'False'}
#             news_content=news_content.append(temp,ignore_index=True)        
        
#         # for i in range(len(s)):
#         #     C[i]=s[i]['text']
#         #     L[i]=len(C[i])
#         # k = collections.Counter(L)
#         # high = k.most_common(3)
#         # print(type(k))
#         # print(type(high))
        

#         # print(high)
#         # for i in range(3):
#         #     temp = {"content": C[high[i][0]],"id" : filename}
#         #     rumor_comment=rumor_comment.append(temp,ignore_index=True)
#         # k.clear()
#         # high.clear()
        
# news_content.to_csv('E://graduate//one//original_weibo_content.csv')



# with open("E://graduate//one//rumomr_repost.txt", "r") as f: 
#     R_R=f.read().splitlines()
#     print(R_R)

# with open("E://graduate//CED_Dataset//rumor-repost//"+filename,'r',encoding = 'utf-8') as f:
#     s = json.load(f)

f1 = pd.read_csv('non_rumomr_comment.csv')
f2 = pd.read_csv('rumomr_comment.csv')
f3 = pd.read_csv('original_weibo_content.csv')
# f4 = pd.read_csv('non_rumomr_comment.tsv')
# f5 = pd.read_csv('rumor_comment.tsv')
# f6 = pd.read_csv('news_content.tsv')
# f7 = pd.read_csv('comment.tsv')
f8 = pd.read_csv('comment.csv')
f9 = pd.read_csv('comment_backup.csv')
f10 = pd.read_csv('test.csv')
# print(type(f10))
'''
以dataframe形式连接csv
'''
# In [4]: frames = [df1, df2, df3]
 
# In [5]: result = pd.concat(frames)

# frames = [f2, f1]
# result = pd.concat(frames)

# print(type(result))

# result.to_csv("comment.csv")

import re

def clearContentWithSpecialCharacter(content):
 
# 先将<!--替换成，普通字符l
    content = content.replace("@","l")
# 再将-->替换成，普通字符l
    content = content.replace(" ","frt_4")
# 分组标定，替换，
    pattern = re.compile(r'(l)(.*)(frt_4)')
    content = content.replace("frt_4"," ")
# 如果想包括两个1，则用pattern.sub(r\1''\3,content)
    return pattern.sub(r'',content)

for index, row in f8.iterrows():
    # print(type(row["comment"]))
    temp = clearContentWithSpecialCharacter(row['comment'])
    # print(type(temp),type(row['comment']))
    # print(temp)
    f10.append(temp)
    # if type(row['comment'])==float:
    #     print(index)
    break

'''
创建csv文件
'''


# import csv
# csvFile=open("E://graduate//one//test.csv",'w',newline='')
# try:
# 	writer=csv.writer(csvFile)
# 	writer.writerow(('id','comment'))

# finally:
# 	csvFile.close()
















