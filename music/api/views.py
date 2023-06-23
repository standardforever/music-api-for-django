from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login, logout
from .serializers import UserSerializer, MusicGenreSerializer
from .models import MusicGenre
from rest_framework.permissions import AllowAny
from rest_framework import generics



class RegistrationView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            # Additional logic for user registration
            return Response({'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(request, username=email, password=password)
        if user:
            login(request, user)
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

class LogoutView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request):
        # Get the user's token
        print(request.user)
        token = Token.objects.get(user=request.user)

        # Delete the token
        token.delete()

        # Log out the user
        logout(request)

        return Response(status=status.HTTP_200_OK)

class MusicGenreListCreateView(generics.ListCreateAPIView):
    queryset = MusicGenre.objects.all()
    serializer_class = MusicGenreSerializer
    permission_classes = [permissions.IsAuthenticated]


class VerifyQuestionsView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request, format=None):
        data = request.data
        music_genre_id = data.get('music_genre_id')
        selected_answers = data.get('selected_answers')

        try:
            music_genre = MusicGenre.objects.get(id=music_genre_id)
        except MusicGenre.DoesNotExist:
            return Response({'error': 'Music Genre not found'}, status=status.HTTP_404_NOT_FOUND)

        correct_answers = 0
        for selected_answer in selected_answers:
            question_id = selected_answer.get('question_id')
            answer = selected_answer.get('answer')
            quiz = music_genre.quiz.filter(question_id=question_id).first()
            if quiz and quiz.answer == answer:
                correct_answers += 1

        if correct_answers == 3:
            return Response({'payment_method': ['PayPal', 'Normal Transfer'], music_genre_id: music_genre_id })
        else:
            return Response({'error': 'Incorrect answers'}, status=status.HTTP_400_BAD_REQUEST)



class PaymentConfirmationView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request):
        music_id = request.data.get('music_id')
        payment_method = request.data.get('payment_method')
        payment_details = request.data.get('payment_details')
        
        # Process the payment confirmation and perform necessary actions
        # Here, you can implement your logic for handling the payment confirmation
        
        if payment_method == 'PayPal':
            # Perform actions specific to PayPal payment method
            # Example: send payment confirmation email to user, update payment status, etc.
            music = MusicGenre.objects.filter(id=music_id).values('name', 'artist').first()
            if music:
                return Response({'message': 'Payment confirmed via PayPal', 'music': music}, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Invalid music ID'}, status=status.HTTP_404_NOT_FOUND)
        
        elif payment_method == 'Normal Transfer':
            # Perform actions specific to normal transfer payment method
            # Example: update payment status, notify the user, etc.
            music = MusicGenre.objects.filter(id=music_id).values('name', 'artist').first()
            if music:
                return Response({'message': 'Payment confirmed via normal transfer', 'music': music}, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Invalid music ID'}, status=status.HTTP_404_NOT_FOUND)
        
        else:
            # Invalid payment method provided
            return Response({'error': 'Invalid payment method'}, status=status.HTTP_400_BAD_REQUEST)
