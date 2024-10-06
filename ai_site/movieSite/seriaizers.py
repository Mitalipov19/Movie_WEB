from rest_framework import serializers
from .models import *
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['username', 'email', 'password',  'first_name', 'last_name',
                  'age', 'phone_number', 'status']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = Profile.objects.create_user(**validated_data)
        return user

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user': {
                'username': instance.username,
                'email': instance.email,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Неверные учетные данные")


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


class ProfileSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name']


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['country_name']


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = '__all__'


class DirectorSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ['director_name']


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = '__all__'


class ActorSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ['actor_name']


class JanreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Janre
        fields = ['janre_name']


class MovieLanguagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieLanguages
        fields = ['language', 'video']


class MomentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Moments
        fields = ['movie_moments']


class CommentSerializer(serializers.ModelSerializer):
    user = ProfileSimpleSerializer()
    created_date = serializers.DateTimeField(format='%d-%m-%Y %H:%M')

    class Meta:
        model = Comment
        fields = ['user', 'stars', 'parent', 'text', 'created_date']


class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = '__all__'


class MovieListHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['movie_name']


class HistorySerializer(serializers.ModelSerializer):
    user = ProfileSimpleSerializer()
    movie = MovieListHistorySerializer()
    viewed_at = serializers.DateTimeField(format('%d-%m-%Y %H:%M'))

    class Meta:
        model = History
        fields = ['user', 'movie', 'viewed_at']


class MovieListSerializer(serializers.ModelSerializer):
    country = CountrySerializer()
    janre = JanreSerializer(many=True, read_only=True)
    year = serializers.DateField(format='%d-%m-%Y')

    class Meta:
        model = Movie
        fields = ['movie_name', 'year', 'country', 'janre', 'movie_time', 'movie_image', 'status_movie']


class MovieDetailSerializer(serializers.ModelSerializer):
    country = CountrySerializer()
    janre = JanreSerializer(many=True, read_only=True)
    director = DirectorSimpleSerializer(many=True, read_only=True)
    actor = ActorSimpleSerializer(many=True, read_only=True)
    moments = MomentsSerializer(many=True, read_only=True)
    comment = CommentSerializer(many=True, read_only=True)
    language = MovieLanguagesSerializer(many=True, read_only=True)
    average_rating = serializers.SerializerMethodField()
    year = serializers.DateField(format='%d-%m-%Y')

    class Meta:
        model = Movie
        fields = ['movie_name', 'year', 'country', 'director', 'actor', 'janre', 'types', 'movie_time',
                  'movie_trailer', 'movie_image', 'movie', 'status_movie', 'average_rating', 'moments',
                  'description', 'language', 'comment',]

    def get_average_rating(self, obj):
        return obj.get_average_rating()


class FavoriteMovieSerializer(serializers.ModelSerializer):
    cart = FavoriteSerializer()
    movie = MovieListSerializer()
    class Meta:
        model = FavoriteMovie
        fields = ['cart', 'movie']