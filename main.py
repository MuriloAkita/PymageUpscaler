import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from upscale_image import UpscaleImage
import design


class PymageUpscaler(QMainWindow, design.Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        self.uploadButton.clicked.connect(self.uploadFile)
        self.searchButton.clicked.connect(self.saveDirectory)
        self.submitButton.clicked.connect(self.upscaleImage)

    def uploadFile(self):
        fileName, _ = QFileDialog.getOpenFileName(
            self, 'Selecione a imagem', "", "Image Files (*.png *.jpg)")
        self.imageLineEdit.setText(fileName)
        self.file = fileName

    def saveDirectory(self):
        directoryName = QFileDialog.getExistingDirectory(self, "Salvar Em")
        self.saveInLineEdit.setText(directoryName)
        self.directory = directoryName

    def upscaleImage(self):
        upscale = UpscaleImage(self.file, self.directory)
        upscale.run()


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    pymageUpscaler = PymageUpscaler()
    pymageUpscaler.show()
    qt.exec_()
