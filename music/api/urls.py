# urls.py
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views


from django.urls import path
from api.views import RegistrationView, LoginView, LogoutView, MusicGenreListCreateView, PaymentConfirmationView, VerifyQuestionsView

urlpatterns = [
    path('register/', RegistrationView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('genres/', MusicGenreListCreateView.as_view(), name='music_genres'),
    path('quiz/', VerifyQuestionsView.as_view(), name='music_genres'),
    path('payment/confirm/', PaymentConfirmationView.as_view(), name='payment_confirmation'),
]

