from django.urls import path
from .views import get_citations, citations_view

urlpatterns = [
    path('get_citations/', get_citations, name='get_citations'),
    path('', citations_view, name='citations_view'),  # Ensure this line exists
]
