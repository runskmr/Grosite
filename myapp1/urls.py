from django.urls import path
from . import views
app_name = 'myapp1'
urlpatterns = [
    path(r'', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('redirect/', views.hmeRedirect, name='hmeRedirect'),
    # path('products/', views.products, name='products'),
    path('<int:type_no>/', views.detail, name='detail'),
    path('items/', views.items, name='items'),
    path('placeorder/', views.placeorder, name='placeorder'),
]
