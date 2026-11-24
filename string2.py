code="the verification code is: 123456. Don't share it with anyone"

fcode= code.split(":")[1].split(".")[0].strip()
print("The code is:",fcode)