from controllers.account_controller import AccountController

CURRENT_DB_NAME = 'queries/database/vehicle_management.db'
def main():
    USERNAME = "wow"
    PASSWORD = "PASSWORD"
    accountController= AccountController(dbName=CURRENT_DB_NAME)
    accountController.login(username=USERNAME, password=PASSWORD)

    accountController.create_account(userType="client",username="wow", password="PASSWORD",
                                     email="haHAA@gmail.com", phoneNumber=912848912,
                                     address="Nowhere")


if __name__ == '__main__':
    main()
