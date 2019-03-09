from datetime import datetime
hoy=datetime.now()
print(hoy)
#Con formato
hoy=hoy.strftime('%d%m%Y')
print(hoy)