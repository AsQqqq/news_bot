import psycopg2
from start_bot.config import HOST, USER, PASSWORD, DB_NAME

try:
    connection_user = psycopg2.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        database=DB_NAME
    )
    connection_user.autocommit = True
    print("INFO: Connected to database")
    crs_user = connection_user.cursor()
except Exception as _ex:
    print("INFO:Error while working PostgreSQL", _ex)

def table_create_user():
    with connection_user.cursor() as cursor:
        cursor.execute(
            """CREATE TABLE IF NOT EXISTS users(
                id serial PRIMARY KEY NOT NULL,
                user_id bigint NOT NULL,
                status bool NOT NULL DEFAULT (TRUE),
                videogames bool NOT NULL DEFAULT (FALSE),
                livegames bool NOT NULL DEFAULT (FALSE),
                bot bool NOT NULL DEFAULT (FALSE),
                world bool NOT NULL DEFAULT (FALSE));"""
        )

#CONTROL
class control_user_table:
    def user_exists(self, user_id):
        request = "SELECT * FROM users WHERE user_id = %s"
        crs_user.execute(request, (user_id,))
        result = crs_user.fetchone()
        return bool(result)

    def add_user(self, user_id):
        request = "INSERT INTO users (user_id) VALUES (%s)"
        crs_user.execute(request, (user_id,))
    
    def exists_user_sub(self, sub, user_id):
        if sub == "videogames":
            request = "SELECT videogames FROM users WHERE user_id = %s"
        elif sub == "livegames":
            request = "SELECT livegames FROM users WHERE user_id = %s"
        elif sub == "bot":
            request = "SELECT bot FROM users WHERE user_id = %s"
        elif sub == "world":
            request = "SELECT world FROM users WHERE user_id = %s"
        else:
            print(f"ERROR: not found {sub}")
        crs_user.execute(request, (user_id,))
        result = crs_user.fetchone()
        for ret in result:
            bool_ret = ret
        if bool_ret == True:
            return True
        else:
            return False
    
    async def add_user_sub(self, sub, bool_sub, user_id):
        if sub == "videogames":
            request = "UPDATE users SET videogames = %s WHERE user_id = %s"
        elif sub == "livegames":
            request = "UPDATE users SET livegames = %s WHERE user_id = %s"
        elif sub == "bot":
            request = "UPDATE users SET bot = %s WHERE user_id = %s"
        elif sub == "world":
            request = "UPDATE users SET world = %s WHERE user_id = %s"
        else:
            print(f"ERROR: not found {sub}")
        crs_user.execute(request, (bool_sub, user_id,))