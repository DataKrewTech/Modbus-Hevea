
#typical drinking water in the range of 5–50 mS/m,
#while sea water about 5 S/m[2] (or 5,000,000 μS/m)


import minimalmodbus
import time
import requests
import json

url = "https://acqdat.herokuapp.com/device/add-data"
headers = {'content-type': 'application/json'}
device_id = '37af4980d09811e987422683630d76ed'
delay = 1

def send_request(payload):
  try:
    response = requests.api.post(url, data=payload, headers=headers)
    print(response.status_code)
    print(response.json())
  except requests.exceptions.RequestException as e:
    print(e)


minimalmodbus.BAUDRATE = 9600
# port name, slave address (in decimal)
instrument = minimalmodbus.Instrument('/dev/ttyUSB0', 1) # linux
instrument.serial.baudrate = 9600


if __name__ == "__main__":
  while True:
    # Register number, number of decimals, function code
    # Register number, number of decimals, function code
    ec = instrument.read_register(0,2)
    temp = instrument.read_register(10,1)
    print('Electrical Conductivity :' + str(ec) + ' mS/cm')
    print('Water Temperature :' + str(temp) + ' C\n')
    params = {'device_id': device_id,
               'timestamp': "2012-04-23T18:25:43.511Z",
               'sensor_data': {
                 'temperature': {'temp': temp},
                 'Conductivity': {'cond': ec}
               }
              }
    send_params = json.dumps(params, indent=4, default=str)
    send_request(send_params)
    time.sleep(delay)
