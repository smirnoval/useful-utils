from mail import MailBox, Email


def main_functionality():
    mailbox = MailBox("smtp.gmail.com", 587, auth=("gmail_login@gmail.com", "gmail_password"))
    mailbox.start()
    mail = Email("from@gmail.com", ["to@gmail.com"], subject="mail title", content="<p>Your message</p>", content_type="html")
    mailbox.send_mail(mail)


if __name__ == '__main__':
    main_functionality()
