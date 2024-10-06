from django.urls import path
from .views import *


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),

    path('', MovieListViewSet.as_view({'get': 'list', 'post': 'create'}), name='movie_list'),
    path('<int:pk>/', MovieDetailViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                                    'delete': 'destroy'}), name='movie_detail'),

    path('users/', ProfileViewSet.as_view({'get': 'list', 'post': 'create'}), name='user_list'),
    path('users/<int:pk>/', ProfileViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                                    'delete': 'destroy'}), name='user_detail'),

    path('country/', CountryViewSet.as_view({'get': 'list', 'post': 'create'}), name='country_list'),
    path('country/<int:pk>/', CountryViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                                    'delete': 'destroy'}), name='country_detail'),

    path('director/', DirectorViewSet.as_view({'get': 'list', 'post': 'create'}), name='director_list'),
    path('director/<int:pk>/', DirectorViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                                    'delete': 'destroy'}), name='director_detail'),

    path('actor/', ActorViewSet.as_view({'get': 'list', 'post': 'create'}), name='actor_list'),
    path('actor/<int:pk>/', ActorViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                                    'delete': 'destroy'}), name='actor_detail'),

    path('janre/', JanreViewSet.as_view({'get': 'list', 'post': 'create'}), name='janre_list'),
    path('janre<int:pk>/', JanreViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                                    'delete': 'destroy'}), name='janre_detail'),

    path('movielanguages/', MovieLanguagesViewSet.as_view({'get': 'list', 'post': 'create'}), name='movie_list'),
    path('movielanguages/<int:pk>/', MovieLanguagesViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                                    'delete': 'destroy'}), name='movie_detail'),

    path('moments/', MomentsViewSet.as_view({'get': 'list', 'post': 'create'}), name='moments_list'),
    path('moments/<int:pk>/', MomentsViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                                    'delete': 'destroy'}), name='moments_detail'),

    path('comments/', CommentViewSet.as_view({'get': 'list', 'post': 'create'}), name='comment_list'),
    path('comments/<int:pk>/', CommentViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                                    'delete': 'destroy'}), name='comment_detail'),

    path('favorite/', FavoriteViewSet.as_view({'get': 'retrieve'}), name='favorite_detail'),

    path('favoritemovie/', FavoriteMovieViewSet.as_view({'get': 'list', 'post': 'create'}), name='favoriteMovie_list'),
    path('favoritemovie/<int:pk>/', FavoriteMovieViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                                    'delete': 'destroy'}), name='favoriteMovie_detail'),

    path('history/', HistoryViewSet.as_view({'get': 'list', 'post': 'create'}), name='history_list'),
    path('history/<int:pk>/', HistoryViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                                    'delete': 'destroy'}), name='history_detail'),
]
