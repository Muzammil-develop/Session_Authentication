from django.urls import path
from home import views

urlpatterns = [
    path ('view' , views.Workshop_view.as_view () , name='Workshop_view'),
    path ('<int:pk>' , views.Workshop_detail.as_view () , name='Workshop_detail')
]
