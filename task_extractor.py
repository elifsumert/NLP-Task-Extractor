import spacy

# İngilizce NLP modelini yüklüyoruz
nlp = spacy.load("en_core_web_sm")

def gorev_cikar(text):
    doc = nlp(text)

    gorev_paketi = {
        "eylem": None,
        "zaman": None,
        "hedef": [] 
    }

    # 1. Aşama: Eylemi ve Zamanı Bul
    for token in doc:
        if token.pos_ == "VERB": 
            gorev_paketi["eylem"] = token.lemma_  
            
    for ent in doc.ents:
        if ent.label_ == "DATE":
            gorev_paketi["zaman"] = ent.text      

    # 2. Aşama: Gürültüyü Temizle ve Hedefi Bul
    for token in doc:
        # Stop word değilse, noktalama değilse ve zaten bulduğumuz eylem/zaman değilse
        if not token.is_stop and not token.is_punct and token.lemma_ != gorev_paketi["eylem"] and token.text != gorev_paketi["zaman"]:
            gorev_paketi["hedef"].append(token.lemma_)
            
    # Hedef kelimeleri yan yana birleştir
    gorev_paketi["hedef"] = " ".join(gorev_paketi["hedef"])

    return gorev_paketi

# Test Edelim
test_metni = "I will submit the database assignments today."
print(f"Orijinal Metin: {test_metni}")
print(f"Çıkarılan Görev: {gorev_cikar(test_metni)}")
  