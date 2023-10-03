![](assets/css/images/readme-main.png)
____
**Table of Contents**

- [SHOPIFY-Milestone Final project__](#Shopify-final-milestone-project)
  - [__Description__](#description)
  - [__Shopify responsive website__](#yogym-responsive-website)
  - [__User Experience goals__](#user-experience-goals)
    - [__First time user:__](#first-time-user)
    - [__Frequent user:__](#frequent-user)
    - [__Returning User:__](#returning-user)
  - [__Design__](#design)
    - [__imagery__](#imagery)
  - [__Structure__](#structure)
    - [Homepage](#homepage)
    - [Navigation Bar](#navigation-bar)
    - [About Section](#User-Registration:)
    - [Features Section](#User-login:)
    - [Plans Section](#Password-Change:)
    - [Stories Section](#Admin-Product-Management:)
    - [Contact Us Section](#Product-Listing:)
    - [About Section](#Product-Deatils:)
    - [Features Section](#Adding-to-Cart:)
    - [Plans Section](#Card-Quantity-Modification:)
    - [Stories Section](#Removing-from-Cart:)
    - [Contact Us Section](#Multiple-Address-Storage:)
    - [Features Section](#Selecting-Delivery-Address:)
    - [Plans Section](#Order-palcement:)
    - [Stories Section](#Order-History:)
    - [Contact Us Section](#Order-Status:)
    - [Features Section](#Realtime-Pricing:)
    - [__Technologies Used__](#technologies-used)
    - [HTML](#html)
    - [CSS](#css)
    - [Google Fonts](#google-fonts)
    - [Visual Studio Code](#visual-studio-code)
    - [Techsini](#Cloudinary)
    - [Github](#github)
    - [Github Pages](#github)
  - [**Deployment**](#deployment)
    - [**Starting The Project**](#starting-the-project)
  - [**Deployment to cloud platform**](#deployment-to-cloud-platform)
  - [**Credits**](#credits)
    - [**Acknowledgements**](#acknowledgements)
    - [**Media And Rest**](#media-and-rest)

# __YOGYM-Milestone 1st project__

## __Description__
This website in created for the final project of Code Institute's [Diploma in Full Stack Software Development](https://codeinstitute.net/ie/full-stack-software-development-diploma/). The criteria of used technologies was Pyhton Django and Full stack web farmework. i mainly focused on the backend, did focus on sites fucntionality but mainly the backend and frontend was just simple boostrap.

You can have a Live view of website [here](https://shopify123-255374084b94.herokuapp.com/).

---
## __SHOPIFY responsive website__
The site is fully resposive on all all devices. and does not brea the design at any resolution or any size of the screen
___

## __User Experience goals__
### __First time user:__
As a First time user i want to access all the content and check the the laptops nad mobiles easily and go through all the content of the shopify website, checkout process should be easy and placing order should be in few moments.
### __Frequent user:__
As a frequent user or who is already signed up and have an account my address should be saved and checkour process i can even add new address too.
### __Returning User:__
As a returning user i must be able to go throgh orders history and all my account detals must be saved.

___

## __Design__
### __color scheme__
The design is very simple to follow and very easy to use as a user who is buying products and cheking newly arrived and trending products.
as i was mainly focused in the backend the whole website is built using just bootstrap for frontend, it not amazinly vibrant and coloful but it serves the purpose of an ecommerce website.
### __imagery__
Images are used for product listing and are rendered by a cloud platform called Cloudinary.
___

## Features

### User Registration:
Users can create accounts by providing their email and password.

### User Login:
Registered users can log in securely to access their accounts

### Password Change
Users have the option to change their passwords when needed.

### Admin Product Management:
Admin users can add new products to the catalog, specifying details such as title, description, price, brand, category, and uploading product images.

### Product Listings:
Users can view a list of available products, including details like title, price, and product image.

### Product Details:
Users can click on a product to view its detailed information, including description and discounted price.

### Adding to Cart: 
Users can add products to their shopping carts.

### Cart Quantity Modification: 
Users can easily increase or decrease the quantity of products in their cart.

### Removing from Cart: 
Users can remove products from their cart, with the cart total updating in real-time based on the quantity and price changes.

### Multiple Address Storage:
Users can store multiple delivery addresses in their profiles for easy selection during checkout.

### Selecting Delivery Address: 
During the order placement process, users can choose from their stored delivery addresses.

###  Order Placement: 
Users can place orders for the products in their shopping carts.

### Order History:
Users can view a history of their past orders, including order details, status, and delivery information.

### Order Status Tracking:
Users can check the status of their orders (e.g., pending, accepted, dispatched, delivered).

### Real-time Price Update: 
The order total updates in real-time as users modify the quantity or products in their cart.

### Order Status Update: 
Admin users can update the status of orders (e.g., from accepted to dispatched).

## Architecture Design
<img src="https://res.cloudinary.com/dpzk9bdae/image/upload/v1695482209/media/shopify_nkse9u.png" alt="Architecture" border="0" />

___
### __Technologies Used__
____
### BOTSTRAP
The Layout of the websites is only bootstrap.

### Visual Studio Code

VS code was used as an IDE(*Integrated Development Environment*) to develop this website .

### Cloudinary
Cloudinary.com is a SaaS technology company headquartered in Santa Clara, California, with offices in Israel, England, Poland, and Singapore. The company provides cloud-based image and video management services. 

### Github
Github was used to store all the source code for this website

## Deployment

​This project uses Heroku, a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.​Deployment steps are as follows, after account setup:​

Select New in the top-right corner of your Heroku Dashboard, and select Create new app from the dropdown menu.
Enter a name for your app. The app name must be unique, so you need to adjust the name until you find a name that hasn't been used.
From the dropdown, choose the region closest to you (EU or USA), and finally, select Create App.
From the new app Settings, click Reveal Config Vars, and set the value of KEY to PORT, and the value to 8000 then select add.
Now, add a seecond Config Var for the creds.jsonfile, which contains the API Key from Google Sheets. Set the value of KEY to CREDS and paste the entire contents of creds.json in the VALUE box. Select add.
Further down, to support dependencies, select Add buildpack.
The order of the buildpacks is important. Select Python first, then Save changes. Click Add buildpack again, and select Node.js, then Save changes. If they are not in this order, you can drag them to rearrange them
Heroku needs two additional files in order to deploy properly.

requirements.txt
Procfile
You can install this project's requirements (where applicable) using: pip3 install -r requirements.txt. If you have your own packages that have been installed, then the requirements file needs to be updated using: pip3 freeze --local > requirements.txt

The Procfile can be created with the following command: echo web: node index.js > Procfile

For Heroku deployment, follow these steps to connect your GitHub repository to the newly created app:​

At the top of the screen on Heroku, select Deploy.
Next to Deployment method select GitHub, then scroll down and click Connect to GitHub to confirm you want to connect.
In the repo-name field, search for the name of the GitHub repository to deploy, and click Search.
Click Connect to link the GitHub repository with Heroku.
Scroll down to the Manual deploy section, and click Deploy Branch.
If you like, click Enable Automatic Deploys in the Automatic deploys section to have Heroku rebuild your app every time you push a new change to GitHub.
The frontend terminal should now be connected and deployed to Heroku.

____

___
## **Credits**
____
### **Acknowledgements**
First of All thanks to [Code Institute](https://codeinstitute.net/ie/) for an amazing content and brilliant course to offer, and then All thanks go to my Mentor ***"Ronan Mclelland"*** .

