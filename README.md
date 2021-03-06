# Holly Thomas - Author Site

![README banner](https://github.com/LittleBlue418/Author-Site/blob/master/author_site_project/documentation/laptop-tablet-phone-pc.png)


The home of books by Holly Thomas! Read about the author, the world of the books and the inspiration behind some of her work. Visit the shop and pick up copies of her book, cuddly toys and more! Join our community and see your art featured in the gallery!
***

## Site


[Visit!](https://author-site.herokuapp.com/)

***

## Table of Contents
- [UX](#ux)
  * [Strategy and Planning](#strategy-and-planning)
  * [User Stories](#user-stories)
  * [Research and Prioritization](#research-and-prioritization)
  * [Scope](#scope)
  * [Structure](#structure)
    + [Design Decisions](#design-decisions)
    + [Surface](#surface)
    + [Skeleton](#skeleton)
    + [Database and App Design](#database-and-app-design)
  * [Features](#features)
  * [Technologies Used](#technologies-used)
  * [Testing](#testing)
  * [Deployment & Version Control](#deployment---version-control)
  * [Credits](#credits)
    + [Code](#code)
    + [Content](#content)
    + [Media](#media)
    + [Acknowledgements](#acknowledgements)

<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>

***

# UX

## Strategy and Planning

My UX design process focussed on a mobile first design that would allow users to navigate through the information and the shopping parts of the site easily. The whole site should be tied together with a unified structure and theme to give a clear brand and unified feeling. The overall feeling should be ‘magical’ and welcoming to readers of all ages.

## User Stories
<details>
    <summary>Click to see - User Stories</summary>

### User
* As a user I can read about the author.
* As a user I can see fan art that has been submitted & approved.
* As a user I can see an overview of the different series that the author has written.
* As a user I can read about each series that the author has written.
* As a user I can see an overview of all of the books that the author has written.
* As a user I can see which products are available and which are out of stock.
* As a user I can read a detailed description about each book that the author has written.
* As a user I can add products to my shopping bag.
* As a user I can remove products from my shopping bag.
* As a user I can view my shopping bag.
* As a user I can purchase the items in my shopping bag
* As a user I can create an account.
* As a user I can log into my account.

### Logged In User
* As a logged in user I can log out of my account.
* As a logged in user I can delete my account.
* As a logged in user I can save my payment details.
* As a logged in user I can edit my profile details.
* As a logged in user I can view my order history.
* As a logged in user I can view the shipping status of my order.
* As a logged in user I can submit fan art.
* As a logged in user I can see fan art that I have submitted.
* As a logged in user I can delete fan art that I have submitted.

### Admin
* As an admin user I can view & approve submitted fan art
* As an admin user I can add products
* As an admin user I can edit products
* As an admin user I can view customer orders
* As an admin user I can set the status of each product (in stock or out of stock)
* As an admin user I can hide unavailable products from the shop.
* As an admin user I can set the shipping status for each product

</details>

## Research and Prioritization

<details>
    <summary>Click to see - Research & Prioritization Table</summary>


&nbsp;

Opportunity / Problem | Importance | Feasibility
----------------------|-------------|----------------------
A - Display information about the books & the author | 5 | 5
B - Build a webshop where users and logged in users can purchase products | 5 | 4
C - Allow users to create accounts where they can track the status of their orders & submit their own fan art | 5 | 4
D - Build a gallery where visitors can view submitted fan art  | 4 | 5
E - A robust admin area where one can manage the web shop as well as viewing and approving submitted fan art | 5 | 5
F - Customization for the user accounts, avatars etc | 1 | 3


</details>

## Scope
The goal of this website is to provide a hub for information about the Author and her books, and a place for people to purchase those books and related products.

It should build the fan base by attracting new readers, give existing readers an opportunity to learn more about the books, and help to build a sense of community by encouraging readers to display their fan art.

It is important that this website has a robust admin section, allowing the site administrators to manage the shop, the orders and the approval process for submitted fan art.

> you can focus on writing your app without needing to reinvent the wheel.
> -django

Taking a leaf from the Django philosophy I decided to utilize their incredibly powerful and customizable admin site. As such I have not build front end functionality for admin users to create, edit and delete products etc but have instead focussed on fully styling and customizing the existing django admin tool.


<details>
	<summary>Click to see - Scope Desicions</summary>


### Scope Desicions

As part of the user profiles I originally intended to build in user customization, allowing users to choose an avatar from a pre-approved selection. While this would be a lovely feature for the users experience it ranked very low in importance against the core functionality of the site, as such it has been moved to MVP2 scope.

I briefely considdered allowing users to upload their own profile images, however this is something that I have decided against for now. This author writes children’s books, and so many of the fans and community members are children and young adults. Allowing users to upload images and text that has not been approved leaves the system open to abuse. As such any system that allowed people to upload their own profile images would first need to send those images to be vetted (as we do with all submitted fan art). Balanced against the time to build and the time to run & administrate I decided that this was simply not a priority.

***

Another scope decision early on was to not focuss too much overall project time on building the 'magical' glowing buttons. While they would bring a great look and feel to the project they would not affect the core functionality in any way. While researching and testing chunks of code it became clear that to build the buttons I had in mind origionally would take a significant chunk of time. As such I decided to use a glow style that would work as a good placeholder and move the more ambitious button design to MVP2.

One effect of this decision is that the 'glow' effect is tied to hover functionality, and so does not work on a mobile or tablet screen. While this is by no means ideal I decided that some glow effect would be better than no glow effect, and for mobile users the buttons would still have the golden colour.


</details>


<details>
    <summary>Click to see - Scope Breakdown</summary>

### Core Scope

* A home page that gives an overview of the different series of books that the author has written, clearly signposting the visitor to both read more and to buy the books.
* A shop, where a user can purchase the books or related products.
* Information pages about the author and each of the series, where the user can read more.
* User accounts, where the user can track orders, view past orders and save their details.
* A fan art gallery where any visitor to the site can view the approved fan art, and that allows logged in users to submit fan art.
* A fully customized admin section that allows the site owner to manage the shop and orders, as well as the approval process for the fan art submissions.

### MVP2

* User account customization, where a user can choose between a pre-selected array of avatar images.


</details>


## Structure

### Design Decisions

* It was critical when designing the flow of the user fan art submission that any art, titles and text needed to be approved by a site administrator before being shown to the public. This author has mainly written books for younger readers, and a site that allowed for anything submitted to be instantly displayed would leave an oppertunity for innapropriate things to be posted where children are the target audience. This also applies to editing art that has already been approved.

* As touched on in the scope section I decided to use the exisitng Django admin site. Building my own admin pages felt like trying to re-invent the wheel, so instead I customized the built-in admin site as it already provides all of the existing functionality for managing the orders, products and fan art. Furthermore I customized it to use the same colour scheme and branding as the main website to give a consistent look and feel for an admin user (note the admin top bar logo from the main site footer).

* While the shop sells digital media such as e-boks and audio books handling the distribution of these is out of scope for this project. When a user purchases a digital media product they will recieve a code that they can use to redeam their product on a separate platform.


* While building the order model I decided to remove the ability to delete products from the product model. When creating or accessing an order many of the fields are generated from the product model, such as price etc. The thinking behind this was that this site will mostly feature the same products, adding more as the author writes more books, but will never have the high turnover of a large webshop. It is unlikely that a book will go out of print, and thus have to be completely removed. It is possible that merchandize may no longer be produced by the supplier and so forth, so I have build in the ability to remove products from the shop, but since this applies to only a small number of items I removed the posibility to completely delete them. This is a decision that could easilly be altered in the future if the webshop becomes significantly larger by saving items and prices to an order model rather than calculating them.

* When a product is out of stock it is shown on the products page, and a user is still able to click on it to read more information. There is an out of stock overlay and the purchase button is greyed out, but I decided to let the user click the purchase button and to then show them a message. The thinking behind this was to avoid too many alerts popping up for the user. It is clearly indicated both with text and a greyed out button that this product is out of stock, and it is only if the user still clicks on the purchase button that we show the alert.

* I wanted to integrate my website with social media accounts so people can log in and create a profile using an existing social media account. I have specifically chosen to integrate with Google so people can log in with their g-mail accounnts but by using [django-allauth](https://django-allauth.readthedocs.io/en/latest/installation.html) it is easy to extend to other social media platforms in the future.

### Surface

I held two key elements in mind when designing the surface for the site, the goal that it should feel ‘magical’ and building a site cohesive to the look and feel of the world of the more popular of the author's books. The colours that I used have been pulled directly from the cover of 'Ava and the Magic Door. The glowing effects around the text and on  the buttons is designed to echo the glowing effect of the doorway on the book’s cover.

Similarly I selected the title font to give a whimsical and slightly hand drawn feel. It had to be clear (for yonger readers) but also have a fantasy / magical personality.

[Mystery Quest](https://fonts.google.com/specimen/Mystery+Quest) - Title / Heading font



<details>
    <summary>Click to see - Colour Palet</summary>


![colour palet](https://github.com/LittleBlue418/Author-Site/blob/master/author_site_project/documentation/colour-palet.png)

</details>

### Skeleton

As the site is aimed at a wide age range of users I wanted to keep the design both clean and fun. I wanted to focus on the images, and make large and appealing buttons and UI elements. It was also important to have both a well structured menu and plenty of navigational buttons to give as seamless an experience as possible for everyone.


<details>
    <summary>Click to see - Wireframes</summary>
<br>



[Mobile Wireframe pdf](https://github.com/LittleBlue418/Author-Site/blob/master/author_site_project/documentation/mobile-wireframe.pdf)
<br>

[Desktop Wireframe pdf](https://github.com/LittleBlue418/Author-Site/blob/master/author_site_project/documentation/desktop-wireframe.pdf)

</details>



### Database and App Design

<details>
    <summary>Click to see - Rough Database / App Map </summary>


&nbsp;
![rough databse map](https://github.com/LittleBlue418/Author-Site/blob/master/author_site_project/documentation/database-map-drawing.jpg)

</details>



<details>
    <summary>Click to see - Database Design </summary>

&nbsp;
![databse design](https://github.com/LittleBlue418/Author-Site/blob/master/author_site_project/documentation/database%20design.png)

[Link to pdf of Database Design](https://github.com/LittleBlue418/Author-Site/blob/master/author_site_project/documentation/database%20design.pdf)

</details>


Designing the backend I knew that I wanted to have a separate profile table, not only for the orders but also for handling the fan art. Similarly the series table quickly became important as it ties together the fan art and the products, making both tables searchable on their series field.

When building the product model I knew that I would be selling a range of different types of products, some of which would have type specific fields. Initially I planned to use model inheritance (see attached image) but eventually decided against it. The scope of this webshop is fairly small, there will only be a limited number and range of products available. To create an intricate model inheritance set up felt more geared towards a much larger shop setup. For this reason I instead have the shared fields as required and the type specific fields as optional.

The frontend structure mirrors much of the backend app structure, with the following exceptions. The Series app has no frontend presence, it exists only as a reference for the fan art & product models. The shopping basket app has no models, instead using Django's built-in session and a context processor to track the user’s selections. The static pages app also has no models as these pages will not pull from a database, but instead simply contain information about the author and the series.

While I could have placed the 'about the series' pages in the series app neither page draws from the database, instead containing only static text. Since this is more closely aligned with the other static pages I decided to host them in the static pages app (though in theory they could live in either).

The drawing below roughly maps out the models and the app structure, and the attached PDF shows the database design.




***

[Back To Top](#table-of-contents)

## Features

&nbsp;

<details>
    <summary>Click to see the Existing Features</summary>

<br>

* **A Styled & Branded Navbar** - Signposts visitors to different areas of the site, as well as displaying the name of the author and a character from one of the books as a logo. Responsive on mobile, also displays the user's shopping basket with a responsive display of the number of products in the user's shopping basket.
* **A Simple & Informative Footer** - Gives users a quick overview of the publishing, copyright and contact information at a glance on every screen.
* **A Welcome / Home Page** - Gives an immediate overview of the author’s works, inviting the visitor to read more and browse the shop and make a purchase.
* **Information Pages** - Allowing visitors to read more about the author, and about each of the series.
* **A Fan Art Gallery** - Allowing visitors to the site to browse through the submitted fan art, and for logged in users to add / edit / delete their own fan art.
* **A Filterable Webshop** - Gives users an overview of all products available, as well as being able to filter by series and by product type.
* **A Stripe Checkout** - Allows users to purchase items from the webshop, choosing whether to save their details (if logged in) and then receiving both an order overview and confirmation email upon purchase.
* **A User Account Service** - Where users can submit their fan art, save their address details and view their order history.
* **A Well Organized Admin Section** - Fully customized and styled in line with the site, it is linked to from the nav bar only for super users. Each model has searchable fields, filters and carefully built styling to make using the admin site as intuitive as possible.

</details>

&nbsp;

<details>
    <summary>Click to see the MVP2 features</summary>

<br>

* **User Account Customization** - Allowing the users to customize their accounts further by allowing them to select from a set of pre-approved avatar images



</details>

&nbsp;

[Back To Top](#table-of-contents)

## Technologies Used

This project was built completely in django, and is hosted on Heroku.
&nbsp;

<details>
    <summary>Click to see -  List of Technologies</summary>

### The Site

The site is built using Django and an SQL databse; SQLite for development and PostgreSQL for deployment.

* [HTML](https://en.wikipedia.org/wiki/HTML)
* [CSS](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
* [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
* [Bootstrap](https://getbootstrap.com/)
* [FontAwesome](https://fontawesome.com/)
* [Jquery](https://jquery.com/)
* [django](https://www.djangoproject.com/)
* [Sqlite3](https://sqlite.org/index.html)
* [Python](https://www.python.org/)


### Deployment

I serve the site using uWSGI, packed into a docker image. This docker image is then deployed on Heroku

* [uWSGI](https://uwsgi-docs.readthedocs.io/en/latest/)
* [Docker](https://www.docker.com/)
* [Heroku](https://www.heroku.com/)
* [PostgreSQL](https://www.postgresql.org/)
* [Stripe](https://stripe.com/en-gb-se)
* [Google Cloud](https://cloud.google.com/)

### Version Control

* [git](https://git-scm.com/) - Version controll.
* [GitHub](https://github.com/) - Host directory.


</details>
&nbsp;


&nbsp;

[Back To Top](#table-of-contents)
&nbsp;

## Testing

### User Story Testing


<details>
    <summary>Click to see User Story Testing</summary>

* Home Page
	* See the name of the author
	* Easily access the site menu on both mobile & desktop
	* Log in or sign up
	* Instantly see the shopping basket
	* Scroll down to get an overview of the different series the author has written
	* Click on the ‘read more’ button to navigate to the about the series pages
	* Click on the  ‘buy the book’ buttons to navigate to the shop, where the series clicked on is pre-set as a product filter.
* About Pages (Series + Author)
	* Read more about the series & inspiration
	* Click on and visit related websites (eg. the hotel that inspired the Ava books)
	* Read more about the author
* Fan Art Gallery
	* Before logging in I can scroll through the existing fan art, reading the titles and descriptions and seeing who has submitted them
	* Once logged in I can view my own fan art, including any that I have submitted that has not yet been approved.
	* I can add new fan art.
	* If I have an unapproved fan art I get a clear notification, and the art is clearly labeled as unapproved.
	* I can click edit to change the text, title or artists name on the fan art that I have submitted. If I save changes the fan art is then returned to an un approved state.
	* I can delete fan art that I have submitted.
* Account
	* I can click on the account icon in the header to create an account
	* Once I have created an account and logged in I can reach the admin area if I am a superuser
	* I can see an overview of all my previous orders
	* I can see each previous order in full detail
	* I have a quick link to view my submitted fan art
	* I can see the details that the website has saved for me, and edit them.
        * I can delete my account, and see that my fan art is also deleted (but any orders are not).
* Social Media Account
        * I can click on the google button to create an account using my google email
        * I can choose to de-couple my account from my google account (as long as I have another email registered)
* Shop
	* I can scroll through all of the work that the author has produced to get a full overview
	* I can filter the shop by the type of product i want to buy (eg. audio book)
	* I can filter the shop by the series
	* I can click on an item to read more about it
	* If a product is out of stock I cannot add it to my basket. An error message is shown if i try.
	* On the product page I can click open a drop down to read more of the details
	* I can add the product to my basket.
	* When I add a product to my basket I see a modal with a brief overview of my basket and the option to keep shopping (which returns me to the page) to go to my basket. Inspired by [Threadless](https://www.threadless.com/)
* Basket
	* The basket, with the number of items in it, is visible from every screen
	* The basket page allows me to add and remove items from within the basket screen.
	* I cannot set less than 0 for any product .
	* I cannot add more than 99 of any type of product.
	* I can return to the product overview to read more about the product.
	* When I have made a change to the number of items in the basket a button appears to clearly show I need to click update
	* I cannot click pay while there is an item in my shopping basket that needs to be updated.
	* I can click pay to be taken to the checkout
* Checkout
	* If I try to pay without filling out the required fields the page will not let me submit
	* I have the option to save the card address to my profile if logged in.
	* I have the option to use the same address for both card and shipping, when I choose this I no longer see the shipping address fields.
	* When I submit a payment I am taken to a success page that presents me with a message that the order was successful and tells me that an email will be sent to me.
	* On the success screen I can view my order in detail, including the payment & shipping details.
	* As a non logged in user I can then click to return to the home screen
	* As a logged in user I can click to view all of my orders.
* Admin Area
	* As a logged in super user I can access the admin area through my account drop down in the nav bar.
	* I can view all fan art entries and quickly see which ones are waiting to be approved.
	* I can click on and preview an unapproved entry and check that the language and the image are suitable for all ages, then set the status to approved.
	* I can delete any fan art that is not appropriate, and see which user has submitted it.
	* I can access the product table, getting an overview of which products are in the shop and their in stock status.
	* I can add new products
	* I can edit existing products
        * I cannot delete products
	* If a product is currently out of stock I can set it to be out of stock
	* I can view a complete list of all customer orders.
	* I can search for customer orders on a number of different identifiers (order number, date, stripe payment id, user profile, status, full name and email)
	* I can quickly filter the orders based on their status (submitted, paid, payment failed, shipped)
        * Once the order has been shipped (and status set to shipped) I cannot change any details on the order.


</details>

### Automated & Other Testing


### Chrome Developer Tools
Ensure the app works well and looks as it should on all screen sizes, as well as using the console tool get real time error feedback & stack tracing.

### User Testing
Sending the app to friends & colleagues to use, collecting their feedback for bug fixes and adjustments.


### Django unit testing
I wrote tests for some of the more complex pieces of the site. Ideally it would be nice to get as much coverage as possible, however in the time available I chose to prioritize testing on the more complex functions & views I had written myself (rather than on the code from stripe for example, or on simple views that return just a static page).

### Interesting Bugs

* If shopping basket gets updated after payment intent has been created, and whilst payment is ongoing, then the order gets created with an updated shopping basket while the payment will be the price of the previous shopping basket.

[Back To Top](#table-of-contents)
&nbsp;


## Deployment & Version Control

<details>
    <summary>Click to see - Deployment Steps </summary>

### Local Development
* Clone this directory to your local computer.
* Create a virtual enviroment
`virtualenv venv`.
* Activate the virtual environment `source venv/bin/activate`.
* `pip install -r requirements.txt`
* create a .env file
    * SECRET_KEY=[generare a secret key](https://djecrety.ir/)
    * DEVELOPMENT=True
    * DEFAULT_FROM_EMAIL=(whatever you would like your default 'from' email to be)
* `python manage.py migrate`
* `python manage.py runserver`


### Stripe Payment in Local Development
* Set up a [Stripe account](https://stripe.com/en-gb-se)
* From your Stripe dashboard access and add the following to your .env file
    * STRIPE_PUBLIC_KEY=(Your Publishable key)
    * STRIPE_SECRET_KEY=(Secret Key)
* Install the [Stripe CLI](https://stripe.com/docs/stripe-cli)
* Run the following command and follow the instructions in the terminal
  ```bash
  stripe login
  ```
* Run the command
  ```bash
  stripe listen --forward-to 127.0.0.1:8000/checkout/stripe/
  ```
* That command will print out the webhook secret, add this to your .env file
    * STRIPE_WEBHOOK_SECRET=(get from terminal)
* Open a new terminal (and leave this one running)
* Run the command
  ```bash
  python manage.py runserver
  ```

### Setting Up Email for Local Development
If you want to test sending real email, while developing you need to configure
the project using the SMTP settings from your email provider.
* In your .env file
    * EMAIL_HOST=(The SMTP server)
    * EMAIL_PORT=(The SMTP server port. Defaults to 465)
    * EMAIL_HOST_USER=(The SMTP username. Defaults to whatever you put in DEFAULT_FROM_EMAIL)
    * EMAIL_HOST_PASSWORD=(The SMTP password)
    * EMAIL_USE_SSL=(Whether the SMTP server is using SSL. Defaults to True)

### Setting Up Google with allauth
* Follow [these instructions](https://django-allauth.readthedocs.io/en/latest/providers.html#app-registration)


### Google Bucket
* Follow the steps for setting up Google with allauth if you havent done that already (above). You will have created a project during this step.
* Go to the [cloud console](https://console.cloud.google.com/)
    * IAM & Admin -> Service Accounts -> Create a service account
    * Create a json key for your service account (this will trigger a download of the key file)
    * Move this json file into the top level of your project and rename it  `serviceaccount.json` (your gitignore is set to ignore this file name, don't delete this file)
    * Storage -> Browser -> Create Bucket (use fine grained permissions)
    * Click on your bucket and navigate to permissions
    * Click Add to assign the 'Storage Object Admin' role to your service account
    * Click Add to assign the 'Storage Object Viewer' role to 'allUsers'
* In your .env set
    * GOOGLE_APPLICATION_CREDENTIALS=(the name of the json file)
    * GS_BUCKET_NAME=(your bucket name)


### Deploy to Heroku
These instructions assume that you have a github account and a Heroku account, and have set up the Heroku CLI on your computer.
* Clone this git repository to your own github account
* Run the following commands
  ```bash
  heroku apps:create $APP_NAME --region eu
  heroku stack:set container -a $APP_NAME
  ```
  where `$APP_NAME` is the name of your Heroku app
* On the Heroku website, in your new app, connect to your github
* In the Heroku website create a PostgreSQL database as a Heroku addon
* While in your Heroku project copy the database URI and add it to your .env file
    * DATABASE_URL=(Heroku database URI)
* Go to Stripe -> Developers -> Webhooks
    * Add endpoint
    * Set the URL to the URL for your Heroku app -> https://app-name.herokuapp.com/checkout/stripe/
    * Copy the Signing Secret and go back to Heroku
* In Heroku set the Signing Secret you just coppied as the Config Var STRIPE_WEBHOOK_SECRET
* Set your other config vars
    * ALLOWED_HOSTS=(app-name.herokuapp.com)
    * DATABASE_URL=(same as .env)
    * DEFAULT_FROM_EMAIL=(same as .env)
    * EMAIL_HOST=(same as .env)
    * EMAIL_HOST_PASSWORD=(same as .env)
    * GS_BUCKET_NAME=(same as .env)
    * SECRET_KEY=(same as .env)
    * SERVICE_ACCOUNT_KEY=(the contents of the service account file, the whole object)
    * STRIPE_PUBLIC_KEY=(same as .env)
    * STRIPE_SECRET_KEY=(same as .env)
* Select the repo you have cloned
* On the deploy tab manually deploy
* In your project, in the terminal
  ```bash
  python manage.py migrate
  python manage.py collectstatic
  ```



</details>

[Back To Top](#table-of-contents)
&nbsp;

## Credits

### Code
- Code for the glowing buttons was inspired by [this website](https://www.codingnepalweb.com/2020/05/cool-glowing-effect-on-css-buttons.html)
- I had help building the Docker image and configuring uWSGI from my partner.

### Content
The content for this site was written by the author herself.

### Media

<details>
    <summary>Click to see all media credits</summary>

* Site: [Paralax Header Background](https://www.pexels.com/photo/background-blur-bokeh-bright-220067/) - Pexels
* Home / Shop: Ava book cover - Author's own
* Home / Shop: Parma Ham book cover - Author's own
* Site logo guineapig - Author's own
* Publishing logo / Admin site logo - Author's own
* Ava's World images (1,2,3) - Author's own
* Parma Ham's World images (1,2) -  Author's own
* Shop: Gunea pig christmas decoration - Author's own
* Shop: [Cuddly bear toy](https://unsplash.com/photos/iqiIlTm3-_4) - unsplash - [Ra Dragon](https://unsplash.com/@radragon)

* Fan art - Submitted by fans


</details>


### Acknowledgements
I was inspired to create this website after looking at the following author websites
* [Terry Pratchett](#https://www.terrypratchettbooks.com/)
* [Niel Gaiman](#https://neilgaiman.com/)
* [Natasha Pulley](#https://natashapulley.co.uk/)

[Back To Top](#table-of-contents)
