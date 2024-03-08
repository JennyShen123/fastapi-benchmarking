from django.urls import path
from . import views  # Import views from the current app


urlpatterns = [
    path("", views.root),  # Accessible at /django/
    path("sync/", views.sync_sleep),  # Accessible at /django/sync
    path("async_sleep/", views.async_sleep),  # Accessible at /django/async_sleep
    path(
        "async_sleep_in_thread/", views.async_sleep_in_thread
    ),  # /django/async_sleep_in_thread
    path("async_slowest/", views.async_slowest),  # Accessible at /django/async_slowest
]
