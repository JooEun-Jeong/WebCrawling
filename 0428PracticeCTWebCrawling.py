from selenium import webdriver
import datetime
driver = webdriver.Chrome('./chromedriver')
driver.implicitly_wait(1)
driver.get('https://clinicaltrials.gov/ct2/resources/trends')
driver.implicitly_wait(1)

table = driver.find_elements_by_class_name('ct-data_table.ct-trends_table')

f = open("./result_of_tables.txt", 'w') # text file에 저장

for k in range(len(table)):    
    tbody = table[k].find_element_by_tag_name("tbody")
    rows = tbody.find_elements_by_tag_name("tr")
    
    #contents ot table
    f.write("=====%d table====\n"%(k+1))
    for i in range(len(rows)):
        col = rows[i].find_elements_by_tag_name("td")
        # name = rows[i].find_elements_by_tag_name("th")
        if(len(col) != 0):
            # for j in range(0, len(name)):
            #     print(name[j].text, end="\t")
            for j in range(0, len(col)):
                print(col[j].text, end="\t")
                f.write(col[j].text + "\t")
            print()
            f.write("\n")
    print("\n")
    f.write("\n\n")
f.close()

""" print결과
=====1 table====
Non-U.S. only	214,453   (52%)	
U.S. only	131,529   (32%)	
Both U.S. and non-U.S.	20,616   (5%)	
Not provided	46,430   (11%)	
Total	413,028   (100%)	


=====2 table====
Non-U.S. only	38,110   (61%)	
U.S. only	20,966   (33%)	
Both U.S. and non-U.S.	3,440   (5%)	
Not provided	199   (0%)	
Total	62,715   (100%)	


=====3 table====
413,028	53,975	
319,854   (77%)	50,795   (94%)	
170,710	38,430	
108,299	10,294	
33,154	2,681	
42,315	7,281	
91,520   (22%)	3,180   (6%)	
822	N/A	


=====4 table====
2000 †	1,255 †	2,119	2,119	
2001	2,119	1,773	3,892	
2002	3,892	1,378	5,270	
2003	5,270	3,588	8,858	
2004	8,858	3,166	12,024	
2005	12,024	12,798	24,822	
2006	24,822	10,917	35,739	
2007	35,739	12,549	48,288	
2008	48,288	17,564	65,852	
2009	65,852	17,009	82,861	
2010	82,861	17,346	100,207	
2011	100,207	17,817	118,024	
2012	118,024	19,463	137,487	
2013	137,487	20,431	157,918	
2014	157,918	23,310	181,228	
2015	181,228	24,108	205,336	
2016	205,336	27,789	233,125	
2017	233,125	29,176	262,301	
2018	262,301	30,955	293,256	
2019	293,256	32,517	325,773	
2020	325,773	36,732	362,505	
2021	362,505	37,027	399,532	
2022	399,532	13,496 ‡	413,028 ‡	


=====5 table====
2008 †	0 †	41	41	
2009	41	1,098	1,139	
2010	1,139	1,617	2,756	
2011	2,756	2,200	4,956	
2012	4,956	2,804	7,760	
2013	7,760	3,093	10,853	
2014	10,853	4,827	15,680	
2015	15,680	3,801	19,481	
2016	19,481	4,185	23,666	
2017	23,666	5,827	29,493	
2018	29,493	4,659	34,152	
2019	34,152	6,523	40,675	
2020	40,675	6,043	46,718	
2021	46,718	5,818	52,536	
2022	52,536	1,439 ‡	53,975 ‡	


"""
