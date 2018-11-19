from authSMTP.authsmtp import SendEmail

messaggio = SendEmail()
messaggio.sE_user = "alexandro@ghettini.it"
messaggio.sE_pass = "alexandro1974!"  # ovviamente salvata oscurata
messaggio.sE_host = "mailserver.ghettini.it"
messaggio.sE_port = 587
messaggio.sE_src_add = "alexandro@ghettini.it"
# messaggio.sE_dst_add = "alexandro.ghettini@consultant.aruba.it"
messaggio.sE_dst_add = "lamasquerade@gmail.com"
messaggio.sE_soggetto = "soggetto email"
messaggio.sE_messaggio = "corpo della mail"
print(messaggio.send())
