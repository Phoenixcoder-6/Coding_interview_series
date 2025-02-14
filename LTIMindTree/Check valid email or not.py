#check a valid email or not
class Email:
  @staticmethod
  def create_email(name,number):
    domain="@gmail.com"
    email= name+str(number)+domain
    return email

  @staticmethod
  def check_email(email):
    name_part=email[:5]
    number_part= email[5:8]
    if name_part.isalpha() and number_part.isdigit():
      return True
    else:
      return False
  

e1=Email()
gen_email=e1.create_email("anki",2025)
print(gen_email)
print(e1.check_email(gen_email))
