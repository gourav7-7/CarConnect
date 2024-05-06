from DAO.DatabaseContext import DatabaseContext
class AuthenticationService:
    def __init__(self, db_name):
        self.db_context = DatabaseContext(db_name)

    def authenticate_user(self, username, password):
        query = f"SELECT * FROM customer WHERE username = '{username}' AND password = '{password}'"
        result = self.db_context.runQuery(query)
        if result:
            print("User Authenticated")
        else:
            print("Try Again")

