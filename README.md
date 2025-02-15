# destinationguides-backend
Backend server for SWE (simulated work environment) in group 1 - Destination Guides

## Setup Guide

Please see the [Postman API Documentation]([url](https://documenter.getpostman.com/view/35026527/2sAYXEDdZs)).

1. Clone the repository.
2. Navigate to the created directory using ```cd```.
3. Activate the Pipenv environment with ```pipenv shell```.
4. Install the dependencies using ```pipenv install```.
5. Open the project in Visual Studio Code.
6. Ensure that the correct interpreter is selected.
7. Make migrations with ```python manage.py makemigrations``` (or ```python3 manage.py makemigrations``` if on Mac)
8. Load the migrations with ```python manage.py migrate``` (or ```python3 manage.py migrate``` if on Mac)
9. Load fixtures with the following (in order):
  - Load the users fixtures with ```python manage.py loaddata users``` (or ```python3 manage.py loaddata users``` if on Mac)
  - Load the categories fixtures with ```python manage.py loaddata categories``` (or ```python3 manage.py loaddata categories``` if on Mac)
  - Load the regions fixtures with ```python manage.py loaddata regions``` (or ```python3 manage.py loaddata regions``` if on Mac)
  - Load the countries fixtures with ```python manage.py loaddata countries``` (or ```python3 manage.py loaddata countries``` if on Mac)
  - Load the posts fixtures with ```python manage.py loaddata posts``` (or ```python3 manage.py loaddata posts``` if on Mac)
  - Load the tags fixtures with ```python manage.py loaddata tags``` (or ```python3 manage.py loaddata tags``` if on Mac)
  - Load the post_tags fixtures with ```python manage.py loaddata post_tags``` (or ```python3 manage.py loaddata post_tags``` if on Mac)
  - Load the comments fixtures with ```python manage.py loaddata comments``` (or ```python3 manage.py loaddata comments``` if on Mac)
10. Run ```python manage.py runserver``` (or ```python manage.py runserver``` if on Mac) to run the server

## About the User
- The ideal user for this application is anyone who wants to travel
- Travel writes are also the ideal users for this application to create content for the other users
- The problem this app solves for them is that it creates a central place for travelers to learn about destinations and/or share their travel expertise

## Features
- Create, Read, Update, and Delete posts
- Create, Read, Update, and Delete comments on posts
- Create, Read, Update, and Delete user profiles
- Create, Read, Update, and Delete user tags
- Create, Read, Update, and Delete postTags (many-to-many relationship between posts and tags)
- Create, Read, Update, and Delete countries, regions, and categories

## Video Walkthrough of Simply Books Django server assessment
Coming soon!

## Relevant Links
Please see the [Postman API Documentation]([url](https://documenter.getpostman.com/view/35026527/2sAYXEDdZs))

## Code Snippet

<!-- // Post Model -->

```
class Post(models.Model):
  
  title = models.CharField(max_length=50)
  author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
  category = models.ForeignKey(Category, on_delete=models.CASCADE)
  body = models.CharField(max_length=280)
  country = models.ForeignKey(Country, on_delete=models.CASCADE)
  region = models.ForeignKey(Region, on_delete=models.CASCADE)
  image = models.URLField()
  created_at = models.DateTimeField(auto_now_add=True)
  
  class Meta:
    ordering = ("-created_at", "region", "country")
```

## Contributors
- Cody Keener (https://github.com/codyKeener)
- Sawak Keo (https://github.com/skeoswf)
- Jordan Youssef (https://github.com/Jayoussef28)
