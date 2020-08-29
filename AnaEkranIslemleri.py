import sys
from PyQt5.QtWidgets import QApplication as QA, QMainWindow as QMW, QFileDialog as QFD
from PyQt5 import  uic

import main
import os
import shutil

class App(QMW):
    form_kaynak_dizin = ""
    output_dir = ""
    template = ""

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

        self.win.rdBtnSablonVarOlan.toggled.connect(lambda:self.sablonDosyaSec(self.win.rdBtnSablonVarOlan))
        self.win.rdBtnSablonOzel.toggled.connect(lambda:self.sablonDosyaSec(self.win.rdBtnSablonOzel))
        self.win.btnSablonSec.clicked.connect(self.ozelSablonSec)
        self.win.btnSablonSec.setEnabled(False)
        
        self.win.rdBtnTarayici.toggled.connect(lambda:self.kaynakSec(self.win.rdBtnTarayici))
        self.win.rdBtnFotograf.toggled.connect(lambda:self.kaynakSec(self.win.rdBtnFotograf))

        self.win.rdBtnProduction.toggled.connect(lambda:self.islemTurSec(self.win.rdBtnProduction))
        self.win.rdBtnDebug.toggled.connect(lambda:self.islemTurSec(self.win.rdBtnDebug))

        self.win.btnFormOku.clicked.connect(self.FormIsle)

        # Ekranda pencerenin gösterilmesi
        self.win.show()

    # Kullanıcı formların bulunduğu dizini seçer. Seçilen dizin içerisindeki diğer öğelerle inputs dizinine kopyalanır.
    # Eğer kullanıcının seçtiği dizin inputs dizininde varsa eski dizini siler, yeni dizini kopyalar
    def formKlasorSec(self):
        
        self.dir_path=QFD.getExistingDirectory(self,"Klasör Seçiniz",r"ornekler\taslak1\isaretliformlar")
        
        self.win.lblFormKlasor.setText(self.dir_path)

        #self.root_dir = self.dir_path

        ####
        kaynak_dizin = self.dir_path
        hedef_dizin = "inputs/"
        #extension = ".jpg"
        hedef_dizin2 = os.path.basename(self.dir_path)
        print("hedef dizin2 ", hedef_dizin2)

        self.form_kaynak_dizin = hedef_dizin + hedef_dizin2
        print("formların bulunduğu dizin", self.form_kaynak_dizin)

        dir_path = ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

        # dizini bulmak için
        for root, dirs, files in os.walk(dir_path):             
        ## dizin varsa siler
            for dir in dirs:
                if dir == hedef_dizin2:
                    print("klasör var var ##########")
                    print("klasör adı #############",dir)
                    #os.rmdir("inputs/" + dir)
                    try:
                        shutil.rmtree("inputs/" + dir)
                    except:
                        pass
        
        shutil.copytree(kaynak_dizin, hedef_dizin + hedef_dizin2)


    def ciktiKlasorSec(self):
        
        self.dir_path=QFD.getExistingDirectory(self,"Klasör Seçiniz",r"outputs\sample1\isaretliformlar")
        
        self.win.lblCiktiKlasor.setText(self.dir_path)

    def sablonDosyaSec(self, rb):
        if rb.text() == "Var olan":
            if rb.isChecked() == True:
                kaynak_template_json = r"inputs\template.json"
                hedef_template_json = self.form_kaynak_dizin
                sonuc = shutil.copy(kaynak_template_json, hedef_template_json)

                kaynak_marker_jpg = r"inputs\omr_marker.jpg"
                hedef_marker_jpg = self.form_kaynak_dizin
                sonuc = shutil.copy(kaynak_marker_jpg, hedef_marker_jpg)

                self.win.lblSablonDosya.setText("Kopyalandı")
				
        if rb.text() == "Özel":
            if rb.isChecked() == True:
                self.win.btnSablonSec.setEnabled(True)
                       
    # Seçilen özel şablonu ve marker dosyasını formların bulunduğu dizine kopyalar
    def ozelSablonSec(self):
        sablonDosyasi = QFD.getOpenFileName(self, "Şablon dosyasını seç","C:\\", "Şablon dosyaları (*.json)")
        self.win.lblSablonDosya.setText(sablonDosyasi[0])

        kaynak_template_json = sablonDosyasi[0]
        hedef_template_json = self.form_kaynak_dizin
        sonuc = shutil.copy(kaynak_template_json, hedef_template_json)

        kaynak_marker_jpg = r"inputs\omr_marker.jpg"
        hedef_marker_jpg = self.form_kaynak_dizin
        sonuc = shutil.copy(kaynak_marker_jpg, hedef_marker_jpg)

        #self.win.lblSablonDosya.setText("Kopyalandı ozelden")

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

    def FormIsle(self):
        print("formların bulunduğu dizin", self.form_kaynak_dizin)
        main.formlariIsle(self.form_kaynak_dizin)
        # self.win.lblFormOkuSonuc.setText(self.root_dir)
        # main2.process_dir(self.root_dir, '', self.template)

if __name__ == "__main__":
    app = QA(sys.argv)
    uyg = App()
    # uyg.show()
    # Uygulamanın bitişi sistemden çıkışa bağlanır.
    sys.exit(app.exec_())