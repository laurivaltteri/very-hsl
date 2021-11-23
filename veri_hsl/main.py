
import paho.mqtt.client as mqtt
import os
import logging
import watchtower

from dotenv import load_dotenv
import mqtt_functions as iofunc

appname = os.getenv('APP')
base_path = '/app/' if appname == 'prod' else '.'

#------- Utility functions --------
load_dotenv()

logging.getLogger().handlers.clear()
logger = logging.getLogger(__name__)
cwatch_logger = watchtower.CloudWatchLogHandler(log_group='watchtower', stream_name='hsl-hfp-0.0.1')
logging.basicConfig(
    # match gunicorn format
    #filename='app.log', 
    #filemode='w',
    format='%(asctime)s [%(process)d] [%(levelname)s] %(message)s',
    datefmt='[%Y-%m-%d %H:%M:%S %z]',
    level=logging.INFO,
    handlers=[cwatch_logger]
    )

logging.info(f"Hello! Running version: {appname}")



## run the code
def run():
    client_name = "HFP_messages"
    broker_address = "mqtt.hsl.fi"
    sub_topic = "/hfp/v2/journey/ongoing/vp/#"

    conn = iofunc.get_connection()
    client = mqtt.Client(client_name, userdata=conn) #MQTT connection
    client.connect(broker_address)
    client.on_message = iofunc.on_message
    client.on_log = iofunc.on_log
    client.subscribe(sub_topic)
    client.loop_forever()

if __name__ == "__main__":
    run()
