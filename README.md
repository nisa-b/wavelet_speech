# Wavelet Tabanlı Konuşma Sınıflandırması

Bu depo, insan sesinden alınan **"Evet"** ve **"Hayır"** kelimelerini sınıflandırmak için Ayrık Dalgacık Dönüşümü (DWT) ile özellik çıkarılması ve bu özelliklerin Yapay Sinir Ağı (YSA) kullanılarak analiz edilmesine odaklanmıştır.

## Proje Amacı

Projenin temel amacı, DWT'nin konuşma sinyali analizindeki etkinliğini göstererek, basit bir komut setini (Evet/Hayır) yüksek doğrulukla sınıflandırabilen hafif bir model geliştirmektir.

## Özellik Çıkarma: Ayrık Dalgacık Dönüşümü (DWT)

Konuşma sinyallerinden özellik çıkarmak için DWT kullanılmıştır.

* **Detay Katsayıları:** DWT ile elde edilen detay katsayıları, konuşma sinyali içerisindeki ani değişimleri ve fonem geçişlerini temsil eder. Bu katsayılar, kelimeler arasındaki ayırt edici zamansal–frekansal farkların ortaya çıkarılmasını sağlayarak, sınıflandırma modelinin performansını artırır.

## Dosya Yapısı

| Dosya/Klasör | Açıklama |
| :--- | :--- |
| `data/` | Modelin eğitilmesi ve test edilmesi için kullanılan "Evet" ve "Hayır" kelimelerine ait ham ses dosyalarının (genellikle `.wav`) bulunduğu dizindir. |
| `features.py` | Ham ses verilerini okur, sinyallere DWT uygular ve sınıflandırma modeli için kullanılacak sayısal özellik vektörlerini (özellikle detay katsayılarını) oluşturur. |
| `train.py` | `features.py` tarafından çıkarılan DWT özelliklerini kullanarak Yapay Sinir Ağı (YSA) modelini tanımlar, derler ve eğitir. Eğitilen model çıktısı bu betik ile kaydedilir. |
| `record_audio.py` | Kullanıcının mikrofonu üzerinden yeni ses örnekleri kaydetmek ve `data/` klasörüne eklemek için kullanılan yardımcı betiktir. |
| `utils.py` | Ses verilerini yükleme, ön işleme, sinyalleri normalleştirme ve veri kümesini eğitim/test alt kümelerine ayırma gibi genel amaçlı yardımcı fonksiyonları içerir. |
| `visualize_signals.py` | Ham sinyal formunu, DWT uygulanmış sinyalleri ve katsayıları görselleştirerek veri analizi ve dönüşüm etkisini incelemeye yarar. |
| `vis2.py` | Alternatif veya ek görselleştirme işlevlerini içerir. (Örn: Modelin eğitim geçmişini veya başarı metriklerini görselleştirmek için kullanılabilir.) |

## Kullanım (Varsayımsal Adımlar)

1.  **Veri Toplama:** Projenin gerektirdiği ses verilerini (`data/` klasörüne) `record_audio.py` betiğini kullanarak veya harici bir kaynaktan toplayınız.
2.  **Özellik Çıkarma:** DWT tabanlı özellikleri oluşturmak için `features.py` dosyasını çalıştırınız.
3.  **Model Eğitimi:** Oluşturulan özellik veri seti üzerinde YSA modelini eğitmek için `train.py` dosyasını çalıştırınız.
4.  **Test ve Görselleştirme:** Modelin performansını test edebilir veya sinyalleri incelemek için `visualize_signals.py` betiğini kullanabilirsiniz.


