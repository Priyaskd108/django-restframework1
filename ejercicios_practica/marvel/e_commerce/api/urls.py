from django.urls import path
from e_commerce.api.views import *
from e_commerce.api.marvel_views import *

urlpatterns = [
    path('comic-list/', comic_list_api_view),
    path('comic-retrieve/', comic_retrieve_api_view),
    path('comic-create/', comic_create_api_view),
    path('get/', vista_api_get),
    path('post/', vista_api_post),
    path('get_post/', vista_api_get_post),
    path('get_comics/', get_comics),
    path('purchased_item/', purchased_item)
]
