-- SQLBook: Code

CREATE TABLE
    IF NOT EXISTS goods (
        id_g int PRIMARY KEY NOT NULL,
        name varchar(20)
    );

CREATE TABLE
    IF NOT EXISTS supplier (
        id_s int PRIMARY KEY NOT NULL,
        name varchar(20),
        address varchar(255)
    );

CREATE TABLE
    IF NOT EXISTS supplies (
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

