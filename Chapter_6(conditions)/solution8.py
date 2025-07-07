# Check if a password is "Weak", "Medium", or "Strong". Criteria: < 6 chars (Weak), 6-10 chars (Medium), >10 chars (Strong).

password = "Secure3P@ss"
# password_lenght = len(password) #nhi to hum len(password) ke jagah password_lenght laga ek check kar sakte the phale he uski lenght calculate karke 

if len(password) < 6:  # yaha humne len use kiya h kyuki uper uske criteria me bola h 6 char use check karne ke liye len use hua h
    strenght = "Weak"
elif len(password) < 11:
    strenght = "Medium"
else:
    strenght = "Strong"
    
print(strenght)