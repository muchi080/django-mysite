from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.decorators import login_required
from polls import views
from django.views.generic import TemplateView

# 実はページを表示するだけならこのように1行で書くことが出来ます。
Index_view = TemplateView.as_view(template_name="index.html")

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", login_required(Index_view), name="index"),
    path('', include("django.contrib.auth.urls")),  
    path("signup/", views.SignUpView.as_view(), name="signup"),
    path("size/", views.SizeView.as_view(), name="size"),
    path("list/", views.SizeList.as_view(), name="list"),
    path("list/detail/<int:pk>/", views.SizeDetails.as_view(), name="detail"),
    path("list/update/<int:pk>/", views.SizeUpdate.as_view(), name="update"),
    path("list/delete/<int:pk>/", views.SizeDelete.as_view(), name="delete"),
    path("ave/", views.Average.as_view(), name="ave"),

]