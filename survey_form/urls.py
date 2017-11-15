from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
	url(r'^', include('apps.surveys.urls'))
	#url(r'^surveys/', include('apps.surveys.urls')),
	#url(r'^admin/', admin.site.urls),
]