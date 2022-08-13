# St Patrick's Day Banquet Booking System - Testing


## Table of Contents
* [User Story Testing](#user-story-testing)
  * [Admin](#admin)
  * [User](#user)
* [Responsive Design](#responsive-design)
* [Validators](#validators)
  * [HTML](#html)
  * [CSS](#css)
  * [Python](#python)
* [Issues and Bugs](#issues-and-bugs)


## User Story Testing
- Family members were asked to use the site to determine whether the set aims were achieved

### Admin
- Reusability
  - As an administrator with no coding knowledge, I can change the details of the event to use it for future events. This is achieved using a form on the homepage accessible only by the admin, or through the admin panel.
- Admin Panel
  - As an administrator, I can create and delete bookings so that I have an overview of the attendance for my event.  The admin panel provides all information delivered by users.
- Totals
  - As an administrator, I can get a total number of meal types so that I can easily see how many of each type of meal needs to be prepared.  In the bookings panel, the bookings are listed by booking number and show columns for adult meat and vegetarian meal options and child meals.  At the top of each column, the totals of all columns are calculated.
- Payment
  - As an administrator, I can mark bookings as paid or unpaid in order to have an overview of how many people have paid.  Each booking has a payment boolean field that can be changed in the admin panel and is reflected in the booking detail view.

### User
- Login
  - As a Site User, I can create a profile so that I can log in and manage my bookings.  The site utilises Django AllAuth to manage account creation.
- Bookings
  - As a user, I can make a booking so that I or others can attend the event.  The site has a simple form that is accessible to anyone logged in to the site.  It includes the ability to select the number of adult meat dishes, adult vegetarian dishes, and child meals.  There is also the ability to request a high chair and note any dietary restrictions such as allergies or celiac disease.
- Updating
  - As a Site User, I can edit or delete my booking so that I can add more people to my group or change my mind about going. After booking, a list of all the user's bookings can be viewed and then individually selected.  This presents the user with payment information and the ability to change any of their totals or delete the booking entirely.


## Responsive Design
- Each page of the site was viewed in a variety of device sizes through Chrome's developer tools to make adjustments allowing for clean display of the website on as many devices as possible.


## Validators
- HTML
  - No warnings or errors were reported when run through the [W3C Validator](https://validator.w3.org/#validate_by_input).  As the presence of django tags caused the validator to throw out numerous errors, each page was loaded, then I utilised view page source and copied the html to the validator this way.
- CSS
  - No warnings or errors were returned when run through the [Jigsaw Validator](https://jigsaw.w3.org/css-validator/#validate_by_input)
- Python
  - All python code was run through [PEP8](http://pep8online.com/)
- More in depth information regarding testing can be found [here](https://github.com/notandy82/st-patricks-banquet/blob/main/TESTING.md)


## Issues and bugs
- Users can view, edit, or delete bookings made by other users by changing the booking number in their browser address bar.  This was fixed by adding UserPassesTestMixin to the BookingEdit, DeleteBooking and BookingDetail views.
- Users can access the form to change event details which should only be accessible to the admin.  This was fixed by adding UserPassesTestMixin to the PostEdit view.
- Script to display a user's cost doesn't display anything if any of the meal choices is 0.  It was found that a field of 0 was returning "None" and code was added to address this.