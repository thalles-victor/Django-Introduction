
from django.http import JsonResponse


def helloworld(request):
    data = {
        "name": 'thalles',
        "email": 'thalles@gmail.com'
    }
    return JsonResponse(data)
