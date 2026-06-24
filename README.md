# SQLAlchemy Relational Database Assignment

## Overview

This project demonstrates how to use SQLAlchemy with SQLite to create and manage a relational database.

The database contains three related models:

* `User`
* `Product`
* `Order`

Each order connects one user to one product and stores the quantity ordered.

## Features

* Creates an SQLite database named `shop.db`
* Defines database models using SQLAlchemy ORM
* Adds two users
* Adds three products
* Adds four orders
* Displays order information
* Updates the price of a product
* Deletes a user by ID
* Uses one-to-many relationships between users, products, and orders

## Database Structure

### User

* `id`
* `name`
* `email`

### Product

* `id`
* `name`
* `price`

### Order

* `id`
* `user_id`
* `product_id`
* `quantity`

## Relationships

* One user can have many orders.
* One product can appear in many orders.
* Each order belongs to one user and one product.

## Technologies Used

* Python
* SQLAlchemy
* SQLite

## Installation

1. Clone the repository:

```bash
git clone github.com/darwin2342/sqlalchemy_relational_database
```

2. Move into the project folder:

```bash
cd sqlalchemy_relational_database
```

3. Create a virtual environment:

```bash
python -m venv .venv
```

4. Activate the virtual environment on Windows:

```bash
.venv\Scripts\activate
```

5. Install the dependencies:

```bash
pip install -r requirements.txt
```

## Running the Project

Run:

```bash
python main.py
```

The program will create the database tables and display the order information in the terminal.

## Project Structure

```text
sqlalchemy_relational_database/
├── .gitignore
├── main.py
├── README.md
├── requirements.txt
└── shop.db
```

## What I Learned

Through this project, I practiced:

* Creating database models with SQLAlchemy
* Using `Mapped` and `mapped_column`
* Creating primary and foreign keys
* Defining ORM relationships
* Adding and querying database records
* Updating existing records
* Deleting records by ID
* Committing database changes with a SQLAlchemy session
