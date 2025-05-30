import time
from django.core.cache import cache
from django.http import JsonResponse

def rate_limit(max_requests, timeframe):
    def decorator(view_func):
        def wrapper(request, *args, **kwargs):
            ip = request.META.get('REMOTE_ADDR')
            cache_key = f"rate-limit:{ip}"
            request_data = cache.get(cache_key, {'count': 0, 'start_time': time.time()})

            if time.time() - request_data['start_time'] > timeframe:
                request_data = {'count': 0, 'start_time': time.time()}

            request_data['count'] += 1
            cache.set(cache_key, request_data, timeout=timeframe)

            if request_data['count'] > max_requests:
                return JsonResponse(
                    {'detail': 'Rate limit exceeded. Try again later.'},
                    status=429
                )

            return view_func(request, *args, **kwargs)
        return wrapper
    return decorator