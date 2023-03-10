from dotenv import load_dotenv
from os import environ
load_dotenv()

parolumuz = environ.get("password","Yoxdur")

key = environ.get("api_key")

if parolumuz == "Yoxdur": print(".env faylindaki deyisenlere bax")
else : print(parolumuz)

print(key)