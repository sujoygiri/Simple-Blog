from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^$',views.PostListView.as_view(),name='post_list'),
    url(r'^about/$',views.AboutView.as_view(),name='about'),
    url(r'^post/(?P<pk>\d+)$',views.PostDetailView.as_view(),name='post_detail'),
    url(r'^post/new/$',views.PostCreateView.as_view(),name='new_post'),
    url(r'^post/(?P<pk>\d+)/update/$',views.PostUpdateView.as_view(),name='update_post'),
    url(r'^post/(?P<pk>\d+)/delete/$',views.PostDeleteView.as_view(),name='delete_post'),
    url(r'drafts/$',views.PostDraftListView.as_view(),name='draft_post'),
    url(r'^post/(?P<pk>\d+)/comment/$',views.add_comment_to_post,name='add_comment_to_post'),
    url(r'^comments/(?P<pk>\d+)/approve/$',views.comment_approve,name='comment_approve'),
    url(r'^comment/(?P<pk>\d+)/delete/$',views.comment_delete,name='comment_delete'),
    url(r'^post/(?P<pk>\d+)/publish/$',views.publish_post,name='publish_post')
]
