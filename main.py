from bs4 import BeautifulSoup

with open('home.html', 'r') as html_file:
    content = html_file.read()
    
    
    soup = BeautifulSoup(content,'lxml' )
    # tags = soup.find('h5')  # find method searches only for first tag
    # courses_html_tags = soup.find_all('h5' ) # find method searches for all tags 
    # for course in courses_html_tags:
    #     # print(course) # This prints the whole tag 
        
    #     print(course.text) # This prints only the text in tag
    
    course_cards = soup.find_all('div', class_ = 'card')
    for course in course_cards:
        course_name = course.h5.text
        course_price = course.a.text.split()[-1]
        print(f'{course_name} course costs {course_price}')
        # print(course_name)
        # print(course_price)
        