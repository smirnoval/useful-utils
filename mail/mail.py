"""Simple email lib."""

import smtplib
from email.mime.text import MIMEText
from queue import Queue
import threading
import time


class MailBox(threading.Thread):
    """MailBox class responsible for connecting to the server and sending messages.

    :param server: smtp server domain or ip.
    :param port: smtp server port.
    :param auth=(USERNAME, PASSWORD): used to login to the smtp server.
    :param enable_ssl: Use Secure Socket Layer to communicate with the server.
    :param enable_tls: Use Transport layer security.
    """

    _MAX_QUEUE = 100

    def __init__(self, server, port, auth=("", "")):
        super().__init__()
        self.server = server
        self.port = port
        self.username = auth[0]
        self.password = auth[1]
        self.smtp = smtplib.SMTP(server, port)

        self.waiting_queue = Queue(self._MAX_QUEUE)
        self.stop = False
        self._connect()

    def send_mail(self, mail, async=False, callback=None):
        """send email.

        @async: the mail will be send in the background, when finised, callback will be called.
        """
        if not isinstance(mail, Email):
            raise Exception("Mail Format Error")
        mail.callback = callback

        if async:
            self.waiting_queue.put(mail)
            return True

        return self._send_mail(mail)

    def run(self, *args, **kwargs):
        """Background Email Service, send email in the queue.

        Called by threading.Thread
        """
        while True:
            if self.stop:
                try:
                    self.smtp.quit()
                except:
                    pass
                break
            if self.waiting_queue.empty():
                time.sleep(4)
                continue
            mail = self.waiting_queue.get(False)
            self._send_mail(mail)

    def quit(self, timeout=10):
        self.stop = True
        self.join(timeout)

    def _send_mail(self, mail):
        msg = MIMEText(mail.content, mail.content_type)
        msg["Subject"] = mail.subject
        msg["From"] = mail.sender
        msg["To"] = ",".join(mail.receivers)

        print(msg.as_string())

        # check if smtp is still alive
        is_alive = True
        try:
            status = self.smtp.noop()[0]
            is_alive = True if status == 250 else False
        except self.smtp.SMTPServerDisconnected:
            is_alive = False
        except Exception:
            is_alive = False

        if not is_alive:
            self._connect()

        try:
            self.smtp.sendmail(msg["From"], msg["To"], msg.as_string())
        except (smtplib.SMTPSenderRefused, smtplib.SMTPRecipientsRefused):
            return False
        except Exception:
            return False

        if mail.callback:
            mail.callback("success", mail)
        return True

    def _connect(self):
        self.smtp.starttls()

        if self.username:
            self.smtp.login(self.username, self.password)

        self.smtp.ehlo()


class Email(object):
    """
    MailBox.

    :param sender: sender's email addr, formated as "user@domain.com"
    :param receivers: a list of receivers, each is formated the same as sender
    :param content: the content of the mail
    :param content_type: html or plain
    """

    def __init__(self, sender="", receivers=[], subject="", content="",
                 content_type="plain"):
        self.sender = sender
        self.receivers = receivers
        self.subject = subject
        self.content = content
        self.content_type = content_type
