[![Build Status](https://travis-ci.org/GrantMCA93/Project5-Full-Stack-Frameworks.svg?branch=master)](https://travis-ci.org/GrantMCA93/Project5-Full-Stack-Frameworks)



# Project5-Full-Stack-Frameworks

1. Heroku App: https://project5-full-stack-frameworks.herokuapp.com/
2. Heroku git: https://git.project5-full-stack-frameworks.git
3. GitHub: https://github.com/GrantMCA93/Project5-Full-Stack-Frameworks

This Project is designed to allow users to search through house listings in an easy to use interactive way, to find your dream spanish home.
The website allows the user the created there own account to list there own home. 

#UX
This website is designed for people searching for their dream spanish home.
The website allows you to list your property and receive messages from potential buyers.
If yur search for a house theres a number of difference search parameters that the website provided to help you find the perfect house.
If you has any issues with the website or the listings or a user is looking for more information there is a contact page.

Here is a list of other house listing websites i viewing when designing this website
1.https://www.aplaceinthesun.com/spain
2.https://www.aplaceinthesun.com/spain
3.https://www.idealista.com/en/properties-for-sale-in-spain
4.https://www.kyero.com/en/spain-property-for-sale-0l55529

#Features

##Existing Features
1. Accounts folder is for accounts to be registered, login, logout, view and edit profile
2. Ecommerce foler is send the project elements together.
3. Enquires folder is to allow the users to send direct messages to each other about listings.
4. Listing folder is to allow the user to add a property, edit property, search for houses, view detailed information about those houses.
5. Pages folder contains the index, contact and contact thank you pages of the website. 
6. Static folder contains the CSS, JS and font-awesome files.
7. The templates folder contains the partial elements for other files and the registration files for password changes.

##Features Left to Implement
1. The search form is basic and could be improved be providing more search parameters.
2. Edit house validation error, when editing listing the images must be uploaded again.
3. The website design could be improved to be more visually apealling.
4. Had Issue with the used profile so unable to change phone number after account is created

#Technologies Used

1. 	Bootstrap ( https://getbootstrap.com/ ) 	Bootstrap was used to mobile-first design of the website.	
2. JQuery (https://jquery.com/ ) 	JQuery is used to provide DOM manipulation.
3. Python (https://www.python.org/ ) Python is used to automate sprecific tasks within the project.
4. Json (https://www.json.org/) Json is used for transmitting data between the server and webb application. 
5. Heroku ( https://www.heroku.com/home ) Heroku is used to Host the website.


#Testing
I’ve tested the code in chrome, Firefox, Microsoft edge browser and safari as well as the mobile versions of these browsers. I used W3C for CSS https://jigsaw.w3.org/css-validator/and HTML https://validator.w3.org/ to remove errors.


Contact form:
Go to the "Contact Us" page
Try to submit the empty form and verify that an error message about the required fields appears
Try to submit the form with an invalid email address and verify that a relevant error message appears
Try to submit the form with all inputs valid and verify that a success message appears.
In addition, you should mention in this section how your project looks and works on different browsers and screen sizes.

You should also mention in this section any interesting bugs or problems you discovered during your testing, even if you haven't addressed them yet.

If this section grows too long, you may want to split it off into a separate file and link to it from here.

#Deployment
This section should describe the process you went through to deploy the project to a hosting platform (e.g. GitHub Pages or Heroku).
The project is pushed to github process used - link cloud9 to github git remote add origin https://github.com/GrantMCA93/Project5-Full-Stack-Frameworks.git git add . git commit -m "" <-- in quote marks describe changes made --> git push -u origin master

The code is run locatally using the command "python3 manage.py runserver $IP:$C9_PORT"

The media images are hosting on https://s3.console.aws.amazon.com/s3/buckets/project5-full-stack-frameworks/?region=eu-west-1&tab=overview

The projects is hosted on Github pages, Heroku

#Credits

##Content
The text for section Y was copied from the Wikipedia article Z

##Media
The photos used in this site were obtained from ...

##Acknowledgements
Mentor:- Chris Zielinski  ckz8780@gmail.com 
insperation for the project was taken from - https://github.com/MiroslavSvec/project-5