import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#DEF  DE ENVIAR E-MAIL
def Enviar_Email(email_destinatario):
    try:
        msg = MIMEMultipart("alternative")
        msg["Subject"] = u'Mandar e-mail com caracteres especiais e sem cair em Spam!' #Titulozinho
        msg.attach( MIMEText(u'Olá,\n\nEsta é a mensagem do corpo do e-mail!\n\n\n\nAtt,\nLuis Gustavo Fin', "plain", "utf-8" ) ) #Corpo
        msg = msg.as_string().encode('ascii')
        TO = email_destinatario

        #Pode deixar tudo generico apartir daqui
        gmail_sender = 'seu_email@gmail.com' # favor colocar email com dominio do gmail
        gmail_passwd = 'Colocar aqui sua senha'
        server = smtplib.SMTP('smtp.gmail.com', 587) #L E M B R A R  -  de liberar a porta 587
        server.ehlo()
        server.starttls()
        server.ehlo
        server.login(gmail_sender, gmail_passwd)
        server.sendmail(gmail_sender, [TO], msg)
        print('Email enviado com sucesso para: ',TO)
        server.quit()
    except:
        print('Ocorreu um erro ao enviar e-mail para: ',TO)
#FIM  DA  DEF  DE ENVIAR E-MAIL


Enviar_Email('email_do_destinatario@email.com') # destinatário pode ser qualquer e-mail ^^
