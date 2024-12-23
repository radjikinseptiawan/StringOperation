from personClass import RegistrationValidation

def main():
    while True:
        nama = input("Masukkan nama lengkap : ")
        nomor = input("Masukkan nomor telepon : ")
        email = input("Masukkan email : ")

        validator = RegistrationValidation(nama,nomor,email)
        validator.validate()

main()