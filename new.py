class User:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
    def get_all(self):
        return (self.name, self.surname, self.gender)
    def __str__(self):
        return f"{self.name} {self.surname} {self.gender}"

def create_table_user(cursor):
    command = """
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT,
        surname TEXT,
        gender TEXT
    )
    """
    cursor.execute(command)


def add_user(cursor,user):
    command = """
    INSERT INTO users (name, surname, gender) VALUES (?, ?, ?);
    """
    cursor.execute(command, user.get_all())

def get_users_list(cursor):
    command = """
    SELECT * FROM users;
    """
    result = cursor.execute(command)
    users = result.fetchall()
    for u in users:
        print(u)

def get_users_list_by_gender(cursor,gender):
    command = """
    SELECT * FROM users WHERE gender = ?;
    """
    result = cursor.execute(command,(gender,))
    users = result.fetchall()
    for u in users:
        print(u)

def get_user(cursor,id):
    command = """
    SELECT * FROM users WHERE id = ?
    """   
    result = cursor.execute(command, (id,))
    user = result.fetchall()
    print(user)

def delete_users(cursor):
    command = """
    DELETE FROM users
    """   
    cursor.execute(command)

def delete_user_by_id(cursor,id):
    command = """
    DELETE FROM users WHERE id = ?
    """   
    cursor.execute(command,(id,))

def update_user_name(cursor,value,id):
    command = """
    UPDATE users SET name = ? WHERE id = ?;
    """   
    cursor.execute(command,(value,id,))

if __name__ == '__main__':
    with sqlite3.connect('main.db') as cursor:
        create_table_user(cursor)
        delete_users(cursor)
        add_user(cursor,User("Максим","Максимов","male"))
        add_user(cursor,User("Владимир","Петров","male"))
        add_user(cursor,User("Юлия","Сидорова","female"))
        get_users_list(cursor)
        get_user(cursor,1)
        update_user_name(cursor,"Олег",1)
        get_user(cursor,1)
        print(25*"_")
        delete_user_by_id(cursor,1)
        get_users_list(cursor)
        print(25*"_")
        get_users_list_by_gender(cursor,"male")
        print(25*"_")
        get_users_list_by_gender(cursor,"female")