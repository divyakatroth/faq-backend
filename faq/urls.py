from django.urls import path
from .views import get_faqs  # Import your view for FAQ

urlpatterns = [
    path('api/faq/', get_faqs, name='get_faqs'),
]
