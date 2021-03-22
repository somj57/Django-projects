from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('feedback/', include('feedback.urls')),
    path('portfolio/', include('portfolio.urls')),
    path('admin/', admin.site.urls),
]