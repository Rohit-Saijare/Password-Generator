import random 
import string 
 
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!@#$%^&*()_-+=?><[]"

length = 10  
all_chars = string.ascii_letters + string.digits + string.punctuation
password = ''.join(random.sample(all_chars, length))

print("Generated password:", password)