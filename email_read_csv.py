import imaplib
import email
import io
import pandas as pd

# login info.
email_user = 'youracount'
email_pass = 'password'

# login
mail = imaplib.IMAP4_SSL('imap.gmail.com')
mail.login(email_user, email_pass)

# select file
mail.select('Inbox')

# search mail
search_criteria = 'SUBJECT "title you need"'
result, data = mail.search(None, search_criteria)

# last one mail
email_id = data[0].split()[-1]

# get email info.
_, mail_data = mail.fetch(email_id, "(RFC822)")

# parse 解析
raw_email = mail_data[0][1]
email_message = email.message_from_bytes(raw_email)

for part in email_message.walk():
    if part.get_content_type() == 'text/csv':
        filename = part.get_filename()
        if filename == 'filename.csv':
            csv_content = part.get_payload(decode = True)
            df = pd.read_csv(io.StringIO(csv_content.decode('utf-8')))


# close
mail.close()
mail.logout()