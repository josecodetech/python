from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
c=canvas.Canvas("archivoPdf.pdf")
#ancho de linea
c.setLineWidth(.3)
#fuente y tamaño
c.setFont('Helvetica',14)
#dibuja texto en pos X e Y por puntos, 1pt = 1/72 pulgadas
c.drawString(120,760,"Hola en pdf!")
#pos x1 y1 x2 y2
c.line(120,700,590,747)
#circulo damos x y radio stroke y relleno
c.circle(120,720,20,1,1)
c.save()
    
