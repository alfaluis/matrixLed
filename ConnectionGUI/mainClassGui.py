from PyQt5 import QtGui, QtWidgets, QtCore
import sys
from designerWindow import Ui_MiClassGui
from portConfigDialog import Ui_dialog_port_conf
from SerialCommunication import SerialCommunication


class MainClass(QtWidgets.QMainWindow, Ui_MiClassGui, SerialCommunication):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self)
        main_windows = QtWidgets.QMainWindow()
        Ui_MiClassGui.setupUi(self, main_windows)
        SerialCommunication.__init__(self)
        self.setupUi(self)
        self.dialog = QtWidgets.QDialog()
        self.dialog.ui = Ui_dialog_port_conf()
        self.dialog.ui.setupUiDialog(self.dialog)

        # configuration buttons connection
        self.btn_config_port.clicked.connect(self.dialog_config_port)
        self.btn_quit.clicked.connect(self.close_application)
        self.dialog.ui.btn_ok_cancel.accepted.connect(self.accept)
        self.dialog.ui.btn_ok_cancel.rejected.connect(self.reject)
        self.btn_start.clicked.connect(self.start_serial_communication)
        self.btn_stop.clicked.connect(self.close_serial_communication)
        self.btn_send.clicked.connect(self.send_text)
        self.txt_send.returnPressed.connect(self.send_text)
        self.btn_color.clicked.connect(self.get_color)

        # private attribute to check if will be used the self configuration
        self.__self_configuration = False
        self.port_selected = ''
        self.color = '00FF00'

        # create timer (thread) execution
        self.timer = QtCore.QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.timer_process)
        self.__fill_cmb_end_line()

    def __fill_dialog(self):
        """
        Private method. It fill the opened configuration port dialog.
        This method put inside of comboBox the baud rate and port available
        :return: Nothing
        """
        # fill baud rate combo box in
        list_baudrate = ['300', '600', '1200', '2400', '4800', '9600', '14400',
                         '19200', '28800', '38400', '57600', '115200']
        for baud in list_baudrate:
            self.dialog.ui.cmb_baudrate.addItem(baud)

        self.list_serial_ports()
        print(len(self.port_list))
        for port in self.port_list:
            self.dialog.ui.cmb_ports.addItem(port)

    def __fill_cmb_end_line(self):
        """ private method. It is used to fill the end line combo box"""
        self.cmb_endline.addItem('none')
        self.cmb_endline.addItem('CR')
        self.cmb_endline.addItem('NL')
        self.cmb_endline.addItem('CR/NL')

    def accept(self):
        """Function called once the config dialog configuration was accepted"""
        print("accept here")
        # set true self configuration
        self.__self_configuration = True
        # save the selected port
        self.port_selected = self.dialog.ui.cmb_ports.currentText()
        # save the baud rate selected
        self.baud_rate = self.dialog.ui.cmb_baudrate.currentText()
        # add the port to the available ports list
        self.cmb_ports.addItem(self.port_selected)
        print(str(self.baud_rate) + ' - ' + self.port_selected)

    def reject(self):
        print("reject here")
        pass

    def get_color(self):
        color_obj = QtWidgets.QColorDialog.getColor()
        self.color = color_obj.name().replace('#', '').upper()
        print(self.color)

    def dialog_config_port(self):
        """ 
        Function called when is press the config port button. 
        It fill the config dialog (__fill_dialog() function) and show it
         :param: Object
         :return: Nothing
        """
        print('opening dialog')
        self.__fill_dialog()
        self.dialog.show()

    def close_application(self):
        """
        Function that finish the GUI (or class). It close ports opened and close GUI
        :return: Nothing
        """
        print('close GUI')
        self.close_serial_communication()
        self.timer.stop()
        self.close()

    def start_serial_communication(self):
        """ 
        This function is called when the start_communication button is pressed. It call a function open_serial_port, 
        which try to open a serial port based in a own/default configuration. In addition, it start a timer thread
        """
        if self.__self_configuration:
            self.open_serial_port(port_name=self.port_selected, baud_rate=self.baud_rate)
        else:
            self.open_serial_default_configuration(port_name=self.port_selected)
        self.timer.start(1000)

    def close_serial_communication(self):
        """Function that close properly all running process"""
        self.close_communication()
        self.timer.stop()

    def send_text(self):
        """ 
        Function called once the send_button is pressed or if the enter button is pressed in the text field.
        It send wrote text to serial port. Note that in order to avoid problem with timer process, the timer process is
         disable after finish the write task.
        """
        self.timer.stop()
        wrote_text = self.color + self.txt_send.text()
        print(wrote_text)
        port = self.cmb_ports.currentText()
        self.txt_send.setText('')
        self.txt_write.append(port + '>> ' + wrote_text)
        self.write_data(wrote_text, self.cmb_endline.currentText())
        self.timer.start(1000)

    def timer_process(self):
        """ 
        Process which will be executed each second. It check if there are some data in the serial port and get it 
        if apply.
        """
        print('Bytes available: ' + str(self.serial_conn.inWaiting()))
        if self.serial_conn.inWaiting() > 0:
            text = 'Bytes available: ' + str(self.serial_conn.inWaiting())
            self.txt_write.append(text)
            # received_data = self.serial_conn.read(self.serial_conn.inWaiting())
            received_data = self.read_bytes('all')
            self.txt_write.append(received_data.decode())
        else:
            print('Nothing to print...')


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    form = MainClass()
    form.show()
    sys.exit(app.exec_())
