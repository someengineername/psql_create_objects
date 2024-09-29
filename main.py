import db_config
import psycopg2
import names
import random


def main():
    try:
        for i in range(20_000):
            connection = psycopg2.connect(
                host='192.168.0.132',
                port='5432',
                user=db_config.user,
                password=db_config.password,
                database=db_config.db_name
            )

            connection.set_session(autocommit=True)

            first_name = names.get_first_name()
            last_name = names.get_last_name()

            class_id = random.randint(1, 5)
            group_id = random.randint(1, 8)

            with connection.cursor() as cursor:
                command_new_user = f"insert into user_scheme (name,surname,class_id,group_id) values ('{first_name}','{last_name}',{class_id},{group_id})"
                cursor.execute(command_new_user)

            print(f'user generated {i}')

    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
