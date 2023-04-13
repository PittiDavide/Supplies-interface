# **Supplies-interface**

> This web app allows a store to interface with a list of suppliers for the purchase of goods so that it can decide on the best offer based on its requests.

---

## **Installation**

- to run the web app install docker and run `docker compose up`
- open the browser and go to `http://localhost:8080/database_insert` to insert test data into the database
- visit the web app in `http://localhost:8080`
- on the site search the name of materials (like g1 or g2), quantity of the product that you want and a date
- if those informations are inside of one of the discounts types the total price will be discounted

## **Functional analysis**

### **NARRATIVE**

As a shop employee, I want a system which can find the best supplier for a product knowing the price of the product and eventually sales applied on
it, in order to buy goods from the cheapest supplier.
I also want the minimum shipping times as possible, for each supplier so i can decide who's the fastest to deliver.

1. **Scenario**: No supplier sell the requested product
   > - **Given**: The shop haven't still bought the product
   > - **When** I have to look for a supplier who can sell the product
   > - **Then\*** The system have to send an error message saying that the product is not available
2. **Scenario**: At the least one supplier sells the requested product
   > - **Given** The shop has specified the product and the quantity needed
   > - **When** I have to look for a supplier who can sell the product
   > - **Then** the system must return a list of suppliers who sell the requested product, indicating the purchase price and shipping time of each supplier
3. **Scenario**: No supplier offers a discount for the requested order
   > - **Given** I have to look for a supplier who can sell the product, and there is no discount available
   > - **When** I look for suppliers who sell the required product
   > - **Then** the system should return the supplier list as described in the previous scenario
4. **Scenario**: At least one supplier offers a discount for the requested order
   > - **Since** the store has specified the product to purchase and the desired quantity, and there are discounts available
   > - **When** I look for suppliers who sell the required product
   > - **Then** the system must return a list of suppliers selling the requested product, indicating the purchase price and shipping time of each supplier, including applicable discounts
5. **Scenario**: A vendor offers a discount for a limited time only
   > - **Because** the shop has specified the product to buy and the desired quantity, and a supplier offers a discount for a limited time only
   > - **When** I have to look for a supplier who can sell the product
   > - **Then** the system must return a list of suppliers who sell the requested product, indicating the purchase price and shipping time of each supplier, including discounts applicable only for the indicated period
6. **Scenario**: A supplier offers a discount only for a certain minimum quantity of product
   > - **Since** the store has specified the product to purchase and a certain minimum quantity required to obtain the discount offered by a supplier.
   > - **When** I have to look for a supplier who can sell the product
   > - **Then** the system must return a list of suppliers who sell the requested product, indicating the purchase price and shipping time of each supplier, including discounts applicable only if the minimum quantity requested is reached.

## **Tecnologies**

This app is divided between:

- Frontend
- Backend
- Database

### **Frontend**

Developed using the svelte Kit framework.

### **Backend**

Developed with python using the flask framework.

## **Database**

This project includes a database to manage information about suppliers and supplies they offer. The database consists of three tables: **_'goods'_**, **_'supplier'_**, and **_'supplies'_**.

### **Goods table**

The **_'goods'_** table represents a list of supplies and has the following attributes:

- **_'id_g'_**: unique identifier for the supply
- **_'name'_**: name of the supply

### **Supplier table**

The Supplier table represents a list of available suppliers and has the following attributes:

- **_'id_s'_**: unique identifier for the supplier
- **_'name'_**: name of the supplier
- **_'address'_**: address of the supplier

### **Supplies table**

The **_'supplies'_** table represents the supplies available for each supplier and has the following attributes:

- **_'id_supplies'_**: unique identifier for the supply of a supplier
- **_'price'_**: price of the product sold by the supplier
- **_'delivery_time'_**: time required for delivery of the product
- **_'quantity'_**: quantity of the supply available for sale
- **_'quantity_for_sale'_**: minimum quantity of the supply to be purchased to apply a discount
- **_'quantity_sale'_**: discount applied if the supply is purchased in quantities greater than those indicated in quantity_for_sale
- **_'value'_**: total purchase value required to apply a discount
- **_'value_sale'_**: discount applied if the total purchase value exceeds the value indicated in value
- **_'s_date'_** and **_'e_date'_**: start and end date for applying a discount, if the selected date is between these dates, a discount is applied
- **_'date_sale'_**: discount applicable if the selected date is between s_date and e_date
- **_'season'_**: season for which a discount is applied
- **_'season_sale'_**: discount applied if the selected date falls within the season indicated in season

### **Relationships**

The **_'supplier'_** and **_'supplies'_** tables are linked by a one-to-many relationship, as a supplier can have multiple supplies. Similarly, the **_'goods'_** and **_'supplies'_** tables are linked by a one-to-many relationship, as a supply corresponds to one material. The foreign keys for these relationships are **_'supplier.id_s'_** and **_'goods.id_g'_**, respectively.

### **Model ER**

![model ER](ER.png)

### **Logical model**

- **Supplier** (**_'id_s'_** `PK`, 'name', 'address');
- **Goods** (**_'id_g'_** `PK`, 'name');
- **Supplies** (**_'id_supplies'_** PK, **_'id_s'_** `FK`, **_'id_g'_** `FK`, 'price', 'delivery_time', 'quantity', 'quantity_for_sale', 'quantity_sale', 'value', 'value_sale', 's_date', 'e_date', 'date_sale', 'season', 'season_sale');

## **SQL**

        CREATE DATABASE supplies_db;
        CREATE TABLE goods (
          id_g int PRIMARY KEY NOT NULL,
          name varchar(20)
        );
        CREATE TABLE supplier (
            id_s int PRIMARY KEY NOT NULL,
            name varchar(20),
            address varchar(255)
        );
        CREATE TABLE supplies (
            id_supplies int PRIMARY KEY NOT NULL,
            price int,
            delivery_time int,
            quantity int,
            quantity_for_sale int,
            quantity_sale int,
            value int,
            value_sale int,
            s_date date,
            e_date date,
            date_sale int,
            season varchar(20),
            season_sale int,
            id_s int NOT NULL,
            id_g int NOT NULL,
            FOREIGN KEY (id_s) REFERENCES supplier (id_s) ON DELETE CASCADE,
            FOREIGN KEY (id_g) REFERENCES goods (id_g) ON DELETE CASCADE
        );
