from django.http import JsonResponse
import json

def api_view(method, checked=[]):
    """decorator for checking methods of the request"""
    
    def decorator(func):
        def handler(request):
            if request.method != method:
                return JsonResponse({
                    "status": "fail",
                    "message": f"This is a {method} api."
                })

            if request.method == "GET":
                data = {k:v[0] for k,v in dict(request.GET).items()}
            elif request.method == "POST":
                data = json.loads(request.body.decode('utf-8'))

            for item in checked:
                if not item in data:
                    return JsonResponse({
                        "status": "fail",
                        "message": f"Attribute {item} need to be provided."
                    })
            return func(request, data)
        return handler
    return decorator
