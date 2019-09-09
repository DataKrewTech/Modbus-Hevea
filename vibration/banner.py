import minimalmodbus
import time
import requests
import json

url = "https://acqdat.herokuapp.com/device/add-data"
headers = {'content-type': 'application/json'}
device_id = '79dbfac2d08111e9ae55f2941c37b007'
delay = 1

def send_request(payload):
  response = requests.api.post(url, data=payload, headers=headers)
  print(response.status_code)
  print(response.json())


minimalmodbus.BAUDRATE = 9600
# port name, slave address (in decimal)
instrument = minimalmodbus.Instrument('/dev/ttyUSB0', 1) # linux


if __name__ == "__main__":
  while True:
    # Register number, number of decimals, function code
    temp = instrument.read_register(42, 2, 3)
    zaxis = instrument.read_register(2452, 2, 3)
    print('Temperature:' + str(temp))
    print('Zaxis:' + str(zaxis))
    params = {'device_id': device_id,
               'timestamp': "2012-04-23T18:25:43.511Z",
               'sensor_data': {
                 'temperature': {'temp': temp}
               }
              }
    send_params = json.dumps(params, indent=4, default=str)
    send_request(send_params)
    time.sleep(delay)
