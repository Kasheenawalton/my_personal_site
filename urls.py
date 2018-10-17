import views
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static
urlpatterns = static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


urlpatterns = [
    path('blog2.html', views.about_me),
    path('contact2.html', views.contact_me),
    path('blog1.html', views.content),
    path('github_api', views.github_api),
]
