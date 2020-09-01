"""Creation of methods to display the program scenario in terminal"""


class View:
    """Methods of objects type View"""
    @staticmethod
    def user_input():
        """Mechanics of all user input"""
        result = None
        while result is None:
            try:
                result = int(input(
                    "Appuyer sur le numéro correspondant "
                    "à votre choix, puis Entrée"))
            except ValueError:
                pass
        return result

    @staticmethod
    def input_1_2_error(user_input, method):
        """Mechanics of all user input with 1 or 2 choice"""
        if user_input != 1 and user_input != 2:
            return method
        else:
            pass

    @staticmethod
    def input_categories():
        """Mechanics of user input categories"""
        user_input_categories = View.user_input()
        while user_input_categories not in range(11):
            user_input_categories = View.user_input()
        else:
            return user_input_categories

    @staticmethod
    def input_products(user_input_categories):
        """Mechanics of user input products"""
        displayed_products_list = []
        for x in range(21):
            displayed_products_list.append(x)
        displayed_products_list.remove(0)
        displayed_products_list = \
            [i + (20 * (user_input_categories - 1))
             for i in displayed_products_list]

        user_input_products = View.user_input()
        while user_input_products not in displayed_products_list:
            user_input_products = View.user_input()
        else:
            return user_input_products

    @staticmethod
    def print_onset_text():
        """Print the onset text of the program"""
        print("1 - Quel aliment souhaitez-vous remplacer ? "
              "2 - Retrouver mes aliments substitués.")

    @staticmethod
    def print_saved_text():
        """Print the saved question text"""
        print("Voulez-vous enregistrer ce produit dans "
              "votre liste d'aliments de substitution"
              "? OUI - 1, NON - 2")

    @staticmethod
    def print_restart_text():
        """Print the restart question text"""
        print("Voulez-vous recommencer ? "
              "OUI - 1, NON - 2")

    @staticmethod
    def print_category_text(rows):
        """Print all categories the user can choose from"""
        print("Choisissez parmi ces catégories : ")
        for row in rows:
            print("{0} - {1}".format(row[0], row[1]))

    @staticmethod
    def print_products_text(rows):
        """Print all products the user can choose from"""
        for row in rows:
            print("Choisissez parmi ces produits :"
                  "{0} - {1}".format(row[0], row[1]))

    @staticmethod
    def print_substitute(rows):
        """Print the substitute found with his informations"""
        for row in rows:
            print("Nom : {1}, Description : {2},"
                  "Nutri-Score : {3},"
                  "Magasins : {4}, URL : {5}"
                  .format(row[0], row[1], row[2],
                          row[3], row[4], row[5]))

    @staticmethod
    def print_substitute_text(rows):
        """Print all substitutes the user can choose from"""
        for row in rows:
            print("Choisissez parmi ces produits :"
                  "{0} - {1}".format(row[0], row[1]))

    @staticmethod
    def print_original_product_text():
        """Print the restart question text"""
        print("Voulez-vous voir les produits "
              "que vous vouliez substitué par celui-ci ? "
              "OUI - 1, NON - 2")

    @staticmethod
    def print_original_products(rows):
        """Print the original products found with his informations"""
        for row in rows:
            print("Nom : {1}, Description : {2},"
                  "Nutri-Score : {3},"
                  "Magasins : {4}, URL : {5}"
                  .format(row[0], row[1], row[2],
                          row[3], row[4], row[5]))
