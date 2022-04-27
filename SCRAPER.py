from bs4 import BeautifulSoup as bs 
import requests
import csv
import pandas
r=requests.get("https://www.careerguide.com/career-options")
soup=bs(r.content, 'html.parser')
soup.prettify()

def scrap_data(items):
    col_md=items.find_all('div',class_="col-md-4")
    

    for col in col_md:
        title =col.h2.a.text.replace('/',' ').replace('&','')
        title_list=col.find_all('a')
        list2=[]
        for listitems in title_list:
            list2.append(listitems.text.replace('/',' ').replace('&',''))
        dict2[title]=list2
    #for k,v in dict2.items(): 
        #print(f"{k}:{v}")
    return dict2
def find_jobs(i): 
        job_list=[]
        loc=['Andhra Pradesh','Arunachal Pradesh','Assam','Bihar','Chhattisgarh','Goa','Gujarat','Haryana','Himachal Pradesh','Jharkhand','Kerala','Madhya Pradesh','Maharashtra','Manipur','Meghalaya','Mizoram','Nagaland','Odisha','Punjab','Rajasthan','Sikkim','Tamil Nadu','Telangana','Tripura','Uttar Pradesh','Uttarakhand','West Bengal','Andaman and Nicobar Islands','Chandigarh','Dadra and Nagar Haveli and Daman and Diu','Delhi','Jammu and Kashmir','Ladakh','Lakshadweep','Puducherry']        
        for items in loc:
            url="https://in.linkedin.com/jobs/search?keywords={}&location{}=&geoId=&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0".format(i,items)   
            r=requests.get(url)
            loup=bs(r.content, 'html.parser')
            k=loup.prettify()
            print(k)


    
            
info_box=soup.find('div',class_="c-body")
row_content=info_box.find_all('div',class_="row")
record=[]
dict2={}
for items in row_content:
    scrap_data(items)
del dict2['Institutes in India']
del dict2['Exams and Syllabus']
#del dict2['Gems  Jewellery']
#for k,v in dict2.items():
    #print(f"{k}:::{v}")

job_list=[]
dict3={}

for key in dict2.keys():
    for i in dict2.get(key):
        
        find_jobs(i)    
        #listt=dict2.get(key)
        
        #dict3[key]=dict2.get(key)
        #print(" {} : {}".format(key,i))
         

