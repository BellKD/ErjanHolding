from django.urls import path
from .import views


urlpatterns = [
    path('',views.index_view),
    path('detail/',views.estate_detail_view)

]