from Bio.KEGG import REST
from Bio.Entrez import efetch

from Bio import Entrez
Entrez.email = "larre0128@gmail.com"

import random
from bs4 import BeautifulSoup
import time
import requests
from tqdm import tqdm 
import numpy as np

search = '"Epistasis, Genetic"[Mesh] OR "Genetic Predisposition to Disease"[Mesh] AND Disease AND Genetic'
handle = Entrez.esearch(db='pubmed',
                        sort='relevance',
                        retmax='1000000',
                        retmode='xml',
                        mindate='1946/01/01',
                        maxdate='2021/01/01',
                        term=search)
pubmed_api = Entrez.read(handle)
search_pubmed_count = pubmed_api['Count']
search_pmid = pubmed_api['IdList']

print('\033[1m 搜尋關鍵字:\033[0m', '[{}]'.format(search))
print('\033[1m 搜尋結果:\033[0m {} 篇'.format(search_pubmed_count))
print('\033[1m PMID:\033[0m', search_pmid)

search = '"Epistasis, Genetic"[Mesh] OR "Genetic Predisposition to Disease"[Mesh] AND Disease AND Genetic'
PMID = []

handle = Entrez.esearch(db='pubmed',
                        sort='relevance',
                        retmax='10000',
                        retmode='xml',
                        mindate='1946/01/01',
                        maxdate='2001/01/01',
                        term=search)
pubmed_api = Entrez.read(handle)
PMID += pubmed_api['IdList']
print('\033[1m PMID:\033[0m 1946~2001: ', len(pubmed_api['IdList']))

for year in range(2001, 2021):
    mindate = f'{year}/01/02'
    maxdate = f'{year+1}/01/01'
    handle = Entrez.esearch(db='pubmed',
                            sort='relevance',
                            retmax='10000',
                            retmode='xml',
                            mindate=mindate,
                            maxdate=maxdate,
                            term=search)
    pubmed_api = Entrez.read(handle)
    print(f'\033[1m PMID:\033[0m {year}: ', len(pubmed_api['IdList']))
    PMID += pubmed_api['IdList']

print(len(PMID))

print ("Start : %s" % time.ctime())

PMID_final = []
i=0
Pubtator_all_result = ""
for p in tqdm(range(0,len(PMID))):
# for p in tqdm(range(0,5)):
# for p in range(0,len(PMID)): 
    pmid = PMID[p]
    url = 'https://www.ncbi.nlm.nih.gov/research/pubtator-api/publications/export/pubtator?pmids={}&concepts=gene'.format(pmid)
    ## Step1.取得網頁連線
    slp = 1+random.random() #休息才能走更遠的路
    time.sleep(slp)
    try:

        # keep fetch
        r = requests.get(url) #未經驗證請求網址(!!!)
        # print('{}/{}'.format(i,p),url,'{}s'.format(round(slp,2)))

    except Exception as e:
        # print('Error:\n',e)
        # 休息不夠，更多的休息
        # print('need long time sleep')
        time.sleep(600)
        # keep fetch
        r = requests.get(url)
        # print(p,url,'Sleep 300s......')
        
        
    # 連線是否正常
    if r.status_code!=200:
        print(p,pmid,"連線異常!")
        continue


    ## Step2.使用bs4回傳網頁(html)內容
    resp = BeautifulSoup(r.text,"lxml")


    ## Step3.取得標題所在的標籤內容
    title = resp.find('p')
    if title==None:#跳過沒有內容
        # print(pmid,'no information,skip')#105
        continue
    if len(str(title))<500:#跳過沒有摘要
        # print(pmid,'no abstract,skip') #117
        continue
    Abs = title.text[:]
    
    PMID_final.append(pmid)
    i+=1
    # step4.儲存所有PubTator結果
    # globals()["pub_ent_{}".format(PMID[p])] = Abs # pub_ent_21316027
    Pubtator_all_result += f"\n{Abs}\n{'-'*30}"
    # step5.輸出為外部檔
    # name = "pub_ent_{}".format(PMID[p])
    # save_variable(globals()[name], name+'.txt')

# 儲存PMID list
PMID_final=np.array(PMID_final)
np.save('PMID_final.npy',PMID_final) # 保存為.npy格式

# 儲存PubMed Abstract
with open("Pubtator_all_result.txt", "w") as file:
    file.write(Pubtator_all_result)

print ("End : %s" % time.ctime())
