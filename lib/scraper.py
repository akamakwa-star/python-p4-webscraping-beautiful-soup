
from bs4 import BeautifulSoup
import requests

# 1️⃣ Define headers to avoid 403 Forbidden errors
headers = {'user-agent': 'my-app/0.0.1'}

# 2️⃣ Target URL (Flatiron School courses page)
url = "https://flatironschool.com/our-courses/"
response = requests.get(url, headers=headers)

# 3️⃣ Parse the HTML
doc = BeautifulSoup(response.text, 'html.parser')

# 4️⃣ Select all course containers
# Inspect the site to find a reliable CSS selector
course_elements = doc.select('.course-card')  # Each course is inside a div with class "course-card"

# 5️⃣ Extract and print course info
for course in course_elements:
    # Course title
    title_tag = course.select_one('.course-card__title')
    title = title_tag.get_text(strip=True) if title_tag else "No title"

    # Course description
    desc_tag = course.select_one('.course-card__description')
    description = desc_tag.get_text(strip=True) if desc_tag else "No description"

    # Course URL
    link_tag = course.select_one('a')
    link = link_tag['href'] if link_tag else "No URL"

    # Print info
    print("Title:", title)
    print("Description:", description)
    print("URL:", link)
    print("-" * 50)
