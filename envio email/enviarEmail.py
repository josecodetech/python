import smtplib


def enviarEmail(remitente, destinatario, mensaje):
    usuario = remitente
    password = 'tuclave'
    try:
        conexion = smtplib.SMTP('smtp.gmail.com', 587)
        conexion.starttls()
        conexion.login(usuario, password)
        print("Login correcto")
        conexion.sendmail(remitente, destinatario, mensaje)
        print("Email enviado correctamente")
        conexion.quit()
    except smtplib.SMTPAuthenticationError:
        print("Error de autenticacion")


if __name__ == "__main__":
    enviar("usuario@gmail.com", "destinatario@gmail.com",
           "Hola, prueba desde Python")
