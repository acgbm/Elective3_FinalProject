from django.http import JsonResponse
from .utils import rate_limit

@rate_limit(max_requests=5, timeframe=60)  # 5 requests per 60 seconds per IP
def limited_view(request):
    return JsonResponse({"message": "You are within the request limit."})
