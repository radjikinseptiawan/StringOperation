import re

class RegistrationValidation:
    def __init__(self,fullname,phone_number,email_address):
        self.fullname = fullname
        self.phone_number = phone_number
        self.email_address = email_address
        self.errors = []
    def validate_name(self):
        if not all(char.isalpha() or char.isspace() for char in self.fullname):
            self.errors.append("Nama lengkap harus berisi huruf alphabet")
    
    def validate_phone(self):
        if not self.phone_number.isdigit():
            self.errors.append("Nomor telepon harus berisi angka!")
    
    def validate_email(self):
        if not re.match(r"^[\w\.-]+@[\w\.-]+\.[a-zA-Z]{2,}$",self.email_address):
            self.errors.append('Email harus berisi karakter @ dan karakter . di dalam nya')
   
    def validate(self):
        self.validate_name()
        self.validate_phone()
        self.validate_email()

        if self.errors:
            for error in self.errors:
                print(error)
        else:
            print("Data pendaftaran valid")
