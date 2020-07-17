from gtts import gTTS
import os

myText = r"""Bilim yazarı Sam Kean, vaka raporları ve bilimsel çalışmalar ışığında sürükleyici bir beyin araştırmaları tarihi sunuyor. Sinirbilimin son dört yüzyıldaki gelişimini, insan beyninin en gizemli ve tuhaf hastalıkları üzerinden aktarırken beyin ve sinir sistemine dair bilinmeyenleri gözler önüne seriyor.

Bu kitapta, kokuların gürültü çıkarıp dokuların renkler saçtığı büyüleyici hikayeler bulacak, yarasalar gibi sesin yankılarıyla görmeyi öğrenen körlerden ilham alacaksınız. Hafızalarını kaybettikleri için sevdiklerini bile tanıyamayan insanların, farkında olmadan aslında nasıl hatırlayabildiklerinin bir tanığı da siz olacaksınız.

İnsan Beyninin Gizemi modern sinirbilimin gelişimine önayak olan kral, yamyam ve kaşiflerin yaşamlarını yeniden canlandırarak insan beynine dair binlerce benzeri arasından seçilmiş en ilgi çekici hikâyeleri paylaşıyor.

Bu kampanya, Kolektif Kitap tarafından Evrim Ağacı okurlarına sunulan fırsatlardan birisidir."""
lang = "tr"

output = gTTS(text=myText, lang=lang, slow=False)
output.save("berkcan.mp3")
os.system("start berkcan.mp3")