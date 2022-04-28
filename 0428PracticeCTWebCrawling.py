from selenium import webdriver
import datetime
driver = webdriver.Chrome('./chromedriver')
driver.implicitly_wait(1)
driver.get('https://clinicaltrials.gov/ct2/resources/trends')
driver.implicitly_wait(1)

table = driver.find_elements_by_class_name('ct-data_table.ct-trends_table')

f = open("./result_of_tables.txt", 'w')

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