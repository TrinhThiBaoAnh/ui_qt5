from ui_interface import *
import sys
from Custom_Widgets.Widgets import *
class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.ui  = Ui_MainWindow()
        self.ui.setupUi(self)
        
        ########################################################################
        # APPLY JSON STYLESHEET
        ########################################################################
        # self = QMainWindow class
        # self.ui = Ui_MainWindow / user interface class
        loadJsonStyle(self, self.ui)
        ########################################################################
        # self.ui.pushButton_view.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_view))
        # self.ui.pushButton_config.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_config))
        # self.ui.pushButton_contact.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_contact))
        # self.ui.comboBox.currentIndexChanged.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_function))
        # self.ui.comboBox.activated.connect(self.activated)
        self.ui.toolBox_3.currentChanged.connect(self.test)
        self.show()
    def test(self):
        print("Testing:", self.ui.toolBox_3.currentIndex())
        if self.ui.toolBox_3.currentIndex() ==0:
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_view)
        elif self.ui.toolBox_3.currentIndex() ==1:
            if self.ui.button_function.clicked:
                self.ui.stackedWidget.setCurrentWidget(self.ui.page_function)
        elif self.ui.toolBox_3.currentIndex() ==2:
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_config)
        elif self.ui.toolBox_3.currentIndex() ==3:
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_contact)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())