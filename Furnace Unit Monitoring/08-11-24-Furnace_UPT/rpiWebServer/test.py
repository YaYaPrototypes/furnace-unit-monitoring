from pymodbus.client.sync import ModbusTcpClient

# Define the Modbus server parameters
MODBUS_SERVER_IP = '172.16.4.235'  # Replace with your server's IP address
MODBUS_SERVER_PORT = 502            # Default Modbus TCP port

# Create a Modbus TCP client
client = ModbusTcpClient(MODBUS_SERVER_IP, port=MODBUS_SERVER_PORT)

# Connect to the server
connection = client.connect()
if connection:
    print("Connected to Modbus server")

    # Adjust the register type and address based on your device
    address = 257
    count = 2  # Number of registers to read

    # Try reading holding registers
    response = client.read_holding_registers(address, count)
    if response.isError():
        print(f"Error reading holding registers: {response}")
    else:
        print(f"Data read from holding register {address}: {response.registers}")

    # Try reading input registers (if applicable)
    response = client.read_input_registers(address, count)
    if response.isError():
        print(f"Error reading input registers: {response}")
    else:
        print(f"Data read from input register {address}: {response.registers}")

    # Close the connection
    client.close()
else:
    print("Failed to connect to Modbus server")
