from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.views.generic import RedirectView
from . import views

urlpatterns = [
	url(r'admin/', admin.site.urls),
	url(r'accounts/', include('django.contrib.auth.urls')),
	url(r'^dashboard/', views.dashboard, name='dashboard'),
	url(r'^bye/', views.bye, name='bye'),
	url(r'^json1/$', views.json1(), name='json1'),
	url(r'^json2/$', views.json2(), name='json2'),
	url(r'^json3/$', views.json3(), name='json3'),
	url(r'^', RedirectView.as_view(pattern_name='dashboard', permanent=False)),

]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
