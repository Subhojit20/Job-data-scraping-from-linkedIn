# %%
import pandas as pd 
import re 
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys 


# %%
browser = webdriver.Chrome(r"...\chromedriver.exe")
browser.get("https://www.careerguide.com/career-options")

# %%
categories = browser.find_elements_by_class_name("c-font-bold")
category_list = []
for category in range(1,len(categories)-12):
    category_list.append(categories[category].text)
print(category_list)

# %%
sub_categories = browser.find_elements_by_class_name("c-content-list-1")
sub_category_list = []
for sub_category in sub_categories:
    sub_category_list.append(sub_category.text.replace("\n",",").split(","))
print(sub_category_list)


# %%
browser = webdriver.Chrome(r"...\chromedriver.exe")
browser.get("https://www.linkedin.com")

# %%
username = browser.find_element_by_id("session_key")
username.send_keys("...@gmail.com")
password = browser.find_element_by_id("session_password")
password.send_keys("...")

# %%
login_button = browser.find_element_by_class_name("sign-in-form__submit-button")
login_button.click()

# %%
browser.get("https://www.linkedin.com/jobs/search")

# %%
search_jobs = browser.find_element_by_id("jobs-search-box-keyword-id-ember30")
search_jobs_by_location = browser.find_element_by_id("jobs-search-box-location-id-ember30")
search_jobs.send_keys(category_list[0])
search_button = browser.find_element_by_class_name("jobs-search-box__submit-button")
search_button.click()

# %%
searched_jobs = browser.find_elements_by_class_name("full-width.artdeco-entity-lockup__title.ember-view")
company_job1 = []
for i in searched_jobs:
    company_job1.append(i.text)
search_jobs.clear()
search_jobs_by_location.clear()
print('Job Category:',category_list[0])

# %%
print('{0}\n\nNumber of Jobs: {1}'.format(company_job1, len(company_job1)))

# %%
location = browser.find_elements_by_class_name("job-card-container__metadata-item")
location_name = []
for i in range(len(location)):
    location_name.append(location[i].text)

for y in location_name:
    if y == 'Remote' or y == 'On-site' or y == 'Hybrid':
        location_name.remove(y)

state_name = []
for i in location_name:
    loc = i.split(",")[1:-1]
    for q in loc:
        state_name.append(q[1:])

print('{0}\n\nNumber of state searches: {1}'.format(state_name, len(state_name)))

# %%
search_jobs_by_subcategory = browser.find_element_by_id("jobs-search-box-keyword-id-ember30")
search_jobs_by_subcategory.send_keys(sub_category_list[0][1])
search_jobs_by_state = browser.find_element_by_id("jobs-search-box-location-id-ember30")
search_jobs_by_state.send_keys(state_name[0])
search_button = browser.find_element_by_class_name("jobs-search-box__submit-button")
search_button.click()
search_jobs_by_subcategory.clear()
search_jobs_by_state.clear()

# %%
company_offering_job = browser.find_elements_by_class_name("job-card-container__metadata-item.job-card-container__metadata-item--workplace-type")
company_offering_job_list = []
for i in company_offering_job:
    company_offering_job_list.append(i.text)
    
print('{0}\n\nCount of companies offering jobs at: {1}'.format(company_offering_job_list, len(company_offering_job_list)))

# %%
company = browser.find_elements_by_class_name("job-card-container__company-name")
company_name = []
for i in company:
    company_name.append(i.text)

print('{0}\n\nNumber of companies: {1}'.format(company_name, len(company)))

# %%
location = browser.find_elements_by_class_name("job-card-container__metadata-item")
location_name = []
for i in range(len(location)):
    location_name.append(location[i].text)

for y in location_name:
    if y == 'Remote' or y == 'On-site' or y == 'Hybrid':
        location_name.remove(y)

print('{0}\n\nNumber of locations: {1}'.format(location_name, len(location_name)))

# %%
job_disc = browser.find_elements_by_class_name("jobs-description-content__text--stretch")
discription = []
for i in job_disc:
    discription.append(i.text)
for j in discription:
    print(j)

# %%
comp_page = browser.find_element_by_class_name("artdeco-entity-lockup__title.ember-view.t-20")
comp_page.click()

# %%
company_page_about = browser.find_elements_by_class_name("org-page-navigation__item.m0")
company_page_about[1].click()

# %%
company_discription = browser.find_element_by_class_name("break-words.white-space-pre-wrap.mb5.text-body-small.t-black--light")
company_discription_list = []
company_discription_list.append(company_discription.text)
for i in company_discription_list:
    print(i)

# %%
employee = browser.find_element_by_class_name("text-body-small.t-black--light.mb1")
employee_list = []
employee_list.append(employee.text)
print(employee_list)

# %%
company_location = browser.find_elements_by_class_name("t-14.t-black--light.t-normal.break-words")
company_location_list = []
for i in company_location:
    company_location_list.append(i.text)
print(company_location_list)

# %%
col1 = ["Categories", "Sub Categories", ]
df1 = pd.DataFrame()
dict = {}
Catagories = category_list
Sub_Catagories = sub_category_list
for i in range(len(Catagories)):
    for x in range(len(Catagories)):
        dict[Catagories[i]] = Sub_Catagories[i][0:]

df1.append(dict, ignore_index="True")

# %%
df1.head()

# %%
col2 = ["Sub Categories", "Job Positions", "Company Offering Job", "Company_Name", "State", "Location Name"]
df2 = pd.DataFrame({"Sub Catagories":sub_category_list[0][0], "Job Positions":company_job1[:5], "Company Offering Job":company_offering_job_list[:5], "Company_Name":company_name[:5], "State":state_name[:5], "Location Name":location_name[:5]})


# %%
df2.head()

# %%
col3 = ["Categories", "Job Positions", "Company Offering Job", "Company_Name", "Location Name", "Job Discription", "Company Discription", "Employee List", "Company Location List"]
df3 = pd.DataFrame({"Catagories":category_list[:1], "Job Positions":company_job1[:1], "Company Offering Job":company_offering_job_list[:1], "Company_Name":company_name[:1], "Location Name":location_name[:1], "State":state_name[:1], "Job Discription":discription[:1], "Company Discription":company_discription_list[:1], "Employee":employee_list[:1]})

# %%
df3.head()

# %%
df1.to_csv("Catagories_and_Sub_Categories.csv")
df2.to_csv("Particular_Sub_Categary.csv")
df3.to_csv("Particular_Job_and_its_details.csv")


