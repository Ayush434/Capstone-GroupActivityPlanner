# Capstone Project "Group Activity Planner"

## About
Website to let users make their groups and add new members who are registered on the website. In the group, members can post a activity with title, instructions and the meeting time and location of the activity


## Distinctiveness and Complexity
Group activity planner website is more about planning an activity or just throwing out an idea to the group and see if anyone would be interested or not to participate in the activity. The group will not be posting anything to sell or buy from them or providing anything to entertain but rather simplying creating an activity with instructions, meeting time and location. Members can comment on the activity and choose "yes" or "nah" to indicate if they are going or not.

In older projects of this course, I noticed how we went from building websites using Django and manipulating data/rendering pages through python. Then later in the course when Javascript/React was taught, i noticed that there are some usecases where javascript is more helpful and efficient than Django like adding new a item to the div, changing / updating data and many more things without rendering the page. Thats where i thought to build my final project by combining both of them and using the right tools where needed. 


## Info about the files that I created

 - urls.py - this file controls all the routes of the website. You can check which route belongs to what view and what type of parameters does it accept.

- layout.html - this file is the base web page of all the html pages. I have defined some blocks which is the placeholder for html that other file will be adding on top of this base webpage.

- index.html - If the user is not loged in, this webpage will display some info about the website and some buttons to login/register. If the user is logged in, this file will display the groups thatr user has created or is member of but if the user doesn't have any groups, it will display a message.

- showGroup.html - If the user is logged in, this file will display the members of the group that user has selected. User should be able to add a new member to the group from this file.

- groupActivities.html - If the user is logged in, this file will display all the activities for the group that is currently selected. It will only display the title, meeting time and location of the activity but not the comments or instructions.

- viewActivity.html - if the user is logged in, this file will display the activity which is currently selected by the user. It will display all the info about the activity and also let users add comments and let the people know if they are coming or not.

- createGroup.html - if the user is logged in, this file will display a form to let user create a new Group.

- createActivity.html - if the user is logged in, this file will display a form to let user create a new activity for the currently selected group.

- styles.css - some styling for the body and nav bar

- activity.css - styling for the cards which are displaying activities

- viewactivity.css - some styling for the currently selected activity

- showGroup.js - some functionality to what to do when a new member is added

- viewActivity.js - some functionality to what to do when a new comment is added


## How to Run the application
1. Make sure you have downloaded the zip folder of the application and unzipped it. 
2. Open PowerShell and Change directory to where manage.py is in the application folder. Should be in the 1 level up from root folder eg - ./capstone/manage.py
3. You will need to make migration before running application. Run below commands to make and apply migrations
py manage.py makemigrations GroupPlanner
py manage.py migrate
4. Now you can run the application using this command:
py manage.py runserver

Note: If you face any errors about python or django, please make sure you have python and django installed on your system.

- Python - https://www.python.org/downloads/

- Django - https://docs.djangoproject.com/en/4.1/topics/install/
