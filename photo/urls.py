from django.urls import path
from . import views

app_name = 'photo'

urlpatterns = [
    path('', views.IndexView.as_view(), name = 'index'),
        # 写真投稿ページへのアクセスはviewsモジュールのCreatePhotoViewを実行
    path('post/', views.CreatePhotoView.as_view(), name='post'),
    # 投稿完了ページへのアクセスはviewsモジュールのPostSuccessViewを実行
    path('post_done/',
         views.PostSuccessView.as_view(),
         name='post_done'),
    path('photos/<int:category>',
         views.CategoryView.as_view(),
         name = 'photos_cat'
         ),
]
