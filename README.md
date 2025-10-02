#  CS50 Shop
  An Online Shop for Selling & Buying Clothes

#### [Watch Video Demo On Youtube](https://youtu.be/agswBqxFVQo)



![CS50 shop demo](./CS50shop-demo.gif)

## Table of Contents


- [Description](#description)
  - [Inspiration](#inspiration)
  - [Functionality](#functionality)
    - [Shopping](#shopping)
    - [Managing](#managing)
- [Files & Folders](#files--folders)
- [Notes about drop.sql and query.sql](#notes-about-dropsql-and-querysql)
- [Installation](#installation)
- [Features](#features)
- [Challenges](#challenges)
- [Future Work](#future-work)
- [Acknowledgments](#acknowledgments)

## Description 
### Inspiration
For my CS50 final project, I built a dedicated e‑commerce site to solve a problem I kept seeing: since COVID‑19, more people shop online—whether they’re strapped for time or just don’t enjoy in‑person browsing. In my country, small businesses jumped on Instagram as an easy way to reach customers, but it’s never been designed for actual transactions. Its interface prioritizes social content over shopping, there’s no reliable order tracking, and there’s no official verification to prove a seller’s legitimacy.
On top of that, Instagram runs on foreign servers and often gets slowed or blocked here. People end up wrestling with VPNs or waiting through endless loading screens. My site changes that: it lives on national servers, so it stays fast and accessible even during network disruptions or blackouts.

**My Website versus Instagram:**  
- **A commerce‑focused UI** that makes finding products, managing your cart, and checking out effortless.
- **Real‑time order tracking** for buyers and a clear dashboard for owners—everyone knows exactly when an item ships.
- **Local hosting** to keep the store online no matter how shaky the internet gets.

### Functionality 

#### Shopping
People can sign up by providing basic information and after they're logged in they can browse view products , product's details and add products they want to their shopping cart once they're done choosing they can click the shopping cart button which takes them to a page that displays all the items on their shopping cart from here they can remove the ones they don't want and if they're happy with the list they can click proceed to checkout then after providing the necessary information (which the owner will use to ship their order) they can place their order.  Ideally this would happen after they've made the payment via an online payment gateway which can be implemented using Paypal or Stripe API unfortunately I don't own a credit card which is why i couldn't sign up for these APIs.


#### Managing
My website uses role based access to differentiate between Owner and Customers.
The Owner must have dedicated username and password that me as the developer would provide to the shop owner who is going to manage the shop.
once the Owner is logged in using the provided credentials they can manage the shop , add and remove products and view all the orders that have been placed on the website.
All this is possible using the owner's dashboard which is accessible from the navbar.
When the owner logs in by clicking the user icon on the top right corner they will be taken to the owners dashboard which includes 3 links: 
1. **Add Product** : a link that will take the owner to page that includes only a form. by filling out this form the owner can add products to the website. after filling out the form clicking add product will add the product to the database and immediately display it on the main product listing page. 

2. **View Orders** : this links will take the owner to a page that display all the orders that have been placed on the website each order is displayed visually as a row of the table. clicking view order details of each of the orders will take the owner to a new page that displays all the detail of that order including a list of all the items ordered including a link to the product that has been ordered for each ordered item.
and all the information the customer has provided during checkout this information includes a postal address which owner will use to ship orders and an email address that the owner will use to inform the customer when their order is shipped.

3. **Manage Products** : this link will take the Owner to a version of the listing page that displays all of the products available on the shop and two buttons for each product 1. View details button that will take the user to a product detail page this page displays a bigger picture of the product and more details and description of the product and also all the colors and sizes that's available for the product this button and this page are also displayed and accessible for the customers. next to the view details button there is a red remove button that's only accessible for the owner clicking on it will remove that product from the shop and the database.

## Files & Folders
project/  
- app.py  
- static/   
  - uploads/
  - styles.css
  - templates/ 
- database.db 
- drop.sql
- query.sql
- helper.py
- requirements.txt  


| Path               | Description                                 |
|--------------------|------------------------------------------------------|
| `app.py`           | flask routes and backend logic                       |
| `static/`          | static files including file uploads, images and CSS  |
| `templates/`       |  HTML templates, all jinja templated frontend files  |
| `database.db`      |  sqlite3 database including table structures and all the data stored on the website   |
| `query.sql`        |  includes all the table schema |
| `drop.sql`         |  includes the command to delete everything on the database |
| `requirements.txt` |  Dependencies for the project libraries and frameworks |
| `__pycache__`      | automatically created to store cached data |
| `flask_session`    | automatically created to store flask sessions |


#### Notes about drop.sql and query.sql
- **query.sql** I didn't want to add tables to my database using the terminal because I found that process to be messy and time consuming. so I decided to first figure out what tables with what sort of structure I needed by first writing everything down in a separate file. having the schema for all the tables in one file felt neat and helped me get a general sense of what everything would look like underneath the hood.

- **drop.sql** since I did all the testing manually; while testing my project there were many instances that I needed to delete everything from the database and start from scratch in order to avoid letting all the data accumulate and get out of hand.


I knew it was unlikely I’d get the schema right on the first try. Keeping everything in query.sql made it easy to experiment, adjust table structures, and start fresh whenever needed. Whenever I had to reset, I just ran two commands: first, drop.sql to delete all tables, then query.sql to rebuild them from scratch.

## Installation  
Anyone can run it by installing the requirements and running the command "flask run"

1. Clone the repository
2. Navigate to the project directory
3. Create and activate a virtual environment
4. Install dependencies:
``` pip install -r requirements.txt ```


## Features
- User Registration & Login
- Role-based access (Owner / Customer)
- Product Management (Owners can add,  delete products)
- Product Variants (Size, Color, Stock)
- Product Listing page (Shop)
- Product Details page
- Shopping Cart
- Checkout and Place Order
- Order History
- File/Image Upload for products 
- Owner Dashboard
- User Dashboard
- Contact Page


## Challenges    
- **Foreign Key Constraint Error** : When I tried deleting products from the owner’s dashboard, I ran into an error that confused me for a while. I kept getting a foreign key constraint error and had no idea why. After googling around a bit to understand what causes such errors, I found the issue. In my database, the products table is linked to a variants table through variant IDs. So when I attempted to delete a product without first deleting its associated variants, the database threw the foreign key constraint error. To fix this, I had to first fetch and delete all variants related to the product, and only then proceed to delete the product itself.

- **Image Uploads** : To display images for each product, I needed the owner to upload a photo and I had to find a way to store that photo so I could access and display it later. I found that the common convention with Flask is to have an upload/ directory inside the static/ folder in the main project directory, and to store images there. So when the owner uploads an image, I save it in that folder and store the image’s URL in the image column of the products table in the database. Later, whenever I need to display the image, I just use an <img> tag and pass the image URL into the src attribute like this:    ``` <img src="{{ product.image_url }}"> ```

The Logic made sense and i came up with pseudocode for this problem but i didn't know how to implement it using python so I did use Chatgpt's help partially.

## Future Work
I think this project was a solid way of practicing what i learned in CS50 but if i wanted to use it in the real world i would definitely consider building a version 2 of it using django and postgres to firstly make the deployment easier i have realized many hosts are postgres and django friendly and also it's easier to automate tests using django as far as i know
Improvements : 
- Search and Filter capabilities for products and orders( in view orders via owner dashboard)
- Payment Gateway: i didn't implement a payment gateway because that required signing up to stripe/ paypal which i can't without a credit card
Owner specific 
- sales data available on owner's dashboard 
- edit products
- easily increase the stock quantity whenever they want without having to remove and add product from scratch
- they should be informed which products are out of stock and users have tried to add to their carts (sorted by the amount of times people have tried to purchase them) so that they know which products would sell best if they made them available.

## Acknowledgments: 
For learning the syntax of how to upload and store an image I did use Chatgpt's help.


#### Author : **Negin Jahedi**
