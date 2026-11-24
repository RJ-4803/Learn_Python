code="the verification code is: 123456. Don't share it with anyone"

fcode= code.split(":")[1].split(".")[0].strip() #splits the string to extract the code and removes any leading/trailing whitespace
print("The code is:",fcode)

offer="Get 20% off on your next purchase! Use code: SAVE20 at checkout."
if "SAVE20" in offer:
    print("The offer is valid. Use the code to get a discount.") 



quote="The only limit to our realization of tomorrow is our doubts of today."
print(quote.find("realization")) # prints the index of the first occurrence of the substring


name="Renujaan ravichandran"
