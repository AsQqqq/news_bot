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