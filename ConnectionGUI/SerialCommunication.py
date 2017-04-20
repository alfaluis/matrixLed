import serial.tools.list_ports
import sys
import glob
import time
from serial import Serial, tools, SerialException, SerialTimeoutException


class SerialCommunication(object):
    def __init__(self):
        self.serial_conn = Serial()
        self.port_list = []
        self.os = sys.platform
        self.baud_rate = 9600
        self.parity = 'N'
        self.byte_size = 8
        self.stop_bit = 1
        self.timeout = 10

    def list_serial_ports(self):
        # List all ports
        if self.os.startswith('linux'):
            print('Linux system: ' + self.os)
            ports = glob.glob('/dev/tty[A-Za-z]*')
            for port in ports:
                try:
                    s = Serial(port)
                    s.close()
                    self.port_list.append(port)
                except SerialException:
                    # print('Error in open port: ' + port)
                    pass

        elif self.os.startswith('win'):
            print('Windows system: ' + self.os)
            print(tools.list_ports.comports())
            try:
                ports = list(tools.list_ports.comports())
                for port in ports:
                    print(port[0])
                    self.port_list.append(port[0])
            except SerialException:
                print("Error open port")
        else:
            print("nothing to do")

        return self.port_list

    def open_serial_default_configuration(self, port_name):
        self.serial_conn = Serial(port_name)
        self.serial_conn.baudrate = 9600
        self.serial_conn.parity = 'N'
        self.serial_conn.bytesize = 8
        self.serial_conn.stopbits = 1
        self.serial_conn.timeout = 10
        if self.serial_conn.isOpen():
            print('Serial port connection open successful')

        return self.serial_conn

    def open_serial_port(self, port_name, baud_rate=9600,
                         parity='N', byte_size=8, stop_bit=1, timeout=10):
        try:
            self.serial_conn = Serial(port_name)
            self.serial_conn.baudrate = baud_rate
            self.serial_conn.parity = parity
            self.serial_conn.bytesize = byte_size
            self.serial_conn.stopbits = stop_bit
            self.serial_conn.timeout = timeout
            print('Serial port connection open successful')
        except SerialException:
            print('Port can not be open. Check configuration - '
                  + SerialException)

        return self.serial_conn

    def bytes_available(self):
        return self.serial_conn.inWaiting()

    def read_bytes(self, num_bytes='1'):
        if num_bytes == 'all':
            return self.serial_conn.read(self.bytes_available())
        else:
            try:
                n = int(num_bytes)
                return self.serial_conn.read(n)
            except ValueError:
                print('the value for num_bytes should be a number not ' +
                      str(type(num_bytes)))
                return None
            except SerialException:
                print('Serial port not open properly' +
                      str(SerialException))
                return None
            except SerialTimeoutException:
                print('Timeout exception. check number of bytes passed')

    def close_communication(self):
        try:
            self.serial_conn.close()
            self.serial_conn.__del__()
            print('port close successful')
        except SerialException:
            print('port can not be closed!')
            sys.exit(-1)

    def write_data(self, data='', end_line=''):
        if end_line == 'CR':
            data = data + '/r'
        elif end_line == 'NL':
            data = data + '/n'
        elif end_line == 'CR/NL':
            data = data + '/r/n'

        try:
            data = data
            self.serial_conn.write(data.encode())
        except SerialException:
            print('Can not be write data to the port. ' +
                  str(SerialException))

if __name__ == '__main__':
    flag = False
    ex = SerialCommunication()
    ex.list_serial_ports()
    print(ex.port_list)
    ex.open_serial_default_configuration(ex.port_list[0])
    time.sleep(5)
    print(ex.bytes_available())
    text = ex.read_bytes('all')
    print(text)
    ex.write_data('1')
    time.sleep(5)
    print(ex.bytes_available())
    text = ex.read_bytes('all')
    print(text)
    ex.write_data('0')
    time.sleep(2)
    print(ex.bytes_available())
    text = ex.read_bytes('10')
    print(text)
    ex.write_data('home')
    time.sleep(2)
    print(ex.bytes_available())
    text = ex.read_bytes('all')
    print(text)
    ex.close_communication()
