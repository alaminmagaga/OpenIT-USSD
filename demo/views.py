from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

# Create your views here.


@csrf_exempt
def index(request):
    if request.method == 'POST':
        session_id = request.POST.get('sessionId')
        service_code = request.POST.get('serviceCode')
        phone_number = request.POST.get('phoneNumber')
        text = request.POST.get('text')

        response = ""

        if text == "":
            response = "CON Welcome to OpenIT   \n"
            response += "1. Project \n"
            response += "2. Monitor Projects \n"
            response += "3. language \n"
            response += "4. about \n"

        elif text=="1":
            response = "CON Select State \n"
            response += "1. Plateau \n"
            response += "2. Ekiti \n"
            response += "3. Edo \n"
           
            
         elif text=="1*1":
            response = "CON Select MDA \n"
            response += "1. Ministry of Works \n"
            response += "2. Ministry of Health \n"
            response += "3. Ministry of Water Resources and Energy \n"
            response += "4. Ministry of Tourism, Culture and Hospitality \n"
            
            
            
        elif text == "1*1*1":
            response = "CON Contractor \n"
            response += "1.  P.W Nig Limited \n"
            response += "2.  Fundation solid Nigeria \n"
            response += "3.  Rick Rock Construction Nig. Ltd. \n"
            response += "3.  EEC. International Co. Ltd \n"

       

      
        elif text == "1*1*2":     #one off
            response = "END thank you for your one-off daily football news plan \n"  
  
     
        elif text == "1*2*1":
            response = "END thank you for subscribing to our weekly football news plan \n"

        elif text == "1*2*2":
            response = "END thank you for your one-off weekly football news plan \n"    
    
        elif text == "1*3":
            response = "CON You will be charged N25 for our monthly football news plan \n"
            response += "1. Auto-Renew \n"
            response += "2. One-off Purchase \n"
         
        elif text == "1*3*1":
            response = "END thank you for subscribing to our monthly football news plan \n"
    
        elif text == "1*3*2":
            response = "END thank you for your one-off monthly football news plan \n"


        return HttpResponse(response)

