from django_filters import FilterSet
from .models import *

class MovieFilter(FilterSet):
    class Meta:
        model = Movie
        fields = {
            'country': ['exact'],
            'year': ['gt', 'lt'],
            'janre': ['exact'],
            'status_movie': ['exact'],
            'actor': ['exact'],
            'director': ['exact']
        }