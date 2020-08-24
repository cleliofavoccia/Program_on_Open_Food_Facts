"""Program mechanics and scenarios with instantiation of view's and model's object """
import requests
from Model import DataBase
from View import View


class Controller:
    """Attributes and methods
    (install database, scenario_fetch_substitute, etc...)
    of object type Controller"""
    def __init__(self):
        """Attributes of Controller : Instantiation of view's and model's object"""
        self.database = DataBase()
        self.view = View()

    def fetch_categories_on_OFF(self):
        """Fetch categories on API Open Food Facts with request method"""

        # Collect categories name from API OFF json
        r = requests.get('https://fr.openfoodfacts.org/categories.json')
        j_son = r.json()
        j_son = j_son['tags']
        category_to_collect = ["name"]
        default_value = "Donnée manquante"
        category_collected = []

        # Collect 11 categories names recovered from json
        # in category_collected list variable
        for data in j_son:
            if len(category_collected) <= 10:
                for title in range(len(category_to_collect)):
                    category_collected.append(
                        data.get(category_to_collect[title],
                                 default_value))

        return category_collected

    def fetch_products_on_OFF(self):
        """Fetch products of different categories
        collected in fetch_categories_on_OFF method
        on API Open Food Facts with request method"""

        # Collect categories json url from API OFF json
        r = requests.get('https://fr.openfoodfacts.org/categories.json')
        j_son = r.json()
        j_son = j_son['tags']
        category_url_to_collect = ["url"]
        default_value = "Donnée manquante"
        category_url_collected = []
        name_collected = []
        description_collected = []
        nutri_score_collected = []
        stores_collected = []
        url_collected = []
        category_id = []

        # Collect 11 categories urls recovered from json
        # in category_url_collected list variable
        for data in j_son:
            if len(category_url_collected) <= 10:
                for title in range(len(category_url_to_collect)):
                    category_url_collected.append(
                        data.get(category_url_to_collect[title],
                                 default_value)+'.json')

        # Collect products name, description,
        # nutriscore, stores and url from API OFF
        # json in category_url_collected
        for index in category_url_collected:
            r1 = requests.get(index)
            j2_son = r1.json()

            try:
                j2_son = j2_son["products"]
            except KeyError:
                default_value = "Donnée manquante"
            try:
                name_to_collect = ['product_name_fr']
                description_to_collect = ['generic_name_fr']
                nutri_score_to_collect = ['nutriscore_grade']
                stores_to_collect = ['stores']
                url_to_collect = ['url']

                # Collect products name, description,
                # nutriscore, stores and url recovered from json
                # in different list variable (name_to_collect,
                # description_to_collect, etc...)
                for data in j2_son:
                    for title in range(len(name_to_collect)):
                        name_collected.append(
                            data.get(name_to_collect[title]))
                    for title in range(len(description_to_collect)):
                        description_collected.append(
                            data.get(description_to_collect[title]))
                    for title in range(len(nutri_score_to_collect)):
                        nutri_score_collected.append(
                            data.get(nutri_score_to_collect[title]))
                    for title in range(len(stores_to_collect)):
                        stores_collected.append(
                            data.get(stores_to_collect[title]))
                    for title in range(len(url_to_collect)):
                        url_collected.append(
                            data.get(url_to_collect[title]))

                    for i in range(len(category_url_collected)):
                        if index == category_url_collected[i]:
                            category_id.append(i + 1)
            except KeyError:
                default_value = "Donnée manquante"

        # Zip all lists build (name_to_collect, description_to_collect, etc...) in
        # products_collect list variable
        products_collected = list(
            zip(name_collected, description_collected,
                nutri_score_collected, stores_collected,
                url_collected, category_id))

        return products_collected

    def install_database(self):
        """Create and fill database and tables of open_food_facts database"""
        self.database.create_database()
        self.database.fill_database()

        if len(self.database.check()) == 0:
            self.database.fill_categories(
                                           self.fetch_categories_on_OFF())
            self.database.fill_products(
                                         self.fetch_products_on_OFF())

    def restart(self):
        """Mechanics of restart question"""
        self.view.print_restart_text()
        user_input_restart = self.view.user_input()
        if user_input_restart == 1:
            self.user_scenario()
        if user_input_restart == 2:
            exit()
        else:
            self.view.input_1_2_error(user_input_restart,
                                     self.restart())

    def save(self, rows):
        """Mechanic of save proposition"""
        self.view.print_saved_text()
        user_input_saved = self.view.user_input()
        if user_input_saved == 1:
            self.database.saved_substitute(
                rows)
        elif user_input_saved == 2:
            pass
        else:
            self.view.input_1_2_error(user_input_saved,
                                     self.save(rows))

    def scenario_fetch_substitute(self):
        """Mechanics of "Which aliment do you want to replace?" scenario"""
        # Load categories
        self.database.fetch_all_categories()
        rows_categories = self.database.rows_cursor()

        # Print categories
        self.view.print_category_text(rows_categories)

        # Insertion of the category chosen by the user
        user_input_categories = self.view.input_categories()

        # Load products of category
        self.database.fetch_products_of_categories(
            user_input_categories)
        rows_products = self.database.rows_cursor()

        # Print products of category
        self.view.print_products_text(rows_products)

        # Insertion of the product chosen by the user
        user_input_product = self.view.input_products(user_input_categories)

        # Load substitute
        self.database.fetch_substitute(
            user_input_product)
        rows_substitute = self.database.rows_cursor()

        # Print substitute
        self.view.print_substitute(rows_substitute)

        # Save substitute question
        self.save(rows_substitute)
        # Restart question
        self.restart()

    def scenario_my_substitutes(self):
        """Mechanics of "Find my saved substitute aliments" scenario"""
        # Load categories
        self.database.fetch_all_categories()
        rows_categories = self.database.rows_cursor()

        # Print categories
        self.view.print_category_text(rows_categories)

        # Insertion of the category chosen by the user
        user_input_categories = self.view.user_input()

        # Load substitutes of category
        self.database.fetch_substitute_of_categories(
            user_input_categories)
        rows_substitutes = self.database.rows_cursor()

        # Print substitutes of category
        self.view.print_substitute_text(rows_substitutes)

        # Insertion of the substitute chosen by the user
        user_input_substitute = self.view.user_input()

        # Load substitute
        self.database.fetch_substitute_saved(
            user_input_substitute)
        rows_substitute = self.database.rows_cursor()

        # Print substitute
        self.view.print_substitute(rows_substitute)

        # Restart question
        self.restart()

    def user_scenario(self):
        """Mechanics of the program"""
        self.view.print_onset_text()
        user_input = self.view.user_input()
        if user_input == 1:
            self.scenario_fetch_substitute()
        if user_input == 2:
            self.scenario_my_substitutes()
        else:
            self.view.input_1_2_error(user_input,
                                     self.user_scenario())
