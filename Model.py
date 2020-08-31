"""Creation of database with his tables
and different manipulation useful for the program"""
import mysql.connector
import yaml


class DataBase:
    """Attributes and method useful for creation
    and manipulation of the database"""
    def __init__(self):
        """Connection to the database "open_food_facts"
        and creation of the mySQL cursor"""

        # File with database data connection
        with open("config.yml", "r") as ymlfile:
            cfg = yaml.safe_load(ymlfile)

        # Connection to the database open_food_facts
        self.mydb = mysql.connector.connect(
            host=cfg["mysql"]["host"],
            user=cfg["mysql"]["user"], password=cfg["mysql"]["passwd"],
            database=cfg["mysql"]["db"],
            autocommit=True)
        # Creation of mySQL cursor
        self.cursor = self.mydb.cursor()

    def create_database(self):
        """SQL command to create database"""

        self.cursor.execute("""CREATE DATABASE
        IF NOT EXISTS open_food_facts""")

    def fill_database(self):
        """SQL command to create tables categories
        and products in database"""

        # Create categories table if not exists
        self.cursor.execute("""CREATE TABLE
        IF NOT EXISTS categories (id SMALLINT
        AUTO_INCREMENT PRIMARY KEY,
        category VARCHAR(40)) ENGINE=INNODB""")

        # Create products table if not exists
        self.cursor.execute("""CREATE TABLE
        IF NOT EXISTS products (id SMALLINT
        AUTO_INCREMENT PRIMARY KEY, name TEXT,
        description TEXT, nutri_score CHAR(1),
        stores TEXT, url TEXT, category SMALLINT,
        is_saved SMALLINT, CONSTRAINT category_id
        FOREIGN KEY (category)
        REFERENCES categories (id)) ENGINE=INNODB""")

    def check(self):
        """SQL command to check if
        categories table have any data"""

        self.cursor.execute("""SELECT *
        FROM categories""")
        return self.cursor.fetchall()

    def fill_categories(self, method):
        """SQL command to fill categories
        table with data from a method"""

        try:
            for i in range(len(method)):
                self.cursor.execute("""INSERT INTO
                categories (category) VALUES
                (%(category)s)""",
                                    {"category": method[i]})
        except mysql.connector.errors.IntegrityError:
            pass

    def fill_products(self, method):
        """SQL command to fill
        products table with data
        from a method"""

        try:
            for i in range(len(method)):
                self.cursor.execute("""INSERT INTO
                products (name, description, nutri_score,
                stores, url, category) VALUES
                (%s, %s, %s, %s, %s, %s)""", method[i])
        except mysql.connector.errors.IntegrityError:
            pass

    def fetch_all_categories(self):
        """SQL command to select all
        the data in categories table
        and order by ascendant id"""

        self.cursor.execute("""SELECT *
        FROM categories ORDER BY id ASC""")

    def fetch_products_of_categories(self, user_input):
        """SQL command to select in products table all
        products where category equal a number define
        by user_input"""

        self.cursor.execute(f"""SELECT *
FROM products WHERE category = {user_input}""")

    def fetch_substitute(self, input_product):
        """SQL commands to return a substitute
        with better nutriscore than a product
        select by the user in input_product"""

        # Select the category of the product
        # select by the user in input_products
        self.cursor.execute(
            f"""SELECT category FROM products WHERE id = {input_product}""")

        # Collect the category data
        category = self.cursor.fetchall()

        # Transform tuples collected in category variable in list
        list = [x for elem in category for x in elem]

        # Algorithm to select the best nustriscore
        # in a category of product selected
        self.cursor.execute(f"""SELECT *
FROM products WHERE category = {list[0]}
&& nutri_score = 'a' LIMIT 1""")
        result = self.cursor.fetchall()
        if len(result) == 0:
            self.cursor.execute(
                f"""SELECT *
FROM products WHERE category = {list[0]}
&& nutri_score = 'b' LIMIT 1""")
            result = self.cursor.fetchall()
            if len(result) == 0:
                self.cursor.execute(
                    f"""SELECT *
FROM products WHERE category = {list[0]}
&& nutri_score = 'c' LIMIT 1""")
                result = self.cursor.fetchall()
                if len(result) == 0:
                    self.cursor.execute(
                        f"""SELECT *
FROM products WHERE category = {list[0]}
&& nutri_score = 'd' LIMIT 1""")
                else:
                    self.cursor.execute(
                        f"""SELECT *
FROM products WHERE category = {list[0]}
&& nutri_score = 'c' LIMIT 1""")
            else:
                self.cursor.execute(
                    f"""SELECT *
FROM products WHERE category = {list[0]}
&& nutri_score = 'b' LIMIT 1""")
        else:
            return self.cursor.execute(f"""SELECT *
FROM products WHERE category = {list[0]}
&& nutri_score = 'a' LIMIT 1""")

    def saved_substitute(self, rows_substitute):
        """SQL command to save the substitute found by the user"""

        list = [x for elem in rows_substitute for x in elem]
        self.cursor.execute(f"""UPDATE products
SET is_saved = '1' WHERE id = {list[0]}""")

    def fetch_substitute_of_categories(self, user_input):
        """SQL command to select products in category that
        user saved with method saved_substitute"""

        self.cursor.execute(f"""SELECT *
FROM products WHERE category = {user_input} &&
        is_saved IS NOT NULL""")

    def fetch_substitute_saved(self, user_input):
        """SQL command to select the proposed products by
        method fetch_substitute_of_categories"""

        self.cursor.execute(f"""SELECT *
FROM products WHERE id = {user_input}""")

    def rows_cursor(self):
        """Collect the data from a SQL request"""

        return self.cursor.fetchall()
