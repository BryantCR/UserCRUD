from users_app.confing.MySQLConnection import connectToMySQL

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

    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    


    # @classmethod
    # def get_all(cls):
    #     query = "SELECT * FROM users;"
    #     results = connectToMySQL('users_schema').query_db(query)
    #     users = []
    #     for u in results:
    #         users.append( cls(u) )
    #     return users

    # @classmethod
    # def save(cls, data):
    #     query = "INSERT INTO users (first_name,last_name,email) VALUES (%(first_name)s,%(last_name)s,%(email)s);"

    #     # comes back as the new row id
    #     result = connectToMySQL('users_schema').query_db(query,data)
    #     return result

    # @classmethod
    # def get_one(cls,data):
    #     query  = "SELECT * FROM users WHERE id = %(id)s";
    #     result = connectToMySQL('users_schema').query_db(query,data)
    #     return cls(result[0])

    # @classmethod
    # def update(cls,data):
    #     query = "UPDATE users SET first_name=%(first_name)s,last_name=%(last_name)s,email=%(email)s,updated_at=NOW() WHERE id = %(id)s;"
    #     return connectToMySQL('users_schema').query_db(query,data)

    # @classmethod
    # def destroy(cls,data):
    #     query  = "DELETE FROM users WHERE id = %(id)s;"
    #     return connectToMySQL('users_schema').query_db(query,data)
