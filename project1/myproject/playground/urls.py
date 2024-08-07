from django.urls import path
from . import views

# URLconf
urlpatterns=[
    path('hello/',views.say_hello),
    path('render_html/',views.renderhtmlfile),
    
    path('', views.members, name='members'),
    path('details/<int:id>', views.details, name='details'),
]