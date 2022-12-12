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
                world bool NOT NULL DEFAULT (FALSE),
                storyteller_user TEXT);"""
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
    
    def select_status(self, user_id):
        request = "SELECT status FROM users WHERE user_id = %s"
        crs_user.execute(request, (user_id,))
        result = crs_user.fetchone()
        for ret in result:
            bool_ret = ret
        if bool_ret == True:
            return True
        else:
            return False
    
    async def update_status(self, user_id, status):
        request = "UPDATE users SET status = %s WHERE user_id = %s"
        crs_user.execute(request, (status, user_id,))

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
    
    async def select_user_and_true_status(self):
        request = "SELECT user_id FROM users WHERE status = True"
        crs_user.execute(request)
        result = crs_user.fetchall()
        return result
    
    async def select_user_and_true_status_and_sub_to_news_bot(self):
        request = "SELECT user_id FROM users WHERE status = True AND bot = True"
        crs_user.execute(request)
        result = crs_user.fetchall()
        return result

    def select_storyteller_user(self, user_id):
        request = "SELECT storyteller_user FROM users WHERE user_id = %s"
        crs_user.execute(request, (user_id,))
        result = crs_user.fetchone()
        for ret in result:
            if ret == "NotFound":
                return "NotFound"
            elif ret == "Safi":
                return "Safi"
            elif ret == "Gerald":
                return "Gerald"
            else:
                print(f"ERROR: not found {ret}")

    def update_storyteller_user(self, user_id, storyteller_user):
        request = "UPDATE users SET storyteller_user = %s WHERE user_id = %s"
        crs_user.execute(request, (storyteller_user, user_id,))