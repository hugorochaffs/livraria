from django.http import HttpResponse, JsonResponse


def teste(request):
    return HttpResponse("Olá mundo do Django.")


def teste2(request):
    return HttpResponse("Um teste 2")
