import sys
from PyQt5.QtWidgets import QApplication as QA, QMainWindow as QMW, QFileDialog as QFD
from PyQt5 import  uic

class App(QMW):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Formun yüklenmesi
        self.win = uic.loadUi(r"OFOAnaEkran.ui")

        #text objelerinin metinlerini sıfırla
        self.win.lblFormKlasor.setText("")
        self.win.lblCiktiKlasor.setText("")
        self.win.lblSablonDosya.setText("")
        self.win.lblKaynakSonuc.setText("")
        self.win.lblIslemSonuc.setText("")
        self.win.lblFormOkuSonuc.setText("")
        self.win.lblSunucuGonderSonuc.setText("")

        # Klasör seç düğmesine metodun bağlanması
        self.win.btnFormKlasorSec.clicked.connect(self.formKlasorSec)

        self.win.btnCiktiKlasorSec.clicked.connect(self.ciktiKlasorSec)

        self.win.btnSablonSec.clicked.connect(self.sablonDosyaSec)

        self.win.rdBtnTarayici.toggled.connect(lambda:self.kaynakSec(self.win.rdBtnTarayici))
        self.win.rdBtnFotograf.toggled.connect(lambda:self.kaynakSec(self.win.rdBtnFotograf))

        self.win.rdBtnProduction.toggled.connect(lambda:self.islemTurSec(self.win.rdBtnProduction))
        self.win.rdBtnDebug.toggled.connect(lambda:self.islemTurSec(self.win.rdBtnDebug))

        # Ekranda pencerenin gösterilmesi
        self.win.show()

    def formKlasorSec(self):
        
        self.dir_path=QFD.getExistingDirectory(self,"Klasör Seçiniz",r"ornekler\taslak1\isaretliformlar")
        
        self.win.lblFormKlasor.setText(self.dir_path)

    def ciktiKlasorSec(self):
        
        self.dir_path=QFD.getExistingDirectory(self,"Klasör Seçiniz",r"outputs\sample1\isaretliformlar")
        
        self.win.lblCiktiKlasor.setText(self.dir_path)

    def sablonDosyaSec(self):
        sablonDosyasi = QFD.getOpenFileName(self, "Şablon dosyasını seç",r"ornekler\taslak1", "Şablon dosyaları (*.json)")
        self.win.lblSablonDosya.setText(sablonDosyasi[0])

    def kaynakSec(self, rb):
        if rb.text() == "Tarayıcıdan alındı":
            if rb.isChecked() == True:
                self.win.lblKaynakSonuc.setText("Tarayıcı")
				
        if rb.text() == "Fotoğrafı çekildi.":
            if rb.isChecked() == True:
                self.win.lblKaynakSonuc.setText("Fotoğraf")
        
        # self.win.lblKaynakSonuc.setText("oldu")

    def islemTurSec(self, rb):
        if rb.text() == "Production":
            if rb.isChecked() == True:
                self.win.lblIslemSonuc.setText("Production")
				
        if rb.text() == "Debug":
            if rb.isChecked() == True:
                self.win.lblIslemSonuc.setText("Debug")
        
        # self.win.lblKaynakSonuc.setText("oldu")

if __name__ == "__main__":
    app = QA(sys.argv)
    uyg = App()
    # uyg.show()
    # Uygulamanın bitişi sistemden çıkışa bağlanır.
    sys.exit(app.exec_())