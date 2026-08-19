from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Main page with About, Services, Cars, Contact
    path('', views.home, name='home'),

    # Car booking
    path('book/<int:car_id>/', views.book_car, name='book_car'),

    # Auth
    path('signup/', views.signup_view, name='signup'),
    path('login/', auth_views.LoginView.as_view(
        template_name='cars/login.html',
        next_page='home'  # after login go to home
    ), name='login'),
    path('logout/', views.logout_view, name='logout'),
]