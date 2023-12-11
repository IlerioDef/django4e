from django.urls import path
from . import views
from django.views.generic import TemplateView

# https://docs.djangoproject.com/en/4.2/topics/http/urls/
app_name = 'solo'
urlpatterns = [
    path('', views.SoloMain.as_view(), name='all'),
    path('alternative/', TemplateView.as_view(template_name='solo/solo_app.html'), name="solo_alternative"),
    # path('main/<int:pk>/update/', views.CatUpdate.as_view(), name='cat_update'),
    # path('main/<int:pk>/delete/', views.CatDelete.as_view(), name='cat_delete'),
    # path('lookup/', views.BreedView.as_view(), name='breed_list'),
    # path('lookup/create/', views.BreedCreate.as_view(), name='breed_create'),
    # path('lookup/<int:pk>/update/', views.BreedUpdate.as_view(), name='breed_update'),
    # path('lookup/<int:pk>/delete/', views.BreedDelete.as_view(), name='breed_delete'),
]

# Note that make_ and auto_ give us uniqueness within this application
