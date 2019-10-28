#!/usr/bin/env python
# coding: utf-8

# In[52]:


import pandas as pd
import csv

df =pd.read_csv('/root/comp401/newpheno.csv')


# df = pd.DataFrame(df)
# df.to_csv('/root/comp401/new.csv',header=True, index=True, index_label=None)
# df.columns[1]
df

import six
import math
patID =[]
varID = 0
patID = df.iloc[:,0]
#  store all patID values in the list
for i in range(1,120,1):
#     print df.columns[i]
    tmp = []
    for l in range(0,6134,1):
        if math.isnan(df.iloc[l,i]):
            if -9 in tmp:
                continue
            else:
                tmp.append(-9)
        elif df.iloc[l,i] in tmp:
            continue
        else:
            tmp.append(df.iloc[l,i])
#     print tmp 
    tmp.pop((tmp.index(-9)))
    if len(tmp) <= 10:
#         implement discretized values
        lable each state with the values 
        with open('oct25_training_5col.txt', 'a+') as f:
            for z in range(0,6134,1):
                if math.isnan(df.iloc[z,i]):
                    continue
                else:
                    pid = patID[z]
                    if varID ==0:
                        f.write(str(pid) + ' 1 '+ str(tmp.index(df.iloc[z,i])+varID) + ' 1 1\n' )
                    else:
                        f.write(str(pid) + ' 1 '+ str(tmp.index(df.iloc[z,i])+varID+1) + ' 1 1\n')
        if varID ==0:
            varID = len(tmp)-1+varID
        else:
            varID = len(tmp)+varID
        print varID
    else:
        m = max(tmp)
        with open('oct25_training_5col.txt', 'a+') as f:
             for z in range(0,6134,1):
                pid = patID[z]
                e = df.iloc[z,i]
                if math.isnan(e):
                    continue
                elif float(e)<=(m/4):
                    sid = 1
                elif float(e)<=(m/2):
                    sid = 2
                elif float(e)<=(m*3/4):
                    sid = 3
                else:
                    sid = 4
                f.write(str(pid) + ' 1 '+ str(varID+sid) + ' 1 1\n' ) 
        varID = varID + 4
        print varID
            
    


# In[16]:


import six
patID =[]
varID = 0
for entries in df.iloc[:,0]:
    if entries!='sid':
        patID.append(entries)
#         store all patID values in the list
# print df.loc[:,'var1']
# print df.loc[1]
for label in df.columns[1:120]:
    cnt = 0
    tmp = []
    for col in df.loc[:,label:label]:#df.loc[:,col:col]:
#         print col
        for entry in df.loc[:,col]:
#             print entry
#     count of numerical value
            if entry =='NaN':
                if -9 in tmp:
                    continue
                else:
                    tmp.append(-9)
#                     cnt+=1
            elif entry in tmp:
                continue
            else:
#                 when the entry isn't in tmp
                tmp.append(entry)
                cnt+=1
    varID = df.columns.get_loc(label)
#     print varID
#     print cnt
    if cnt <= 10:
#         implement discretized values
#         lable each state with the values 
        with open('meta.txt', 'a+') as f:
            for i in range(6134):
                f.write('1 '+ str(varID) + str(cnt)  +'\n' )
    else:
        with open('meta.txt', 'a+') as f:
             for i in range(6134):
                f.write('1 '+ str(varID) + ' 4'+'\n' )


# In[56]:


df1 =pd.read_csv('oct25_new.txt',header = None,sep = ' ')
df1


# In[61]:


cnt = 0
for i in range(0,271559,1):
    if df1.iloc[i,0]==5213:
        cnt+=1
cnt


# In[2]:


import six
patID =[]
cntList = []
for label in df.columns[1:120]:
    cnt = 0
    tmp = []
    for col in df.loc[:,label:label]:#df.loc[:,col:col]:
#         print col       
        i = df.columns.get_loc(col)
#         print i
        for entry in df.loc[:,col]:
            if entry =='NA':
                if -9 in tmp:
                    continue
                else:
                    tmp.append(-9)
#                     cnt+=1
            elif entry in tmp:
                continue
            else:
#                 when the entry isn't in tmp
                tmp.append(entry)
                cnt+=1
#                 print cnt
        if cnt <=10:
            cntList.append(cnt)
        else:
            cntList.append(4)
print str(len(cntList))
with open ('meta.txt', 'r') as d:
    line = d.readline()
    while line:
        tmp = line.split(' ')
        tmp[1] = str(int(tmp[1]))
#         print tmp[1]
        tmp.append(str(cntList[int(tmp[1])-1]))
        sep = ' '
        new = sep.join(tmp)
#         print new
        with open ('new_meta.txt', 'a+') as f:
            f.write(new+'\n')
        line = d.readline()
    


# In[1]:





# In[10]:


import numpy as np
import string
import pandas as pd# implement multi-gap free# 4 inputs: fasta file; score for match; score forr mismatch; gap penalty bdef     
def main():
    fasta = open('/root/comp401/hw1_medium.txt','r')  
    mgf(fasta,1,-1,-1)
def SuborMatch(ms,mms,x,y):    
    if x is y:        
        return ms #match score  
    else:        
        return mms#mismatch score    
def mgf(fasta,ms,mms,b):
    l1 = fasta.readline()
    S = list((l1.strip()).split(' ')[1])
    l2 = fasta.readline()
    T = list(l2.split(' ')[1])
    m = len(S)
    n = len(T)
    X= np.full((m+1,n+1),float("-inf"))
    I = np.full((m+1,n+1),float("-inf"))
    D = np.full((m+1,n+1),float("-inf"))
    align = np.full((m+1,n+1),'n')
    X[0,0]=0
    X[0,1]=b
    X[1,0]=b
    I[0,1]=b
    I[1,0]=b
    D[0,1]=b
    D[1,0]=b
    I[0,0]=0
    D[0,0]=0
    for i in range(1,m+1,1):
        for j in range(1,n+1,1):
            I[i,j] = max(X[i-1,j]+b,D[i-1,j]+b)#b
            D[i,j] = max(X[i,j-1]+b,I[i,j-1]+b)#b
            s=SuborMatch(1,-1,S[i-1],T[j-1])
            X[i,j] = max(X[i-1,j-1]+s,I[i-1,j-1]+s, D[i-1,j-1]+s)
            if (X[i,j]==X[i-1,j-1]+s):
                align[i,j] = 'x'
            elif (X[i,j]==I[i-1,j-1]+s):
                align[i,j] = 'd'
            else:
                align[i,j] = 'i'
#     print(X)
#     print(I)
#     print(D)
#     print(S)
#     print(align)
    s_inAlign = []
    t_inAlign = []
    i =m
    j =n
    score = max(X[i,j],I[i,j],D[i,j])
    while (i >=0 and j>=0):
        if align[i,j]=='x':
    #         print ("yes")
            s_inAlign.append(S[i-1])
            t_inAlign.append(T[j-1])
            i=i-1
            j=j-1
        elif align[i,j]=='i':
            t_inAlign.append(T[j-1])
            s_inAlign.append('-')
            j=j-1
        elif align[i,j]=='d':
            s_inAlign.append(S[i-1])
            t_inAlign.append('-')
            i=i-1
        else:
            break
    s_inAlign.reverse()
    t_inAlign.reverse()
    align_s = string.join(s_inAlign)
    align_t = string.join(t_inAlign)
    with open ('/root/comp401/hw1_feedback_q3.txt','a') as f:
        f.write("score for short run is"+str(score)+'\n')
        f.write(align_s+'\n')
        f.write(align_t+'\n')
    print (score)
    print (align_s)
    print (align_t)
main() 


# In[ ]:




