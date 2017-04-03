
import serial
import sys
import glob
import time


class SerialCommunication(object):
    def __init__(self):
        self.serial_conn = serial.Serial()
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
        elif self.os.startswith('win'):
            print('Windows system: ' + self.os)
            # complete this part
        else:
            print("nothing to do")

        for port in ports:
            try:
                s = serial.Serial(port)
                s.close()
                self.port_list.append(port)
            except serial.SerialException:
                # print('Error in open port: ' + port)
                pass

        return self.port_list

    def open_serial_default_configuration(self, port_name):
        self.serial_conn = serial.Serial(port_name)
        self.serial_conn.baudrate = 9600
        self.serial_conn.parity = 'N'
        self.serial_conn.bytesize = 8
        self.serial_conn.stopbits = 1
        self.serial_conn.timeout = 10
        if self.serial_conn.is_open:
            print('Serial port connection open successful')

        return self.serial_conn

    def open_serial_port(self, port_name, baud_rate=9600,
                         parity='N', byte_size=8, stop_bit=1, timeout=10):
        try:
            self.serial_conn = serial.Serial(port_name)
            self.serial_conn.baudrate = baud_rate
            self.serial_conn.parity = parity
            self.serial_conn.bytesize = byte_size
            self.serial_conn.stopbits = stop_bit
            self.serial_conn.timeout = timeout
            print('Serial port connection open successful')
        except serial.SerialException:
            print('Port can not be open. Check configuration - '
                  + serial.SerialException)

        return self.serial_conn

    def bytes_available(self):
        return self.serial_conn.inWaiting()

    def read_bytes(self, num_bytes=1):
        if num_bytes == 'all':
            return self.serial_conn.read(self.bytes_available())
        else:
            try:
                n = int(num_bytes)
                return self.serial_conn.read(n)
            except ValueError:
                print('the value for num_bytes should be a number not ' +
                      type(num_bytes))
                return None
            except serial.SerialException:
                print('Serial port not open properly' +
                      serial.SerialException)
                return None
            except serial.SerialTimeoutException:
                print('Timeout exception. check number of bytes passed')

    def close_communication(self):
        try:
            self.serial_conn.close()
            self.serial_conn.__del__()
            print('port close succesful')
        except serial.SerialException:
            print('port can not be closed!')
            sys.exit(-1)

    def write_data(self, data=''):
        try:
            self.serial_conn.write(data.encode())
        except serial.SerialException:
            print('Can not be write data to the port. ' +
                  serial.SerialException)

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
    text = ex.read_bytes(10)
    print(text)
    ex.write_data('home')
    time.sleep(2)
    print(ex.bytes_available())
    text = ex.read_bytes('all')
    print(text)
    ex.close_communication()
