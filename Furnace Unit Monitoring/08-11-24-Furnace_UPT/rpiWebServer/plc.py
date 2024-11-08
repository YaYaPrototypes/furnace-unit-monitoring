from pymodbus.constants import Endian
from pymodbus.payload import BinaryPayloadDecoder
from pymodbus.client.sync import ModbusTcpClient
import time

#client = ModbusSerialClient(port='/dev/ttyUSB0', baudrate=9600,parity='E')
#client = ModbusTcpClient("172.16.4.235",port = 502)
client = ModbusTcpClient("172.16.4.235",port = 502)
try:
  client.connect()
  print ("OK")
  while True:
   #Register Address,bitdivision,salveid
   #macro side in plc $Variable to Assign After Here Use That Register Value
   data = client.read_holding_registers(257 , 2 ,slave = 1)

   if data.isError():
      print ("Error")
      print (data)
   else:
      decoder = BinaryPayloadDecoder.fromRegisters(data.registers,  Endian.Big, wordorder=Endian.Little)
      volt = decoder.decode_32bit_float()
      print(volt)
      print ("The V1 Volt is ",(volt))
      vo=(volt/1000000000)
      vr=round(vo,6)
      print("actual result Value:" ,vo)
      print("round Value:" ,vr)
   time.sleep(1)

except:
 print  ("NOT OK")

