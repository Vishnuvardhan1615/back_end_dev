from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from django.http import HttpResponse    

@csrf_exempt  # Disable CSRF for development/testing (not safe for production)
def api_calling(request):
    if request.method == 'GET':
        return JsonResponse({'message': 'Hello, this is a GET response!'})

    elif request.method == 'POST':
        try:
            data = json.loads(request.body)
            name = data.get('name', 'Guest')  # example: extract "name" field
            return JsonResponse({'message': f'Hello, {name}! This is a POST response!'})
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
    
    return JsonResponse({'error': 'Unsupported method'}, status=405)
