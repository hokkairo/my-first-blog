
from django.urls import path
from . import views
'''
これはDjangoのpath関数と、
blogアプリの全てのvievsをインポートするという意味です。
'''

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]
'''
このパターンは誰かがあなたのWebサイトの'http://127.0.0.1:8000/'という
アドレスにアクセスしてきたらviews.post_list が正しい行き先だということをDjangoに伝えます。
'''
