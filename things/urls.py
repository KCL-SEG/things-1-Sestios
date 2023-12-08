from django.urls import path
from things.views import simple_page

urlpatterns = [
    path('', simple_page, name='simple_page'),
]