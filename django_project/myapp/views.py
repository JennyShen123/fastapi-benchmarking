from django.http import JsonResponse
import asyncio
import time


# Asynchronous root view
async def root(request):
    return JsonResponse({"message": "Hello World"})


# Synchronous sleep view (blocking)
def sync_sleep(request):
    time.sleep(1)
    return JsonResponse({"message": "sync, but run in thread pool"})


# Asynchronous sleep using asyncio (non-blocking)
async def async_sleep(request):
    await asyncio.sleep(1)
    return JsonResponse({"message": "async mode sleep"})


# Asynchronous view that incorrectly uses synchronous sleep (blocking)
async def async_slowest(request):
    time.sleep(1)  # This is a bad practice in async views
    return JsonResponse({"message": "async mode but use sync sleep"})


# Asynchronous sleep executed in a thread pool (non-blocking)
async def async_sleep_in_thread(request):
    loop = asyncio.get_running_loop()
    await loop.run_in_executor(None, time.sleep, 1)
    return JsonResponse({"message": "sleep run in thread pool"})
