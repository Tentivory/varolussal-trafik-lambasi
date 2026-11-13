#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Varoluşsal Trafik Lambası
Her renk değişiminde evrenin anlamı biraz daha bulanır.
Gerçekten çalışır. Gerçekten saçma.
"""

import time
import random
import base64

# Renkler ve onlarla gelen varoluşsal krizler
RENKLER = {
    "KIRMIZI": [
        "DUR! Hayatın kırmızı ışığında durdun. Neden buradasın?",
        "Kırmızı... Kan gibi, aşk gibi, trafik cezasi gibi.",
        "Beklemek bir sanattır. Sen de bir sanatçısın artık.",
        "Bu kırmızıda geçen süre, ömründen giden süre. Düşün bunu."
    ],
    "SARI": [
        "SARI! Kararsızlık rengi. Geçeyim mi, durayım mı? Evren cevap vermiyor.",
        "Sarı, fırsatın rengidir. Ama fırsat kaçarsa ne olacak?",
        "Bu an geçici. Her şey geçici. Sen de geçicisin.",
        "Sari ışık yanıyor... Hızlan mı, yavaşla mı? Felsefe çalışıyor."
    ],
    "YESIL": [
        "YESIL! Git! Ama nereye? Aslında hiçbir yere gitmiyorsun.",
        "Yeşil ışık yandı. Özgürsün. Ama özgürlük bir illüzyon mu?",
        "Geç, geç, geç! Ama geçtiğin yol da bir başka kırmızıya çıkar.",
        "Yeşilde düşünmek yasak değil. Düşünmeye devam et."
    ]
}

# Gizli mesaj - çözmek için biraz uğraş
_gizli = "b3pndXLDvGxrIGhlciDFn2V5ZGVuIMO8c3TDvG5kw7xyIQ=="

def coz_gizli():
    try:
        return base64.b64decode(_gizli).decode('utf-8')
    except:
        return "Gizli mesaj çözülemedi. Belki de çözülmemeliydi."

def dongu():
    print("=" * 50)
    print("VAROLUŞSAL TRAFİK LAMBASI v1.0")
    print("Kırmızıda dur, sarıda şüphe et, yeşilde sorgula.")
    print("=" * 50)
    print()
    
    renk_sirasi = ["KIRMIZI", "SARI", "YESIL"]
    sayac = 0
    
    try:
        while True:
            renk = renk_sirasi[sayac % 3]
            mesaj = random.choice(RENKLER[renk])
            
            print(f"[ {renk} ] {mesaj}")
            
            # Her 7. döngüde gizli mesajı fısılda
            if sayac % 7 == 0 and sayac > 0:
                print(f"   (Fısıltı: {coz_gizli()})")
            
            print("-" * 40)
            time.sleep(random.uniform(2, 5))  # Gerçek trafik gibi rastgele bekle
            sayac += 1
            
    except KeyboardInterrupt:
        print("\n\nTrafik durdu. Sen de durdun. Hayat devam ediyor mu? Bilmiyoruz.")
        print("\n" + "="*50)
        print("DAMGA / İMZA")
        print("Tarih: 13 Kasım 2026")
        print("İsim: Kayyum Grok (Ciddî ama değil)")
        print("Not: Bu kod ciddi bir şekilde absürttür.")
        print("="*50)

if __name__ == "__main__":
    dongu()
