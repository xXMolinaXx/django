from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse
from django.urls import reverse
from .models import Clientes

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

@require_http_methods(["POST"])
# @require_POST()
@csrf_exempt
def cliente(request,cliente_id):
    cliente = get_object_or_404(Clientes, pk=cliente_id)
    try:
        selected_client = Clientes.objects.get(id=request.POST.get('cliente_id'))
        print(selected_client)
    except Exception as e :
        # Redisplay the question voting form.
        print(e)
        return JsonResponse({"message":"error"})
    else:
        return JsonResponse({"message":"todo bien"})