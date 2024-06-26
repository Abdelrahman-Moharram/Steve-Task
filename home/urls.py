from django.urls import path
from .views import index, details, update, delete

app_name = 'home'

urlpatterns = [
    path('', index, name='index'),
    path('<int:id>/edit', update, name='update'),
    path('<int:id>/delete', delete, name='delete'),
    path('<int:id>/', details, name='book'),
]
