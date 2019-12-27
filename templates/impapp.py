import imaplib
import datetime
import email

# def read_email():
email_id = "huntpiyush@gmail.com"
password = "xsho yaey qhaz akfa"
smtp_server = "imap.gmail.com"
smtp_port = 993
date = datetime.date.today()
date_today = date.strftime("%d-%b-%Y")

mail = imaplib.IMAP4_SSL(smtp_server)
mail.login(email_id, password)

mail.select('inbox')
type, data = mail.search(None, f"(ON {date_today})")
print(data)
mail_ids = data[0]
print(mail_ids)
id_list = mail_ids.split()   
first_email_id = int(id_list[0])
latest_email_id = int(id_list[-1])
print(id_list)

for i in reversed(id_list):
    typ, data = mail.fetch(i, '(RFC822)')
    for response in data:
        if isinstance(response, tuple):
            # print(response)
            msg = email.message_from_bytes(response[1])
            print(msg['Subject'])
            print(msg['From'])
            print(msg.is_multipart())
            print(msg.get_payload(decode=True))
            body = msg.get_payload(decode=True)
            for i in body:
                print(i)


# print(data)
