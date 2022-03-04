from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]

#! for react app we will run npm run build and take the build file and put it here
urlpatterns += [re_path(r'^.*', TemplateView.as_view(template_name='index.html'))]