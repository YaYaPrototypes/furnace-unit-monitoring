#!/usr/bin/python3
from pymodbus.constants import Endian
from pymodbus.payload import BinaryPayloadDecoder
from pymodbus.client import ModbusSerialClient
from pymodbus.client import ModbusTcpClient
from fractions import Fraction
import time

ip_address ="172.16.4.237"
#if You Read Plc To Python #PLC Macro Address $200 You Simply Call 200 #PLC MAcro Address $M200 You Should Call 2200
HMI_Doller_Address = 746

#client = ModbusSerialClient(port='/dev/ttyUSB0', baudrate=9600,parity='E')
#client = ModbusTcpClient("172.16.4.235",port = 502)
client = ModbusTcpClient(ip_address,port = 502)
try:
    client.connect()
    print ("Client Connect Success Fully")

    while True:
        #Register Address,bitdivision,salveid
        #macro side in plc $Variable to Assign After Here Use That Register Value
        data = client.read_holding_registers(HMI_Doller_Address , 2 , slave = 1 ,timeout=1000)
        print (data)
        decoder = BinaryPayloadDecoder.fromRegisters(data.registers,  Endian.Big, wordorder=Endian.Little)
        print("decoder")
        address_result   = decoder.decode_32bit_float()
        string_convert   = str(address_result)
        length_of_number = len(string_convert)
        #print ("The Register Address Value Is :  ",(address_result))
        #print("Total Length Of Character : ",(length_of_number))
        if (length_of_number==9):
            Round_Value = round(address_result)
            KWh = Round_Value
            print (KWh)

        elif (length_of_number==10):
            Round_Value = round(address_result)
            MWh = Round_Value/1000000000
            v=round(MWh,8)
            print ("KWh",MWh)
            print (v)
        elif (length_of_number==11):
            Round_Value = round(address_result)
            MWh = Round_Value/100000
            v=round(MWh,8)
            print ("MWh",MWh)
            print (v)
        elif (length_of_number==12):
            Round_Value = round(address_result)
            MWh = Round_Value/10000000
            v=round(MWh,8)
            print ("MWh",MWh)
            print (v)
        elif (length_of_number==13):
            Round_Value = round(address_result)
            MWh = Round_Value/1000000000
            v=round(MWh,9)
            print ("MWh",MWh)
            print (v)
    
        else:
            print ("Something Wrong If You read Energy meter data shuold be contain minimum 10 indegers \n Please Check KWh Or MWh or GWh")
        
        time.sleep(0.6)

except:
    print  ("NOT OK")



#if You Read Energy Meter Reading HMI To Read Pymodbus
#Please Add Macro Side As per Given Steps
#$36 = FMOV({Link1}219@w4321) (Signed DW)


