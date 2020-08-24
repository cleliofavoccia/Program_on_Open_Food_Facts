"""Execute the program"""
from Controller import Controller

if __name__ == "__main__":
    """Call of methods from Controller class to execute the program"""
    controller = Controller()
    # Create and fill the database
    controller.install_database()
    # Play the user scenario
    controller.user_scenario()
