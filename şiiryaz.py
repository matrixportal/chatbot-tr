import random

kelime_listeleri = {
    "sen": {
        "sıfatlar": ["güzel", "tutkulu", "sevimli", "şefkatli","anlayışlı", "duyarlı","cennetten gelmiş","muhteşem", "hoş","nadide","ninni gibi","saf","samimi"," fedakâr","sadık","merhametli","kutsal","candan"," iyi","korumacı","ilgili","sıcacık","sevecen","yumuşak","nazik"," yakın","özverili","canlı" "düşünceli", "hassas"," narin"," nezaketli"," muhabetli","esirgenmeyen","terbiyeli","aklı başında"],
        "isimler": ["melek", "bebek", "kelebek", "güneş", "yol", "dünya", "umut", "gül", "deniz", "bahar","nehir","orman","güvercin","bulut","rüzgar","kum","dalga","kaya","dağ","çiçek", "ağaç", "kuş","karınca", "arı","kelebek","kurbağa","yıldız","gece","gün","anne","baba","kardeş","dost","sevgi","özgürlük","mutluluk","huzur","keyif","neşe","coşku","heyecan","merak","şaşkınlık","korku","endişe","ümit","sabır","cesaret","adil"," iyilik","yardımseverlik","anlayış", "hoşgörü", "mütevazılık","alçakgönüllülük","cömertlik","misafirperverlik","centilmenlik","zarafet","kibarlık","nezaket", "şans", "kader"],
        "fiiller": ["varsın", "istesen", "olursun", "dans ederiz", "yürürüz", "gülümserim", "severim", "düşünürüm", "yaşarım", "aşarım"],
    },
    "aşk": {
        "sıfatlar": ["sıcak", "tutkulu", "dolu", "heyecanlı", "romantik", "sonsuz", "güzel", "kutsal", "pırıl pırıl" , "etkileyici",  "ufuksuz", "çılgın", "katıksız", "yumuşak", "dipdiri", "taze", "hür","etkileyici", "saf", "muhteşem", "kıskandırıcı", "tatlı", "ödüllendirici","beraberce", "zengin", "şaşkın", "ebedi", "samimi", "bembeyaz", "tanrısal", "berrak", "yumuşacık"],
        "isimler": ["canım", "balım", "sevgilim", "aşkım", "kalbim", "ruhum", "yarınlarım", "özlem" "düş", "tutku", "isteğim", "sevgili", "sarhoşluk", "cepteki şeker", "sırdaş", "hülyam", "kaderim", "sırdaşım","aklım", "delirirsem", "anım", "hayalim", "ipoteğim", "sıcak bir yuva", "öpücüğüm", "hayal", "kurbanım", "yükselişlerim", "sevinç"],
        "fiiller": ["katabilirsin", "atılabilirsin", "yaşatırım", "sevgiye doyururum", "durmaksızın özlerim", "seni düşünürüm", "senin için yaşarım", "yakarım", "yakınlaşırız", "birleşiriz", "vefa dolu kılabilirim", "ödüllendirebilirim", "yakıp kavurabilirim", "yanıp kavurabiliriz", "gizlice koklayabilirim", "aşkımıza tat katabiliriz", "kandırılabilirim", "sarmaş dolaş olabiliriz", "tüm geceleri bize adayabiliriz"],
    },
    "umut": {
        "sıfatlar": ["masmavi", "adil", "afili", "bahtiyar", "üzgün", "ballı", "sessiz", "bambaşka", "barışık", "barışçıl", "cıvıltılı", "cazibeli", "ceylan bakışlı", "güzel", "çikolatalı", "çilekli", "çiçekli", "çırılçıplak", "çıtı pıtı", "dalgalı"],
        "isimler": ["umut", "düşünce", "pırıltı", "yaprak", "çiçek", "gökyüzü", "deniz", "bahar", "dost", "güneş", "bulut", "bulutlar", "sema", "doğa", "ay çiçeği", "kumsal", "sahil", "deniz kabukları", "boncuk"],
        "fiiller": ["ummarım", "umuyorum", "ümit ediyorum", "ümit ederim", "hayal ediyorum", "hayalini kurarım", "hayal eder misin",  "mutllulukla dans ederiz", "koşar gelirim", "el ele tutuşuruz", "sevgiyle dolarız", "gözlerinde kaybolurum", "heyecanlanırım", "biz oluruz", "tekrar aşık olurum", "kalbini hızlandırırım", "gözlerimi kamaştırır güzelliğin", "seni düşünüyorum seni", "seni düşünürüm seni", "özletiyor", "seni sevdim", "sana geliyorum", "kalbim çarpıyor"],
    },
}

# Kelime seçen fonksiyon
def kelime_sec(konu, kelime_tipi):
    return random.choice(kelime_listeleri[konu][kelime_tipi])

# Dize oluştur fonksiyonu
def dize_olustur(konu):
    sıfat1, isim1, fiil1 = kelime_sec("sen", "sıfatlar"), kelime_sec("sen", "isimler"), kelime_sec("sen", "fiiller")
    sıfat2, isim2, fiil2 = kelime_sec(konu, "sıfatlar"), kelime_sec(konu, "isimler"), kelime_sec(konu, "fiiller")

    dize1 = f"{sıfat1.capitalize()} {isim1} ile {fiil1}, \n"
    dize2 = f"{sıfat2.capitalize()} {isim2} ile {fiil2},\n"
    dize3 = f"{isim1.capitalize()} ile {fiil1} {sıfat2} {isim2}.\n"
    dize4 = f"{isim2.capitalize()} {fiil2} {sıfat1} {isim1},\n"

    return dize1 + "\n" + dize2 + "\n" + dize3 + "\n" + dize4 + "\n"

# Şiir oluştur fonksiyonu
def siir_olustur():
    konular = ["aşk", "umut"]
    siir = "".join([dize_olustur(random.choice(konular)) for _ in range(4)])
    return siir

# Başlık oluşturma fonksiyonu
def baslik_olustur(siir):
    baslik_kelimesi = kelime_sec("sen", "isimler")
    baslik = f"{baslik_kelimesi.upper()} İLE BAŞLAYAN ŞİİR\n"

    return baslik + siir

# Şiir ve başlık yazdırma
siir = siir_olustur()
baslik_ve_siir = baslik_olustur(siir)
print(baslik_ve_siir)
