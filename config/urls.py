"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from blog.views import create_comment, post_detail, posts_list, create_post, post_detail, post_delete, post_update, create_comment, comment_delete, comment_update

urlpatterns = [

    path('admin/', admin.site.urls),
    path('posts/', posts_list ),
    path('post_create/', create_post),
    path('post_detail/<int:p_id>/', post_detail),
    path('post_delete/<int:p_id>/', post_delete),
    path('post_update/<int:p_id>/', post_update),

    path('comment_create/', create_comment),
    path('comment_delete/<int:c_id>/', comment_delete),
    path('comment_update/<int:c_id>/', comment_update)





]
