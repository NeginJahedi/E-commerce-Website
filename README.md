# Portfolio Project: Online Clothing Shop Website

---

## Project Title

**Responsive Online Clothing Shop**

---

## Project Overview

This is a fully functional e-commerce website developed as part of a final project for CS50. The website is designed for a clothing shop and includes essential features such as user authentication, product browsing, cart management, wishlist functionality, and checkout. It was built with scalability and adaptability in mind, allowing it to be easily modified for different types of shops in the future.

---

## Technologies Used

- **Frontend**: HTML, CSS, Bootstrap
- **Backend**: Flask (Python)
- **Database**: SQL (SQLite)
- **Other Tools**: Jinja2 for templating, AWS Linux and VS Code for development environment setup

---

## Features

1. **User Authentication**
   - Users can register and log in.
   - Session management is implemented to allow dynamic display of user-specific features.
   - Owner and regular user dashboards are accessible based on the type of account.

2. **Product Display**
   - A visually appealing, responsive grid layout displays all available products.
   - Products include an image, name, description, price, and "View Details" button.

3. **Cart and Wishlist Functionality**
   - Users can add items to their cart and wishlist.
   - Cart displays the items with quantities, prices, subtotals, and total cost.
   - Wishlist provides easy access to saved items.

4. **Checkout Process**
   - Users can proceed to checkout directly from the cart.
   - Checkout displays an order summary and allows the user to input their details.

5. **Database Management**
   - The database tracks users, products, product variants, cart items, wishlists, and orders.
   - Efficient SQL queries ensure the performance and integrity of operations.

6. **Responsive Design**
   - The entire website is mobile-friendly and adapts seamlessly to different screen sizes using Bootstrap’s grid system.

7. **Owner Dashboard**
   - Separate dashboard for shop owners to view and manage their store.

---

## Challenges and Solutions

1. **Foreign Key Constraint Issues**
   - Encountered challenges when trying to delete products tied to other tables. Solved by ensuring proper database relationships and cascading deletions where necessary.

2. **Session Management**
   - Managed user-specific features dynamically using Flask sessions and conditional rendering in Jinja templates.

3. **Dynamic Data Display**
   - Integrated SQL queries with Python logic to dynamically display product data, cart items, and user-specific features without duplicating code.

4. **Design Consistency**
   - Bootstrap’s utility classes were leveraged for consistent spacing, alignment, and styling across the website.

5. **Development Environment**
   - Transitioned from CS50 Codespace to a local environment using AWS Linux and VS Code to ensure smoother workflows.

---

## Screenshots

- **Homepage**: A visually appealing, responsive homepage introducing the clothing shop with a simple navigation bar and links to shop, wishlist, and user account sections.
- **Shop**: Displays featured products in a clean, grid layout.
- **Product Page**: Detailed view of a single product with descriptions, images, and size options.
- **Cart**: Displays selected items with subtotals and total cost.
- **Wishlist**: A section for users to save items for later.
- **Checkout**: Order summary and form to input customer details.
- **Owner Dashboard**: Provides an overview of shop performance (placeholder functionality).

---

## Potential Future Enhancements

1. **Payment Integration**
   - Add secure payment gateways like PayPal or Stripe to enable online transactions.

2. **Product Filtering and Search**
   - Implement features to filter products by category, size, or price range.

3. **Enhanced Admin Panel**
   - Build a comprehensive owner dashboard for inventory and order management.

4. **Email Notifications**
   - Notify users about order status and promotions via email.

5. **Enhanced Styling**
   - Further refine UI/UX with advanced animations and interactivity.

---

## Why This Project Stands Out

This project demonstrates strong problem-solving skills, full-stack development capabilities, and attention to detail. It shows a clear understanding of:

- Database design and optimization
- Dynamic backend integration
- Frontend styling with responsiveness
- Debugging and managing complex workflows


