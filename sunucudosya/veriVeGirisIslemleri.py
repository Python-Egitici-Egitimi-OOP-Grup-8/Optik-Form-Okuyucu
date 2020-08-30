import requests
import json
import os
import json
from requests.auth import HTTPBasicAuth
from time import localtime, strftime, time
import csv
import config

Giris_API = "http://sahinmansuroglu.pythonanywhere.com/restapi/login"
API_ENDPOINT="http://sahinmansuroglu.pythonanywhere.com/restapi/ogrencicevapekle"
from abc import ABC, abstractmethod

class GirisVeSunucuIslemleri(ABC):

    Giris_API = "http://sahinmansuroglu.pythonanywhere.com/restapi/login"
    API_ENDPOINT="http://sahinmansuroglu.pythonanywhere.com/restapi/ogrencicevapekle"


    kullaniciGirisBilgileri = {}
    kullaniciToken = {}

    @classmethod
    def girisVeTokenAl(cls, kullaniciAdi, parola):
        cls.kullaniciGirisBilgileri["username"] = kullaniciAdi
        cls.kullaniciGirisBilgileri["password"] = parola
        
        # print("sunucu işlemlerinden", kullaniciGirisBilgileri)
        
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        r = requests.post(url = cls.Giris_API, data=json.dumps(cls.kullaniciGirisBilgileri), headers=headers)

        # print("----------------------------")
        # print("--- "+r.text)
        # print("--- Status Code:"+str(r.status_code))
        # print("----------------------------")
        # print("r.text veri tipi ", type(r.text))

        if r.status_code == 201:
            token = json.loads(r.text)
            cls.kullaniciToken["token"] = token["token"]        
            print(cls.kullaniciToken)
            return cls.kullaniciToken
        else:
            return 0
        

    @classmethod
    def sonuclariGonder(cls, args):
        # birden faza işaretlemenin yapıldığı sonuçlar MultimarkedFiles_.csv dosyasına yazılıyor
        # aynı formlar tekrar okutulduğunda aynı dosyaya ekliyor

        # cevaplar Results_XXX.csv dosyasında saklanıyor. Buraya sadece doğru işaretlenen forms sonuçları ekleniyor.
        # aynı formalar tekrar okutulduğunda aynı değerler tekrar yazılıyor.
        # o yüzden tekrarlı verilerin temizlenmesi gerekir sunucuya gönderilmeden önce

        # işlemler bittikten sonra sonuç .csv dosyalarının bir sonraki işlem için silinmesi gerekir
        # ya da sınavkoduna göre gönderilmesi gerekir.

        # taranan formlar (.jpg) dosyaları üstüne yazılıyor

        # --- SONUÇLARIN KAYITEDİLDİĞİ CSV DOSYASI ELDE EDİLİR
        subdir = ''
        timeNowHrs = strftime("%I%p", localtime())
        paths = config.Paths(os.path.join(args['output_dir'], subdir))
        csvDosyaYolu = paths.resultDir + 'Results_' + timeNowHrs + '.csv'
        # ---

        csvDosyaYolu = "outputs/Results/Results_01AM.csv"

        print("sonuc dosya yolu verivegirisislemerinden ", csvDosyaYolu)

        """
        #csv dosyasının içindeki satırları okur json verisine çevirir
        with open(csvDosyaYolu) as csvfile:
            csvReader = csv.DictReader(csvfile)
            for rows in csvReader:
                # id = rows["SINAVKODU"]
                #data[id] = rows

                sinavSonuc = json.dumps(rows)
                #print(type(out))
                sinavSonuc = json.loads(sinavSonuc)
                #print(type(out))
                del sinavSonuc["file_id"]
                del sinavSonuc["input_path"]
                del sinavSonuc["output_path"]
                del sinavSonuc["score"]
                sinavSonuc['sinav'] = sinavSonuc.pop('SINAVKODU')
                sinavSonuc['ogrenci'] = sinavSonuc.pop('TCKIMLIKNO')
                #out = out.remove()
                # gönderme işlemi burada yapılacak
                
                veriGonder(sinavSonuc)
                print(sinavSonuc)
        """    
        with open(csvDosyaYolu) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            i=0
            data_set={ }
            line_count = 0
            for row in csv_reader:
                if (len(row)!=0 and line_count!=0):
                    i=i+1
                    print(str(i)+"\n")
                    data_set["ogrenci"]=int(row[5])
                    data_set["sinav"]=int(row[4])
                                
                    for j in range(6,56):
                        if row[j]!="":
                            data_set["C"+str(j-5)]=cls.harfToSayi(row[j])
                                    
                    print(data_set) 
                    # r = requests.post(url = APICEVAPEKLE, data=json.dumps(data_set), headers=headers)
                    print("----------------------------")
                    cls.veriGonder(data_set)
                    # if r.status_code==201:
                    #     print(str(data_set["ogrenci"]) +" nolu ogrencinin "+str(data_set["sinav"])+" nolu sınav cevapları sunucuya gönderilmiştir...")
                    # else:
                    #     print("--- "+r.text)
                    #     print("--- Status Code:"+str(r.status_code))
                    # print("----------------------------")
    
                data_set={}   
                line_count +=1    
                
        # okunan csv dosyasını json dosyasına çevirir

        # jsonDosyaYolu = "jsonDosyalari\\" + str(id) + ".json"

        # with open(jsonDosyaYolu, 'w') as jsonFile:
        #     jsonFile.write(json.dumps(data, indent=4))

    @classmethod
    def harfToSayi(cls, harf):
        if harf=='A':
            return 1
        if harf=='B':
            return 2
        if harf=='C':
            return 3
        if harf=='D':
            return 4
        if harf=='E':
            return 5

    """
    # BU FONKSİYONA GEREK KALMADI
    def sonucDosyasiBul():
        # dir_path = os.path.dirname(os.path.realpath(__file__))
        dir_path = os.path.normpath(os.path.join(__file__, '..', '..'))

        # Dosya adının sınava göre özelleştirilmesi gerekmektedir.
        filename = "Results_06PM.csv"

        # Okunan formların sonuçlarının saklandığı csv dosyası
        csvDosyaYolu = ""

        print("dosyanın arandığı yol ", dir_path)

        # sonuç dosyasını yani oluşturulan csv bulmak için
        # csv dosyasının adını sınav koduna göre değiştirmek gerekiyor
        # csv dosyasının adını oluşturulduğu yerden almak gerekiyor
        for root, dirs, files in os.walk(dir_path): 
            for file in files:  
        
                # change the extension from '.mp3' to  
                # the one of your choice. 
                # if file.endswith('.csv'): 
                #     print(root+'/'+str(file))

                if file.endswith(filename):
                    csvDosyaYolu = root + '\\' + file
                    print(csvDosyaYolu)

        return csvDosyaYolu
    """
    
    @classmethod
    def veriGonder(cls, data):
        
        # data = {        
        #     "C1": 1,
        #     "C2": 2,
        #     "C3": 5,
        
        #     "C5": 5,
        
        #     "ogrenci": 25,
        #     "sinav": 41,
        # }

        headers = {'Content-type': 'application/json','Authorization': 'Token ' + cls.kullaniciToken["token"]}
        r = requests.post(url = cls.API_ENDPOINT, data=json.dumps(data), headers=headers)

        print("----------------------------")
        print("--- "+r.text)
        print("--- Status Code:"+str(r.status_code))
        print("----------------------------")