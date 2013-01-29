# Create your views here.
from django.http import HttpResponse
import qr

def request(request):
    params = request.GET.get('params', '')
    qrEncoder = qr.QRencode()
    data = params.split(',')
    qrHash = data[1]
    qrImage = qrEncoder.generate(qrHash)
    qrStorage = 'http://localhost/static/qrs/'
    f = qrStorage + qrImage + '.png'
    response = '<html>' \
               '<strong><em>Your ticket</em></strong><br />' \
               '<img src="'+ f +'" alt="image not loaded"/>' \
               '</html>'
    return  HttpResponse(response)