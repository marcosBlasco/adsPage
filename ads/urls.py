# from django.urls import path
# from . import views

# urlpatterns = [
#     path("", views.index, name="index"),
# ]

from django.urls import path, reverse_lazy
from . import views
from django.views.generic import TemplateView

app_name='ads'
urlpatterns = [
    path('', views.AdListView.as_view(), name='all'),
    path('<int:pk>/', views.AdDetailView.as_view(), name='ad_detail'),
    path('generic/', TemplateView.as_view(template_name="ads/generic.html"), name='generic'),
    path('create/', views.AdCreateView.as_view(success_url=reverse_lazy('ads:all')), name='ad_create'),
    path('<int:pk>/update/', views.AdUpdateView.as_view(success_url=reverse_lazy('ads:all')), name='ad_update'),
    path('<int:pk>/delete/', views.AdDeleteView.as_view(success_url=reverse_lazy('ads:all')), name='ad_delete'),
    path('ad_picture/<int:pk>', views.stream_file, name='ad_picture'),

    path('ad/<int:pk>/comment', views.CommentCreateView.as_view(), name='ad_comment_create'),
    path('comment/<int:pk>/delete', views.CommentDeleteView.as_view(success_url=reverse_lazy('ads:all')), name='ad_comment_delete'),
    
    path('ad/<int:pk>/favorite', views.AddFavoriteView.as_view(), name='ad_favorite'),
    path('ad/<int:pk>/unfavorite', views.DeleteFavoriteView.as_view(), name='ad_unfavorite'),
]

# We use reverse_lazy in urls.py to delay looking up the view until all the paths are defined