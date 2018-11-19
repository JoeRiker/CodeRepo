from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import ssl


class SendEmail:
    def __init__(self, username="", password="", hostname="", porta=587,
                 mittente="", destinatario="", messaggio="", soggetto=""):

        # Dettagli mailserver e credenziali autenticazione
        self.sE_user = username
        self.sE_pass = password
        self.sE_host = hostname
        self.sE_port = porta
        # Dettagli messaggio da inviare
        self.sE_src_add = mittente
        self.sE_dst_add = destinatario
        self.sE_soggetto = soggetto
        self.sE_messaggio = messaggio

    def send(self):
        # Creazione messaggio da inviare
        msg = MIMEMultipart()
        msg['From'] = self.sE_src_add
        msg['To'] = self.sE_dst_add
        msg['Subject'] = self.sE_soggetto
        msg.attach(MIMEText(self.sE_messaggio, 'plain'))

        # Apertura connessione al server e invio messaggio
        try:
            context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
            server = smtplib.SMTP(self.sE_host, self.sE_port)
            server.ehlo_or_helo_if_needed()
            server.starttls(context=context)
            server.login(self.sE_user, self.sE_pass)
            server.sendmail(msg['From'], msg['To'], msg.as_string())
            server.quit()
            return "Email Inviata"
        except Exception as e:
            return "Email non inviata: ", e
            # print("Successfully sent email message to %s:" % (msg['To']))
