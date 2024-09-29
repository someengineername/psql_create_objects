import db_config
import psycopg2
import names
import random
from argparse import ArgumentParser
from time import sleep


def main(type: str, counter_str: str, delay: float):
    base_counter = int(counter_str)

    match type:
        case 'gen':

            try:
                connection = psycopg2.connect(
                    host='192.168.0.132',
                    port='5430',
                    user=db_config.user,
                    password=db_config.password,
                    database=db_config.db_name
                )

                connection.set_session(autocommit=True)

                temp_int = 0
                while ...:
                    sleep(delay)

                    if temp_int == base_counter:
                        break

                    first_name = names.get_first_name()
                    surname = names.get_last_name()

                    class_id = random.randint(1, 5)
                    group_id = random.randint(1, 8)

                    with connection.cursor() as cursor:
                        command_new_user = f"insert into user_scheme (name,surname,group_id,class_id) values ('{first_name}','{surname}',{group_id},{class_id})"
                        cursor.execute(command_new_user)
                    temp_int += 1

                    print(f'User added: {first_name} {surname} {group_id} {class_id}')
            except Exception as e:
                print(e)

        case 'read':
            try:
                connection = psycopg2.connect(
                    host='192.168.0.132',
                    port='5430',
                    user=db_config.user,
                    password=db_config.password,
                    database=db_config.db_name
                )

                connection.set_session(autocommit=True)

                temp_int = 0
                while ...:
                    sleep(delay)

                    if temp_int == base_counter:
                        break

                    first_name = names.get_first_name()
                    surname = names.get_last_name()

                    class_id = random.randint(1, 5)
                    group_id = random.randint(1, 8)

                    with connection.cursor() as cursor:
                        command_get_user_id = f'select * from user_scheme us where group_id = {group_id} and class_id = {class_id}'
                        cursor.execute(command_get_user_id)
                        user_id = cursor.fetchall()
                        print(f'Result extraction: {len(user_id)}')

                    temp_int += 1
            except Exception as e:
                print(e)


if __name__ == "__main__":
    parser = ArgumentParser()

    parser.add_argument('-type', type=str, required=True,
                        help='type of application run.')
    parser.add_argument('-counter', type=str, required=False,
                        help='counter of run. With {-1} specified will run indefinitely')
    parser.add_argument('-delay', type=float, required=False, default=0.0,
                        help='delay between iterations of required command. Default - no delay')

    args = parser.parse_args()

    main(args.type, args.counter, args.delay)
