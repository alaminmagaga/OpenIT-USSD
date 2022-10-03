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
            response = "CON Select LGE \n"
            response += "1. Barkin Ladi \n"
            response += "2. Bassa \n"
            response += "3. Bokkos \n"
            response += "1. Jos-East \n"
            response += "2. Jos-North \n"
            response += "3. Jos-South \n"
            response += "1. Kanam \n"
            response += "2. Kanke \n"
            response += "3. Langtang North \n"
            response += "1. Langtang South \n"
          
               
        elif text=="1*1*1":
            response = "CON Select MDA \n"
            response += "1. Ministry of Works \n"
            response += "2. Ministry of Health \n"
            response += "3. Ministry of Water Resources and Energy \n"
            response += "4. Ministry of Tourism, Culture and Hospitality \n"
            
        elif text == "1*1*1*1":
            response = "CON Select Contractor \n"
            response += "2.  Fundation solid Nigeria \n"
            response += "1.  P.W Nig Limited \n"
            response += "3.  Rick Rock Construction Nig. Ltd. \n"
            response += "3.  EEC. International Co. Ltd \n"
            
        elif text == "1*1*1*: 
            response = "END Dualization of Polo Roundabout-Farin Gada Algadama-Rock Haven Alheri Road Network and Terminus-Bauchi Road at JOS/NORTH, 100 \n"  
       
    
    
        return HttpResponse(response)

