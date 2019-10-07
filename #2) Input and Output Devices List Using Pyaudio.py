import pyaudio

p = pyaudio.PyAudio()
info = p.get_host_api_info_by_index(0)
numdevices = info.get('deviceCount')

for i in range(0, numdevices):
    device = p.get_device_info_by_host_api_device_index(0, i)
    if device.get('maxOutputChannels') > 0:
        print("Device ID:",i,"OUTPUT DEVICE:",device.get('name'))
    elif device.get('maxInputChannels') > 0:
        print("Device ID:",i,"INPUT DEVICE:",device.get('name'))

try:
    print("\n\nDefault Input Device:",p.get_default_input_device_info().get('name'))
    print("Default Output Device:",p.get_default_output_device_info().get('name'))
except OSError as e:
    print("\n\aException :",e)