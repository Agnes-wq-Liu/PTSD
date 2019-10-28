import pandas as pd
import csv
# processing: generating tab delimited 5 col input file for mixEHR
# formatting on each row: {patient ID, type ID, feature ID, state ID, frequency}
# in this case: encode each answer state under features (questions in the questionnaire) as 1 feature, thus stateID ==1 for all features
# datatype = 1, frequency = 1
# omitting all entries with value nan: 271559 rows in total
df =pd.read_csv('/root/comp401/newpheno.csv')
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
#         print varID
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
#         print varID
