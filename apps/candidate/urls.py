from django.urls import path

from .views import api_candidate_list, candidate, candidate_list, vote

urlpatterns = [
    path('', candidate_list, name='candidate_list'),
    path('<int:pk>/', candidate, name='candidate_detail'),
    path('vote/<int:candidate_id>/', vote, name='vote'),
    path('api/', api_candidate_list)
]
