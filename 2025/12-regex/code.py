# import re 
# strng = "Bill has an email address bill@email.com"
# lst = re.findall('\S+@\S+', strng)
# print(''.join(lst))

# ########################################

# From the given string, use regex to find and print all emails with a yahoo domain and a three letter first name.

import re 
strng = '''Bill has an email address Bill@email.com
           Suzanne has an email address Suzanne@other.org
           Joe has an email address Joe@yahoo.com
           Jill has an email address Jill@yahoo.com
           Jim has an email address Jim@yahoo.com
           Dre has an email address Dre@google.com
           Han has an email address Han@yahoo.com
           Jen has an email address Jennifer@yahoo.com
           '''

pattern = r'\b[A-Za-z]{3}@yahoo\.com\b'

matches = re.findall(pattern, strng)

for match in matches:
    print(match)

########################################



########################################



########################################