import pyotp
import qrcode

print(pyotp.random_base32())


chave = 'SJDLZ6QRDT6BPMU4MFEGDT75JO432TU3'
email = 'Ladislau.ball@gmail.com'
empresa = 'Minha empresa'
print(pyotp.TOTP(chave).now())
url = pyotp.totp.TOTP(chave).provisioning_uri(name=email,  issuer_name=empresa)
qrcode_imagem=qrcode.make(url)
qrcode_imagem.save('TESTE.PNG')