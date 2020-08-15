# Optik Form Okuyucu
Optik formları tarayıcınızı 🖨 veya cep telefonunuzu 🤳 kullanarak tarayıp okutun. 

## Telif Hakkı
Bu proje, GNU Genel Erişim Lisansı ile dağıtılan ve kökü Udayraj Deshmukh tarafından oluşturulup https://github.com/Udayraj123 sayfasında dağıtılmakta olan projeden ayrılarak yine aynı lisanslama modeli ile dağıtılmaktadır.

### Desteklenen İşletim Sistemi
Windows işletim destekleniyor olsa da, hatadan arınmış bir deneyim için **Linux** tavsiye edilir.

#### Derleme İçin Gerekli Kütüphaneler ve Kurulumu
![imutils 0.5.2](https://img.shields.io/badge/imutils-0.5.2-blue.svg) ![matplotlib 3.0.2](https://img.shields.io/badge/matplotlib-3.0.2-blue.svg) ![pandas 0.24.0](https://img.shields.io/badge/pandas-0.24.0-blue.svg) ![numpy 1.16.0](https://img.shields.io/badge/numpy-1.16.0-blue.svg)

```bash
cd Optik-Form-Okuyucu/
python -m pip install --user -r requirements.txt
```
> **Bilgi:** Eğer bazı kütüphanelerin zaten kurulu olduğu uyarısı alırsanız, `--ignore-installed` parametresini yukarıdaki komuta ekleyip tekrar çalıştırmayı deneyin.

### Programı Çalıştırma

1. Optik formlarınızın ve şablon json dosyanızın olduğu klasörü inputs dizinine taşıyın. Örnek kullanım için aşağıdaki yöntemi kullanabilirsiniz: 
	```bash
	# Note: inputs dizininde önceden kalma dosyaları öncelikle silmelisiniz. 
	cp -r ./ornekler/taslak1 inputs/
	```
	
2. Optik okuma scriptini çalıştırabilirsiniz: 

	```bash
	# Note: main.py scripti, içinde açıklamaları da yer alan --setLayout , --autoAlign , --noCropping , --inputDir , --outputDir , --template parametreleriyle de çalıştırılabilir. AnaEkranIslemleri scripti bu parametreleri arayüz ile uygulamak içindir.
    ```

	```bash
    python main.py
    ```

