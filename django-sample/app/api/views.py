import requests

from django.conf import settings
from django.http import JsonResponse


def api(request):
    if settings.API_HOST:
        api_url = f'http://{settings.API_HOST}/api/'
        response = requests.get(api_url)
        return JsonResponse({'message': response.json().get('message'), 'message from': api_url})
    else:
        return JsonResponse({'message': 'Does not specified `API_HOST`.'})


def database(request):
    database_url = settings.DATABASES['default']
    return JsonResponse({'database': database_url})


def message(request):
    return JsonResponse({'message': 'hello', 'API_HOST': f'{settings.API_HOST}'})
