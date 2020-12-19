import imaplib, email

# Defines access variables: user, password and mail url

user = 'tester.lucca@gmail.com'
password = '019283vulp'
imap_url = 'imap.gmail.com'

# Mail connection and inbox selection

mail = imaplib.IMAP4(imap_url)
mail.login(user, password)
mail.list()