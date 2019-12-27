import minimalmodbus
import time
import requests
import json

url = "https://heveaconnect.herokuapp.com/device/add-data"
headers = {'content-type': 'application/json'}
device_id = '309efbba119111eaaa47b6b16018c425'
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


if __name__ == "__main__":
  while True:
    # Register number, number of decimals, function code
    temp = instrument.read_register(42, 2, 3)
   
    xaxis_peak_velocity_mm_sec = instrument.read_register(2453, 2, 3)
    zaxis_peak_velocity_mm_sec = instrument.read_register(2403, 2, 3)

    xaxis_rms_velocity_mm_sec = instrument.read_register(2452, 2, 3)
    zaxis_rms_velocity_mm_sec = instrument.read_register(2402, 2, 3)
    
    xaxis_peak_velocity_comp_freq_hz = instrument.read_register(2454, 2, 3)
    zaxis_peak_velocity_comp_freq_hz = instrument.read_register(2404, 2, 3)

    xaxis_peak_acceleration_g = instrument.read_register(2456, 2, 3)
    zaxis_peak_acceleration_g = instrument.read_register(2406, 2, 3)
    
    xaxis_rms_acceleration_g = instrument.read_register(2455, 2, 3)
    zaxis_rms_acceleration_g = instrument.read_register(2405, 2, 3)
    
    xaxis_high_frequency_rms_acceleration_g = instrument.read_register(2459, 2, 3)
    zaxis_high_frequency_rms_acceleration_g = instrument.read_register(2409, 2, 3)

    xaxis_kurtosis = instrument.read_register(2458, 2, 3)
    zaxis_kurtosis = instrument.read_register(2408, 2, 3)

    xaxis_crest_factor = instrument.read_register(2457, 2, 3)
    zaxis_crest_factor = instrument.read_register(2407, 2, 3)
    

    print('-----------------------------') 
    print('Temperature:' + str(temp))

    print('xaxis_peak_velocity_mm_sec: ' + str(xaxis_peak_velocity_mm_sec))
    print('zaxis_peak_velocity_mm_sec: ' + str(zaxis_peak_velocity_mm_sec))

    print('xaxis_rms_velocity_mm_sec: ' + str(xaxis_rms_velocity_mm_sec))
    print('zaxis_rms_velocity_mm_sec: ' + str(zaxis_rms_velocity_mm_sec))

    print('xaxis_peak_velocity_comp_freq_hz: ' + str(xaxis_peak_velocity_comp_freq_hz))
    print('zaxis_peak_velocity_comp_freq_hz: ' + str(zaxis_peak_velocity_comp_freq_hz))

    print('xaxis_peak_acceleration_g: ' + str(xaxis_peak_acceleration_g))
    print('zaxis_peak_acceleration_g: ' + str(zaxis_peak_acceleration_g))

    print('xaxis_rms_acceleration_g: ' + str(xaxis_rms_acceleration_g))
    print('zaxis_rms_acceleration_g: ' + str(zaxis_rms_acceleration_g))

    print('xaxis_high_frequency_rms_acceleration_g: ' + str(xaxis_high_frequency_rms_acceleration_g))
    print('zaxis_high_frequency_rms_acceleration_g: ' + str(zaxis_high_frequency_rms_acceleration_g))

    print('xaxis_kurtosis: ' + str(xaxis_kurtosis))
    print('zaxis_kurtosis: ' + str(zaxis_kurtosis))

    print('xaxis_crest_factor: ' + str(xaxis_crest_factor))
    print('zaxis_crest_factor: ' + str(zaxis_crest_factor))


    #print('Zaxis:' + str(zaxis))
    #print('Xaxis:' + str(xaxis))
    params = {'device_id': device_id,
               'timestamp': "2012-04-23T18:25:43.511Z",
               'sensor_data': {
                 'temperature': {'temp': temp},

                 'vibration_peak_velocity_mm_sec': {
                   'x_axis': xaxis_peak_velocity_mm_sec,
                   'z_axis': zaxis_peak_velocity_mm_sec
                  },

                'vibration_rms_velocity_mm_sec': {
                   'x_axis': xaxis_rms_velocity_mm_sec,
                   'z_axis': zaxis_rms_velocity_mm_sec
                  },

                'vibration_peak_velocity_comp_freq_hz': {
                   'x_axis': xaxis_peak_velocity_comp_freq_hz,
                   'z_axis': zaxis_peak_velocity_comp_freq_hz
                  },

                'vibration_peak_acceleration_g': {
                   'x_axis': xaxis_peak_acceleration_g,
                   'z_axis': zaxis_peak_acceleration_g
                  },

                'vibration_high_frequency_rms_acceleration_g': {
                   'x_axis': xaxis_high_frequency_rms_acceleration_g,
                   'z_axis': zaxis_high_frequency_rms_acceleration_g
                  },

                'vibration_kurtosis': {
                   'x_axis': xaxis_kurtosis,
                   'z_axis': zaxis_kurtosis
                  },
                
                'vibration_crest_factor': {
                   'x_axis': xaxis_crest_factor,
                   'z_axis': zaxis_crest_factor
                  },
               }
              }
    send_params = json.dumps(params, indent=4, default=str)
    send_request(send_params)
    time.sleep(delay)
