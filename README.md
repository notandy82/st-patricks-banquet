# St Patrick's Day Banquet Booking System

![Responsive view mockup](assets/images/amiresponsive_nis.png)
The Norwegian Irish Society is a group of Irish immigrants and expats living in Norway.  Their goal is to help other Irish people living in and around Oslo retain their connection to Ireland.  Included in their efforts is a yearly banquet held for St Patrick's Day.  This has proven to be very popular with almost 200 attendees.  The attendence and paying has previously been handled through emails and phone calls which is less than ideal.  This system provides a way for the group to organise their event with much greater ease.
Live demo [_here_](https://nisbanquet.herokuapp.com/)


## Table of Contents
* [User Experience (UX)](#user-experience)
  * [User Stories](#user-stories)
* [Design](#design)
* [Features](#features)
  * [Existing Features](#existing-features)
  * [Features to Implement](#features-to-implement)
* [Technologies Used](#technologies-used)
* [Testing](#testing)
* [Deployment](#deployment)
  * [GitHub](#github)
  * [Heroku and Django](#heroku-and-django)
* [Credits](#credits)
* [Contact](#contact)


## User Experience (UX)
A user of this booking system fall into two categories.  The first is a person or group organising the banquet. The second is any person wanting to attend the St Patrick's Day banquet.

### User Stories
- Admin
  - As an administrator, I would like to be able to reuse the site for future events without having to adjust the code.
  - As an administrator, I would like to be able to get a quick overview of how many of each type of meal is needed for the event.
  - As an administrator, I would like to be able to note which bookings have been paid for.
-User
 - As a user, I would like to be able to create a user account on the site.
 - As a user, I would like to be able to create multiple bookings for the event.
 - As a user, I would like to be able to review and edit my bookings.
 - As a user, I would like to know how much the event will cost.


## Design

### Colour Scheme
The design of the site was intended to evoke a sense of "Irishness" and achieves this mainly through the colour scheme.  On a larger screen, the navbar utilises a color gradient, shifting from green to white to orange.  On mobile devices, the navbar and footer are a solid green.  The site is then accented with green and orange buttons for various tasks.

### Font
The fonts chosen for the site are Cormorant Garamond and Proza Libre.  Cormorant Garamond was chosen for the event title as it was felt it looked best, and then Proza Libre was chosen to pair with it for the rest of the content.

### Imagery
The site uses few images.  All images used are of the most recent location of the banquet.


## Features

### Existing Features
- Navbar
  - The navigation bar is located at the top of each page and contains links to other pages.
  - The links present in the bar will change based on the logged in status of the user.
    - A user not logged in will be provided with links to log in and register an account.
    - A user that is logged in will be provided with links to log out, create a new booking, or view any bookings that they've already created.
  - On smaller screens, the links will not be displayed but a button on the right side will display them in a drop-down menu.
![Mobile homepage](assets/images/homepage_mobile.png)

- Home page
  - The home page provides concise details about the event, including the location, time, and cost of the event.
  - A photo at the top of the screen provides a view of the location of the event.
  - When the logged in user is the administrator, a button is present that will take the administrator to a page to adjust the details of the event.
![Admin logged in homepage](assets/images/homepage.png)

- Booking page
 - The page provides a short form for the user to select how many people will be part of their booking.  These are divided up by the number of each type of meal that will be requested.

- View Bookings page
 - The page provides a list of all bookings that a user has made. 
 - Should the user not have any bookings, an image of the interior of the banquet hall is displayed.
 - Users with bookings will have a view of all of their bookings.
 - The details for how to pay are displayed.
 - Each booking is selectable to view in detail.
 - The detail view provides the cost due.
 - From the detail view, the user is able to edit or delete their booking.
![Detail view](assets/images/detail_page.png)

- Admin Panel
  - The admin panel provides the admin with the ability to manage users, bookings, and event information.
  - The booking section provides a list of each individual booking and a quick view of how many of each type of meal has been ordered in that booking.
  - The total number of each type of meal booked is calculated at the top of the booking.
![Admin panel column totals](assets/images/admin_panel_bookings.png)

### Features to Implement
- A reconfiguring of the main booking model to separate each booking into individual meals in order to apply allergy information to specific individuals.
- A model to create a seating assignment.


## Technologies Used

### Languages
- HTML 5 
- CSS 
- JavaScript 
- Python

### Libraries and Programs
- GitPod for building and editing code
- GitHub for storing code and deploying site
- Git for version control
- Django as a site framework
- Bootstrap for styling
- Google Fonts for site fonts
- Font Awesome for icons
- Balsamiq for initial development
- Favicon.io for favicon generating
- Heroku for project deployment


## Testing
- HTML
  - No warnings or errors were reported when run through the [W3C Validator](https://validator.w3.org/#validate_by_input)
- CSS
  - No warnings or errors were returned when run through the [Jigsaw Validator](https://jigsaw.w3.org/css-validator/#validate_by_input)
- Python
  - All python code was run through [PEP8](http://pep8online.com/)
- More in depth information regarding testing can be found [here](https://github.com/notandy82/st-patricks-banquet/blob/main/TESTING.md)


## Deployment
The site was deployed through GitHub and Heroku

### Github
 - The repository was created as follows:
   - Log in to GitHub
   - In the search bar, search for Code Institute's gitpod full template
   - Select Use this template
   - Fill in a repository name
   - Click Create repository from template
   - Click the greeen Gitpod button to create a new workspace

### Heroku and Django
 - The process of setting up Django and deploying to Heroku was done by following the Code Institute [cheatsheet](https://docs.google.com/document/d/1P5CWvS5cYalkQOLeQiijpSViDPogtKM7ZGyqK-yehhQ/edit)


## Credits

### Media
- Hero image taken by Rachel Marsili
- Additional photo taken by Sarah Fawsitt

### Content
- View clarification provided by Django documentation and [Classy Class-Based Views](https://ccbv.co.uk/)
  
- Thanks
  - Thanks to my family for their support and patience
  - Thanks to my mentor Adegbenga Adeye for his guidance


## Contact
Created by Andrew Stanek (notandystanek@gmail.com)