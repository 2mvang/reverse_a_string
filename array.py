def checkGmail(email_domain):
    domain_arr = email_domain.split("@")
    return domain_arr[1] == "gmail.com"

checkGmail = checkGmail("mv@gmail.com")
print(checkGmail)
#
# for c
# # if checkGmail[1] == "gmail.com":
#     return True
