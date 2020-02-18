from web_scrap_source import *
from colors import *

# Ask's the user for some basic information on what job/career they are looking for & the location
user_job_want = input('Type the job/career you are looking for: ').lower()
user_job_location = input('Type the city name you would like this job/career to be: ' + red + '\n'
                          'If your looking for a remote position type remote: ' + end)
print('\n')

user_site_combination = 'https://www.monster.com/jobs/search/?q=' + user_job_want + '&where=' + user_job_location

url = user_site_combination
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find(id='ResultsContainer')
#print(results.prettify())

job_elements = results.find_all('section', class_='card-content')
# .find_all() returns a iterable containing all the HTML for all the job listings displayed on the user's
#  page link that they have provided @ url

for job_element in job_elements:
    '''  print(job_elements, end='\n'*2)
# This shows the info regarding the jobs in a bit more in-depth info
'''
    job_title_element = job_element.find('h2', class_='title')
    # Further job filtering to ensure the user gets the job postings that they want to see
    job_filter = results.find_all('h2', string=lambda text:user_job_want in text.lower())
    # links the program to the job link. This will give the user an
    # ability to further read the job posting info
for posted_job in job_filter:
    link = posted_job.find('a')['href']
    print(posted_job.text.strip())
    print(f"Click here to apply: {link}\n")

    company_name_element = job_element.find('div', class_='company')
    location_element = job_element.find('div', class_='location')


# Checks if the data is N/A it will tell the program just to continue
    if None in (job_title_element, company_name_element, location_element):
        continue


# RED = Job Title, # Green = Company Name, # Blue = Job/Buisness Location
    print(red + bold + str(job_title_element.text.strip()) + end)
    print(green + bold + str(company_name_element.text.strip()) + end)
    print(blue + bold + str(location_element.text.strip()) + end)
    # Spaces between the other job postings
    print()

# if the user keyword has no results, it will notify them of the issue and ask them to refine their input, else
# it will tell them the number of times their keyword pops up on the site
if len(job_filter) == 0:
    print('You have' + bold + red + ' no matches' + end + ', for your keyword: ' + bold + yellow +
          str(user_job_want).capitalize() + end + '. Please refine your keyword/location.')
else:
    print('Total job matches for your keyword: ' + bold + yellow + str(user_job_want).capitalize() + end +  bold + red +
      ' #' + str(len(job_filter)) + end)




