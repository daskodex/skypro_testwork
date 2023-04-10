from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('resume/', views.PersonListView.as_view()),
    path('resume/<int:pk>/', views.PersonDetailView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)