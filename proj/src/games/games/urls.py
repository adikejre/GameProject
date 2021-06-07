"""games URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from my_games.views import CustomLoginView,game_pg,RegisteringPg,snakegame,snake_score,list_of_scores,flappybrd,flappy_score,dinogame,dino_score,ponggame,pong_score,tttgame,ttt_score,leaderb
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('admin/', admin.site.urls),
    #path('',home_pg),
    #path('home',home_pg),
    path('',CustomLoginView.as_view() ,name='loginpg'),#TODO
    #path('login',CustomLoginView.as_view() ),
    path('logout',LogoutView.as_view(next_page='loginpg') ,name='logout'),
    path('allgames/',game_pg ,name='game_list'),#

    path('leaderboard/',leaderb,name="leader_board"),

    path('register/',RegisteringPg.as_view(),name='register'),
    path('snake/',snakegame,name='mysnake_game'),

    path('flappy/',flappybrd,name='flappygame'),

    path('dino/',dinogame,name='dinogame'),

    path('pong/',ponggame,name='ponggame'),

    path('ttt/',tttgame,name='tttgame'),

    path('savescore/',snake_score),
    path('savescoreflappy/',flappy_score),
    path('savescoredino/',dino_score),
    path('savescorepong/',pong_score),
    path('savescorettt/',ttt_score),

    path('my-scores/',list_of_scores,name='list_of_scores'),
]
