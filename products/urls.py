from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/',views.ProductDetailsApiview.as_view()),
    path('',views.ProductCreateApiview.as_view()),
    path('list/',views.ProductListcreateApiviews.as_view()),
    path('<int:pk>/update/',views.ProductUpdateApiview.as_view()),
    path('<int:pk>/delete/',views.ProductDeleteApiview.as_view()),
]
