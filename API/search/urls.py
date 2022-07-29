from django.urls import include, path
from.views import  SearchAPIView_keb, SearchAPIView_reb
urlpatterns = [
    path('search/keb/<str:keb_text>/', SearchAPIView_keb.as_view(), name='SearchAPIkeb'),
    path('search/reb/<str:reb_text>/', SearchAPIView_reb.as_view(), name= 'SearchAPIreb' )
]