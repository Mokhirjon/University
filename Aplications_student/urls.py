from django.urls import path
from.views import Aplicationdelete,AplicationList,AplicationCreat,details
urlpatterns =[
    path('Aplication/',AplicationList.as_view()),
    path('create/',AplicationCreat.as_view()),
    path('delete/',Aplicationdelete.as_view()),
    path('detail/',details.as_view())
]