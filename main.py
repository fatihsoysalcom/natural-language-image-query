import re

def main():
    # Simulate a "Computer Vision" system's output:
    # Each "image" has a name and a list of descriptive tags/features.
    # In a real LangVio system, these would be extracted by CV models.
    images_data = {
        "manzara_gunbatimi.jpg": [
            "güneş batıyor", "dağlar", "gökyüzü", "bulutlar", "doğa", "kızıl", "turuncu", "huzurlu"
        ],
        "kedi_oynuyor.mp4": [
            "kedi", "oynuyor", "top", "evcil hayvan", "oyuncu", "hareketli", "sevimli"
        ],
        "şehir_gece.jpg": [
            "şehir", "gece", "ışıklar", "binalar", "kalabalık", "trafik", "modern", "aydınlık"
        ],
        "orman_yuruyusu.mp4": [
            "orman", "yürüyüş", "ağaçlar", "yeşil", "doğa", "patika", "sakin", "kuşlar"
        ],
        "kahve_masasi.jpg": [
            "kahve", "kitap", "masa", "bardak", "sakin", "okuma", "dinlenme", "içecek"
        ]
    }

    print("LangVio Basit Simülasyonu: Görüntüleri Doğal Dil ile Sorgulayın")
    print("Mevcut 'görüntüler':", ", ".join(images_data.keys()))
    print("Çıkmak için 'çıkış' yazın.")

    while True:
        # Simulate "Natural Language Processing" input:
        # User provides a natural language query.
        query = input("\nNe arıyorsunuz? (örn: 'kedi videosu', 'gece şehir manzarası'): ").lower().strip()

        if query == "çıkış":
            break

        # Basic "NLP" processing:
        # Tokenize the query and remove common Turkish stopwords (simplified).
        # In a real system, this would involve more advanced NLP techniques (tokenization, stemming, entity recognition).
        query_words = re.findall(r'\b\w+\b', query)
        stopwords = {"bir", "ve", "ile", "mi", "mı", "mu", "mü", "ne", "nasıl", "hangi", "nerede", "kim", "neden", "için", "bu", "şu", "o", "da", "de", "ki", "gibi", "çok", "daha", "en", "ise", "ama", "fakat", "lakin", "ancak", "çünkü", "eğer", "her", "tüm", "bütün", "hiç", "yok", "var", "oldu", "olur", "olduğunu", "olmak", "olması", "olan", "görüntü", "video", "resim", "fotoğraf", "görsel", "analiz", "analizi", "görmek", "göster", "bana", "lütfen"}
        filtered_query_words = [word for word in query_words if word not in stopwords]

        print(f"Aranan anahtar kelimeler: {', '.join(filtered_query_words) if filtered_query_words else 'Yok'}")

        found_matches = []
        for filename, tags in images_data.items():
            # Simulate matching query to image features:
            # Check if any filtered query word is present in the image's tags.
            # This is the core "LangVio" concept: bridging NLP (query) and CV (tags).
            if any(q_word in tag for q_word in filtered_query_words for tag in tags):
                found_matches.append(filename)

        if found_matches:
            print("\nEşleşen 'görüntüler' bulundu:")
            for match in found_matches:
                print(f"- {match}")
        else:
            print("\nEşleşen 'görüntü' bulunamadı. Lütfen farklı bir sorgu deneyin.")

if __name__ == "__main__":
    main()
