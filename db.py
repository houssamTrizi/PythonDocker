import logging
import time

import mysql.connector

from config import *


def init_db():
    with open("./app/test.txt", 'w') as f:
        f.write("did it")
    logger = logging.getLogger(__name__)
    mydb: mysql.connector.MySQLConnection = mysql.connector.MySQLConnection()
    count = 0
    while count < DB_CONNECT_RETRY_COUNT:
        try:
            mydb = mysql.connector.connect(
                host=DB_HOST,
                user=DB_USER,
                password=DB_PASSWORD)
        except mysql.connector.errors.InterfaceError as e:
            logger.warning(f'Failed to connect to mysql db... retrying in {DB_CONNEC_SLEEP_BEFORE_RETRY}s')
            time.sleep(DB_CONNEC_SLEEP_BEFORE_RETRY)
        finally:
            count += 1
    if not mydb.is_connected():
        raise ConnectionError("Failed to connect to mysql db")
    cursor = mydb.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS inventory")
    cursor.close()

    mydb = mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_INVENTORY_NAME
    )
    cursor = mydb.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS widgets (name VARCHAR(255), description VARCHAR(255))")
    cursor.close()

    return mydb
