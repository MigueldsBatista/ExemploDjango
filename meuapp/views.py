from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

# Create your views here.

class SightView(View):
    def get(self, request):
        
        ctx = {
            'user': 'Paulo'
            }
        return render(request, 'teste.html', ctx)
    
    def post(self, request):
        nome = request.POST.get("inputizinho")
        print(nome)
        return HttpResponse("texto")
