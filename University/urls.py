from django.urls import path
from .views import UniverListAPiviews,UniverCreate,UniverDelete,UniverUpdate,UniverDetails

urlpatterns = [
    path('lists/',UniverListAPiviews.as_view()),
    path('create/',UniverCreate.as_view()),
    path('update/int:pk/',UniverUpdate.as_view()),
    path('delete/int:pk/',UniverDelete.as_view()),
    path('details/int:pk/',UniverDetails.as_view())
]