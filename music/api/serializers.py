from rest_framework import serializers
from .models import Album, MusicGenre, MusicGenreQuiz, User



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'age', 'first_name', 'last_name', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        validated_data['username'] = validated_data['email']
        user = User.objects.create_user(**validated_data)
        return user


class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = MusicGenreQuiz
        fields = ['question1', 'question2', 'question3', 'answer', 'question_id']

class MusicGenreSerializer(serializers.ModelSerializer):
    quiz = QuizSerializer(many=True)

    class Meta:
        model = MusicGenre
        fields = ['id', 'name', 'artist', 'quiz']

    def create(self, validated_data):
        quiz_data = validated_data.pop('quiz')
        music_genre = MusicGenre.objects.create(**validated_data)

        for quiz_item in quiz_data:
            MusicGenreQuiz.objects.create(music_genre=music_genre, **quiz_item)

        return music_genre
