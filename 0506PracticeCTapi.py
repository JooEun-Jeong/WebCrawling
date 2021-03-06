import pandas as pd
import requests

url = 'https://clinicaltrials.gov/api/query/'
response = requests.get(url+ "full_studies?expr=heart+attack&max_rnk=20&fmt=JSON").json()

nctId = []
briefTitle = []
StartDate = []
CompletionDate = []
keywords = []
studyType = []
duration = []

for index in range(0, 20):
        protocalSection = response['FullStudiesResponse']['FullStudies'][index]['Study']['ProtocolSection']
        designModule = protocalSection['DesignModule']
        nctId.append(protocalSection["IdentificationModule"]['NCTId'])
        briefTitle.append(protocalSection["IdentificationModule"]['BriefTitle'])
        StartDate.append(protocalSection['StatusModule']['StartDateStruct']['StartDate'])
        studyType.append(designModule['StudyType'])
        try:
                duration.append(designModule['TargetDuration'])
        except:
                duration.append('None')
        try:
                CompletionDate.append(protocalSection['StatusModule']['PrimaryCompletionDateStruct']['PrimaryCompletionDate'])
        except:
                CompletionDate.append('None')
        try:
                keys = protocalSection['ConditionsModule']['KeywordList']['Keyword']
                tmpList = []
                for k in range(0, len(keys)):
                       tmpList.append(keys[k]) 
                keywords.append(tmpList)
        except:
                keywords.append('None')
        

data = {'NCTID': nctId,
        'Brief Title': briefTitle,
        'Start Date': StartDate,
        'Completion Date': CompletionDate,
        'Study Type' : studyType,
        'Duration' : duration,
        'KeyWords': keywords
        }

df = pd.DataFrame(data)
print(df)
df.to_csv('sample.csv')

"""
          NCTID  ...                                           KeyWords
0   NCT01874691  ...     [acute myocardial infarction, China, Registry]
1   NCT03015064  ...                                               None
2   NCT01168609  ...  [Left atrial distensibility, left ventricular ...
3   NCT03928119  ...  [Acute myocardial infarction, STEMI, regional ...
4   NCT03412435  ...  [Acute myocardial infarction, Myocardial infar...
5   NCT04628104  ...                                               None
6   NCT00632788  ...  [myocardial infarction, catheterization, angio...
7   NCT01484158  ...                            [Myocardial Infarction]
8   NCT00888537  ...  [Decision aid, Heart attack, myocardial infarc...
9   NCT05023681  ...  [Acute Myocardial Infarction???Recombinant Staph...
10  NCT05090618  ...                                             [GWAS]
11  NCT01109225  ...  [aldosterone, myocardial infarction, cardiac r...
12  NCT02913820  ...                                               None
13  NCT03022552  ...  [Myocardial Infarction, Platelets, Blood Colle...
14  NCT02072850  ...  [Myocardial infarction, Primary percutaneous c...
15  NCT00597922  ...  [Acute Myocardial Infarction, Heart Attack, Ge...
16  NCT01182064  ...  [Heart injuries, Posttraumatic myocardial infa...
17  NCT04327635  ...                                               None
18  NCT04957719  ...                  [Platelet Aggregation Inhibitors]
19  NCT04050163  ...                                     [Heart Attack]
"""
