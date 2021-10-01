from users_app.confing.MySQLConnection import connectToMySQL
from users_app.models.User import User

class User:
    def __init__(self, id, first_name, last_name, email, created_at):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.created_at = created_at

    @classmethod
    def get_all_users(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL("users_shema").query_db( query )
        users = []
        for n in results:
            users.append( User( n['id'], n['first_name'], n['last_name'], n['email'], n['created_at'] ) )
        return users
    
    @classmethod
    def addDataForm(cls, data):
        query = "INSERT INTO users (first_name , last_name , email, created_at, updated_at) VALUES ( %(first_name)s , %(last_name)s , %(email)s, SYSDATE(), SYSDATE());"
        result = connectToMySQL('users_shema').query_db(query,data)
        return result

    @classmethod
    def editUserData(cls, data):
        query = "UPDATE users SET first_name = %(first_name2)s, last_name = %(last_name2)s, email = %(email2)s, updated_at = SYSDATE() WHERE id=%(id)s;"
        result = connectToMySQL('users_shema').query_db(query, data)
        return result

    @classmethod
    def get_one(cls, data):
        print("8")
        query  = "SELECT * FROM users WHERE id = %(id)s;"
        data = {
            "id" : id
        }
        result = connectToMySQL('users_shema').query_db( query, data )
        user_data = []

        for users in result:
            user_data.append(User(user['id'],user['first_name'], user['last_name'], user['email'],user['created_at'],user['updated_at']))
        print("9", user_data )
        return result

    @classmethod
    def deleteUser(cls, data ):
        query = "DELETE FROM users WHERE id = %(id)s;"
        return connectToMySQL('users_shema').query_db( query, data )