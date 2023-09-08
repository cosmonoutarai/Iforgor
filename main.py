# kamus bahasa Gaul

meme_dict = { 
            "CRINGE": "Sesuatu yang sangat aneh atau memalukan",
            "LOL": "Tanggapan umu terhadap sesuatu yang lucu",
            "CREEPY": "Sesuatu yang disgusting",
            "ROFL": 'tanggapan terhadap lelucon'
            }

word = input("Ketik kata yang tidak Kamu mengerti (gunakan huruf kapital semua!): ")

if word in meme_dict.keys():
    # Apa yang harus kita lakukan jika kata itu ditemukan?
    print(meme_dict[word])
else:
    # Apa yang harus kita lakukan jika kata itu tidak ditemukan?
    print('KATA TIDAK DITEMUKAN!')
