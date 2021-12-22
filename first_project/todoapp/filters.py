from django_filters.rest_framework import FilterSet, filters

from .models import Project


class ProjectFilter(FilterSet):
    name = filters.CharFilter(lookup_expr='contains')

    class Meta:
        model = Project
        fields = ['name']
