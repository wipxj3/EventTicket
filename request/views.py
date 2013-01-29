# Create your views here.
from django.http import HttpResponse
import qr

def request(request):
    params = request.GET.get('params', '')
    qrEncoder = qr.QRencode()
    data = params.split(',')
    info, qrHash = qrEncoder.getData(int(data[0]),int(data[1]),int(data[2]),int(data[3]),int(data[4]))
    qrImage = qrEncoder.generate(qrHash)
    qrEncoder.saveToDB(str(qrImage), str(info), str(qrHash))
    qrStorage = 'http://localhost/static/qrs/'
    f = qrStorage + qrImage + '.png'
    response = '<html>' \
               '<strong><em>Your ticket</em></strong><br />' \
               '<img src="'+ f +'" alt="image not loaded"/>' \
               '</html>'
    return  HttpResponse(response)