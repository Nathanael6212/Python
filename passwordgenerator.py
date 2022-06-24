import random
import string

characters=string.ascii_letters+string.digits+"!@#$%^&*()_="
length=16
password="".join(random.sample(characters,length))
print("your new pass is: "+ password)