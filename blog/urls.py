from django.urls import path

from blog.views import post_list, post_detail, post_new, \
    post_edit, post_delete, published_post, post_draft, \
    category, comment_post

urlpatterns = [
    path('', post_list, name='post_list'),
    path('post/detail/<int:post_pk>', post_detail, name='post_detail'),
    path('post/new', post_new, name='post_new'),
    path('post/edit/<int:post_id>', post_edit, name='post_edit'),
    path('post/delete/<int:post_id>', post_delete, name='post_delete'),
    path('post/publ/<int:post_id>', published_post, name='published_post'),
    path('post/draft', post_draft, name='post_draft'),
    path('post/category/<int:category_pk>', category, name='category'),
    path('post/comments/<int:post_id>', comment_post, name='comment_post'),
]