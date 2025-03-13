class MySQLDatabase:
    def connect(self):
        print("Connected to MySQL")

class UserService:
    def __init__(self):
        self.db = MySQLDatabase()  
    def get_user(self):
        self.db.connect()
        print("Fetching user data")


from abc import ABC, abstractmethod

class Database(ABC):
    @abstractmethod
    def connect(self):
        pass

class MySQLDatabase(Database):
    def connect(self):
        print("Connected to MySQL")

class PostgreSQLDatabase(Database):
    def connect(self):
        print("Connected to PostgreSQL")

class UserService:
    def __init__(self, db: Database): 
        self.db = db

    def get_user(self):
        self.db.connect()
        print("Fetching user data")


db = PostgreSQLDatabase()
user_service = UserService(db)
user_service.get_user()
