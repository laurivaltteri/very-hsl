# downloaded from: https://files.pythonhosted.org/packages/9a/ac/62edd91cb130cf848476cfa96666b96c162bdb1b4c2941b074083e467dd6/psycopg2_binary-2.9.2-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
# https://pypi.org/project/psycopg2-binary/#files
# zip -r lambda.zip *
import psycopg2

####
def get_connection(): # -> psycopg2.extensions.connection:
    """Return a psycopg2 db connection object credentials fetched from envvars"""

    host = #
    db = #
    port = #
    user = #
    passwd = #
    
    conn = psycopg2.connect(host=host, dbname=db, port=port, user=user, password=passwd)
    return conn
####
def print_results(): # -> str

    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SET search_path TO data")

    query_3last = f"SELECT * FROM hfp_data ORDER BY tst DESC LIMIT 3;"
    query_rows = f"SELECT count(*) FROM hfp_data WHERE oday=CURRENT_DATE;"
    query_avg_spd = f"SELECT avg(spd) FROM hfp_data WHERE oday=CURRENT_DATE;"
    query_rows = f"SELECT count(*) FROM hfp_data WHERE oday='2021-11-16';"
    query_avg_spd = f"SELECT avg(spd) FROM hfp_data WHERE oday='2021-11-16';"

    cur.execute(query_3last)
    last_entries = cur.fetchall()
    cur.execute(query_rows)
    entry_number = cur.fetchall()
    cur.execute(query_avg_spd)
    avg_speed = cur.fetchall()

    print(f"Hello!")
    print(f"3 last messages in hfp system:")
    print(*last_entries, sep='\n')
    print(f"On '2021-11-16' there was {entry_number[0][0]} entries")
    print(f"On '2021-11-16' average speed of vessels was {avg_speed[0][0]} km/h")

def lambda_handler(event, context):
    print_results()