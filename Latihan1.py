txt = 'Hello World'

# Hitung jumlah karakter
char_result = len(txt)
print(char_result)

# Ambil karakter terakhir
char_index = txt[10]
print(char_index)

# Ambil karakter 2 sampai 4
char_2to4 = txt[1:5]
print(char_2to4)

# Hilangkan spasi pada karakter tersebut
char_pop = txt.replace(" ","")
print(char_pop)

# Ubah text menjadi huruf besar
char_upper =txt.upper()
print(char_upper)

# Ubah text menjadi huruf kecil
char_lower = txt.lower()
print(char_lower)

# Ganti karakter H dengan karakter J
char_changer = txt.replace("H","J")
print(char_changer)