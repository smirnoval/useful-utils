# useful-utils

My utilities


## News to mail

 - Get fresh news and send to your e-mail


## Simple implementations of cryptosystems

 - RSA
 - Shamir secret sharing
 - Elgamal


## Implementations of  naive cryptosystems

 - Trisemus
 - Atbash
 - Magic square
 - Route transposition
 - Double transposition
 - Simple caesar
 - Affine system caesar
 - Key word caesar
 - Playfair
 - Polybius
 - Сoordinate polybius
 - Scytale
 - Two-square cipher

## Case converters

 - Snake case to Camel case
 - Camel case to Snake case

## Mail lib

```python
from mail import MailBox, Email

mailbox = MailBox("smtp.gmail.com", 587, auth=("gmail_login@gmail.com", "gmail_password"))
mailbox.start()
mail = Email("from@gmail.com", ["to@gmail.com"], subject="mail title", content="<p>Your message</p>", content_type="html")
mailbox.send_mail(mail)
```