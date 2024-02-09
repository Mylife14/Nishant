from adb_shell.adb_device import AdbDeviceTcp, UsbHandle
from adb_shell.auth.sign_pythonrsa import PythonRSASigner

device_ip = '100.96.190.150'
rsa_key = 'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDImvDySuc0u15sjTCbQxVQ9rEWnumwEI6jM2razmFslM1BmW6Ij5tv8etsv5YAyUfIbZ4hoZwN0kV7Zu2rdme7xqQi88peDPBwvwV4gDKOhVwxj3DTOGOvZH/7Fg43lCQVeQEaXONBHIc2KyHb0t+H0Ry5+K2q3nOI+3xJd1P362QkbgPNx8+6M+bfbjLa5GczxcV+dEAvlKeUVh53qCofFvzI1brpLDiDZ4cer8P8jfidQPbD1+A7c+i291ssd1mJLhYMLe9dflDOv5PAqqEQ1wky85zOirhNRJEsxyukBPK4A8vE7L8ilD5K6/Bsm+BylzRUmQ6mwwk/r6GF2y6Z my@DESKTOP-7J5G09E'

handle = UsbHandle()
device = AdbDeviceTcp(device_ip, handle, default_transport_timeout_s=9.)
device.connect(rsa_keys=[rsa_key], auth_timeout_s=0.1)

command = 'ls /sdcard/'  
result = device.shell(command)
print(f"Output of '{command}':")
print(result.decode('utf-8'))
