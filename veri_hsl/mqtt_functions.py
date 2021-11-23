## MTQQ connections
import psycopg2
import json
import os
import logging
from fastapi import HTTPException
from random import random


msg_count = 0

def get_connection(): # -> psycopg2.extensions.connection:
    """Return a psycopg2 db connection object credentials fetched from envvars"""

    host = os.getenv("AWSRDS_HOST")
    db = os.getenv("AWSRDS_DB")
    port = os.getenv("AWSRDS_PORT")
    user = os.getenv("AWSRDS_USER")
    passwd = os.getenv("AWSRDS_PASSWD")

    try: 
        conn = psycopg2.connect(host=host, dbname=db, port=port, user=user, password=passwd)
    except psycopg2.DatabaseError as e:
        raise HTTPException(status_code=500, detail=str(e))    
    
    return conn

def on_message(client, userdata, message):
    """Behaviour of mqtt client on message event"""
    global msg_count
    global conn
    if (userdata.closed == 1):
        conn = get_connection()
        userdata = conn
    cur = userdata.cursor()
    dict_msg = json.loads(message.payload)
    json_msg = json.dumps(dict_msg.pop('VP'))

    query_sql = f"""INSERT INTO data.hfp_data
    SELECT * FROM json_populate_record(NULL::data.hfp_data, %s)
    """
    try:
        cur = userdata.cursor()
        cur.execute(query_sql, (json_msg,))
    except psycopg2.DatabaseError as e: 
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        userdata.commit()
        cur.close()
        msg_count += 1

def on_log(client, userdata, level, buf):
    """Behaviour of mqtt client on log event"""
    if random() > .99:
        global msg_count
        logging.info(f"log: {buf}")
        logging.info(f"message count: {msg_count}")