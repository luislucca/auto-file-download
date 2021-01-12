import imaplib, email

"""
Ref for IMAP4_SSL conn:
https://www.thepythoncode.com/article/reading-emails-in-python

Prerequisite for the connection:
https://myaccount.google.com/lesssecureapps?pli=1

Ref for prerequisite:
https://stackoverflow.com/questions/33119667/reading-gmail-is-failing-with-imap
"""

# Defines access variables: user, password and mail url

user = 'tester.lucca@gmail.com'
password = '019283vulp'
imap_url = 'imap.gmail.com'

# Mail connection and inbox selection
# IMAP4_SSL is needed for encrypted auth
mail = imaplib.IMAP4_SSL(imap_url)
mail.login(user, password)

# Query the email inbox
status, messages = mail.select("INBOX")

# number of emails in the inbox
messages = int(messages[0])

print(messages)