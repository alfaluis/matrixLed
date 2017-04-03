from PyQt5 import QtGui, QtWidgets
import sys
from designerWindow import Ui_MiClassGui
from SerialCommunication import SerialCommunication
from portConfigDialog import Ui_dialog_port_conf


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
        # private attribute to check if will be used the self configuration
        self.__self_configuration = False
        self.port_selected = ''

    def __fill_dialog(self):
        '''
        Private method. It fill the opened configuration port dialog.
        This method put inside of comboBox the baud rate and port available
        :return:
        '''
        # fill baud rate combo box in
        list_baudrate = ['300', '600', '1200', '2400', '4800', '9600', '14400',
                         '19200', '28800', '38400', '57600', '115200']
        for baud in list_baudrate:
            self.dialog.ui.cmb_baudrate.addItem(baud)
        self.list_serial_ports()
        for port in self.port_list:
            self.dialog.ui.cmb_ports.addItem(port)

    def accept(self):
        print("accept here")
        self.__self_configuration = True
        self.port_selected = self.dialog.ui.cmb_ports.currentText()
        self.baud_rate = self.dialog.ui.cmb_baudrate.currentText()
        print(str(self.baud_rate) + ' - ' + self.port_selected)

    def reject(self):
        print("reject here")
        pass

    def dialog_config_port(self):
        print('opening dialog')
        self.__fill_dialog()
        self.dialog.show()

    def close_application(self):
        '''
        Function that finish the GUI (or class). It close ports opened and close GUI
        :return: Nothing
        '''
        print('close GUI')
        self.close_serial_communication()
        self.close()

    def start_serial_communication(self):
        if self.__self_configuration:
            self.open_serial_port(port_name=self.port_selected, baud_rate=self.baud_rate)
        else:
            self.open_serial_default_configuration(port_name=self.port_selected)

    def close_serial_communication(self):
        self.close_communication()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    form = MainClass()
    form.show()
    sys.exit(app.exec_())

