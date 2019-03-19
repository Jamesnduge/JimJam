from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url

urlpatterns = [
    url(r'home$', views.home, name='home'),
    url(r'^search/', views.search, name='search'),
    url(r'^accounts/edit/',views.edit_profile, name='edit_profile'),
    url(r'^user/(?P<username>\w+)', views.profile, name='profile'),
    url(r'^$',views.signup, name='signup'),
    url(r'^upload/$', views.upload_image, name='upload_image'),
]