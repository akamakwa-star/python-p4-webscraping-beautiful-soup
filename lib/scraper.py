from bs4 import BeautifulSoup
import requests

# Add headers to avoid 403 Forbidden errors
headers = {'user-agent': 'my-app/0.0.1'}

# -------------------------------
# SCRAPE MAIN PAGE HEADING
# -------------------------------
url = "https://flatironschool.com/"
response = requests.get(url, headers=headers)

doc = BeautifulSoup(response.text, 'html.parser')

# Get the main heading text
heading = doc.select('.heading-financier')[0].contents[0].strip()
print("Main Heading:")
print(heading)

# -------------------------------
# SCRAPE COURSE TITLES
# -------------------------------
courses_url = "https://flatironschool.com/our-courses/"
courses_response = requests.get(courses_url, headers=headers)

courses_doc = BeautifulSoup(courses_response.text, 'html.parser')

courses = courses_doc.select('.heading-60-black.color-black.mb-20')

print("\nCourses Offered:")
for course in courses:
    print(course.contents[0].strip())
