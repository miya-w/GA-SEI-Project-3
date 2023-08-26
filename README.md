
# General Assembly SEI Project 3 - UniMate
[UniMate](https://project3-realstate-c135ee1a757c.herokuapp.com/)
By team of [Alireza](https://github.com/Alirezanava72),[Miya Miah](https://github.com/miya-w)
## Overview
![web-home](https://github.com/Alirezanava72/project3/blob/main/README-img/web-home.png)
---
The third project of the software engineering immersive course at GA Australia. The assignment was to create a full-stack application with Python, Django, SQL. This project was completed in a team of 2 within a week.
About **UniMate**. It’s a platform is designed for university students seeking hassle-free accommodation solutions. Whether you're on the hunt for the perfect shared room or looking for a compatible housemate to share your space with.
- Property detail
![web-details](https://github.com/Alirezanava72/project3/blob/main/README-img/web-property-detail.png)
- Amenity
![web-amenity](https://github.com/Alirezanava72/project3/blob/main/README-img/web-amenity.png)
- Amenity details
![Amenity details](https://github.com/Alirezanava72/project3/blob/main/README-img/web-property-details-amenity.png)

## Table of Contents
1. [Brief](#Project-Brief)
2. [Technologies used](#Technologies-Used)
3. [Approach](#Approach)
    - [Planning](#Planning)
    - [Back-end](#Back-end)
    - [Front-end](#Front-end)
- [Challenges and Lessons Learned](#Challenges-and-Lessons-Learned)
- [Wins](Wins)
- [Future Features and Improvements](#Future-Features-and-Improvements)

## Project Brief
- Build a full-stack application

## Technologies Used

* HTML
* CSS
* JavaScript
* Python
* Django
* SQL

## Approach

### Planning
We began our project with a discussion of our ideas and quickly agreed to make a website we both are interested in -- a property rental website. To have a different niche in the market, we want to create a platform exclusively for uni students searching for a room or roommate in Australia.

So, these are the functions needs to meet the needs

- As a user, I want to add the room for renting 
- As a user, I want to share the amenities the property provides.
- As a user, I want to see the list of the renting room.
- As a user, I want to see the lease date and rent.

After settling on the needs we began to build up our project:

1. We set up our goals and our priorities in common. Then use Trello to assign the jobs. For collaboration, we agreed to separate the job into the back-end and Front-end.   
2. Discuss how to design the models for our UniMate application.
3. While the back end is in process, Front end developer starts the UI with the wireframe and then draws it on Figma.
4. After the back-end developer finishes the Models, URLs and Views, the front-end developer starts the HTML and CSS.
5. Once we had make sure we finish and meet all requirements, we started to add the extra features.
6. Review and polish the code.



#### Figma and Trello
![Trello](https://github.com/Alirezanava72/project3/blob/main/README-img/trello.png)
We used **Trello** throughout the process as our project management tool. With this online tool, It's much easier to assign the job and schedule. We created the three main boards: todo, doing and done, which help us to make sure everything is on track.

![Figma](https://github.com/Alirezanava72/project3/blob/main/README-img/figma.png)
**Figma** is an online disign tool to create the UI.

## Deployment
UniMate has been deployed to Heroku. [Find me on Heroku](https://project3-realstate-c135ee1a757c.herokuapp.com/)
Heroku is a platform-as-a-service (PaaS) that allows you to deploy, manage, and scale web applications without needing to manage infrastructure. It supports various programming languages, including Python, and provides tools to simplify deployment and application management which we have used to deploy the Unimate web application.

#### MVT (Model View Template)
Our first goal to work toward was our MVT, so we planned out what we would ideally like to have in the initial working version of our application:

#### ERD(entity relationship diagram)
![ERD](https://github.com/Alirezanava72/project3/blob/main/README-img/erd.png)
- Property has a many-to-many relationship with Amenity. A property can have multiple amenities, and an amenity can be associated with multiple properties.
- Property has a one-to-many relationship with Renting. One property can have multiple rental listings.
- Property has a one-to-many relationship with Photo. Many rental listings are associated with one property.

## Back end:

Since our application is built around various types of property listings, each with its specific attributes, we have established a set of diverse models. These models include Property, Amenity, and Renting, alongside the central user model, to form the core of our backend infrastructure.

### Models: 

Property: This model represents a property listing with various attributes such as title, address, suburb, state, postcode, details, price, and a Many-to-Many relationship with amenities.

```python
class Property(models.Model):
  title = models.CharField(max_length=50)
  address = models.TextField(max_length=200)
  suburb = models.CharField(max_length=50)
  state = models.CharField(max_length=3)
  postcode = models.IntegerField()
  details = models.TextField(max_length=200)
  price = models.IntegerField()
  amenities = models.ManyToManyField(Amenity)
```

Amenity: This model represents different amenities that a property can have, like features or facilities. Each amenity is described by its name.

```python
class Amenity(models.Model):
  name = models.CharField(max_length=100)
```

Renting: This model represents a renting option associated with a specific property. It includes details such as the available date and purpose (house sharing, room sharing, entire property).

```python
class Renting(models.Model):
    available_date = models.DateField('availability Date')
    purpose = models.CharField(
      max_length=1,
      choices=PURPOSES,
      default=PURPOSES[0][0]
      )

```
###  Views:

In “views.py” file, we defined various view functions and class-based views to handle different actions and interactions with the above models:
-  home and about: 
Render simple templates for the home and about pages.
- properties_index: 
Retrieve all properties from the database and render them on the index page.
- properties_detail:
 Retrieve detailed information about a specific property, including its associated amenities and a form to add a new renting option.
- Property Add, PropertyUpdate, PropertyDelete: 
Class-based views for creating, updating, and deleting properties(full CRUD functionality).
add_renting: To handle adding a new renting option to a property.
- AmenityList, AmenityDetail, AmenityCreate, AmenityUpdate, AmenityDelete: 
Class-based views for listing amenities, showing individual amenity details, creating, updating, and deleting amenities(full CRUD functionality).
- assoc_amenity and unassoc_amenity:
To associate or disassociate an amenity with a property.

### URLs:

In “urls.py” file, we’ve defined URL patterns that map to the respective views for different actions and interactions:
URLs related to properties, including property detail, creation, updating, and deletion.
URLs related to renting options, including adding a new renting option.
URLs related to amenities, including listing amenities, showing details, creating, updating, and deleting amenities.
### Forms:

“forms.py” file is defined with RentingForm class that inherits from ModelForm. This form is used for creating renting options associated with a property, allowing users to input the available date and purpose.</br>

Our Django project follows the Model-View-Template (MVT) architecture, where models represent data structures, views handle the logic and interactions, and templates render the user interface.This project focuses on managing property listings, associated amenities, and renting options through well-structured views and models. The provided URLs help to route requests to the appropriate views, and forms simplify the process of collecting user input for creating new renting options.
## DATABASES:

We have used PostgreSQL as the database backend which allows Django to establish a connection to the specified PostgreSQL database. 

---
### Front-end

![Phone](https://github.com/Alirezanava72/project3/blob/main/README-img/web-phone.png)
#### Responsive

- In this project, we didn't use any CSS framework, so it took us some time to do the Responsive Web Design. We used the developer tool to debug. A good example is the front end set the sections in vh hight and it causd the fail of responsive web design.
- In Django, it has the Material style by default, we keep it so this project can be done before the deadline.  It's a bit challenging to integrate the design with the new CSS and the existing Material CSS.


## Challenges and Lessons Learned
### Using Git collaboratively 
This was our first project where we coded collaboratively using Git - allowing us to understand the complexities of merging and conflict resolution. Working as a team with Git was challenging, especially when we had any miscommunication and it might cause conflicts. During this project, we didn't reach an agreement on the way to commit to Git, so it took us some time to fix the problem of the branch that was created to merge with the main. Git is definitely the biggest lesson in this project.
### Smart Team Work By Using the Online Tools. 
Each team member was assigned specific cards representing tasks or objectives within the project in Trello. We recognized early on that clear task descriptions were import. This approach ensured that our project remained on track. 

### communication, communication, communication
As we learned from Git co-work, communication was important. discuss tasks, share insights, and provide updates. Daily check-ins, Git commits, were scheduled to review progress and resolve any ambiguities. Apart from code, communication is a big part of team work.

# Wins
- Teamwork - This is the first group project in this boot camp, it was challenging at points,but it was overall an incredibly valuable experience as we learnt how to work as part of a team while building a full-stack application across lots of components. 

## Future Features and Improvements
- Create the public List 
- Create the space for the properties list and roomamte list
- Improve the UI and UX for user to creat the amenity list.
- Using the Google Map API to calculate the distance

### Resources
---
[Project 3 - brief](https://git.generalassemb.ly/seir66anz/project-3-brief)
[Project 3- link](https://project3-realstate-c135ee1a757c.herokuapp.com/)