from django.contrib import admin
from django.urls import path
from core import views as core_views
from portfolio import views as portfolio_views
from certifica import views as certifica_views
from django.conf import settings

urlpatterns = [
    path('', core_views.home, name="home"),
    path('about/', core_views.about, name="about"),
    path('portfolio/', portfolio_views.portfolio, name="portfolio"),
    path('certifica/', certifica_views.certifica, name="certifica"), #<==
    path('contact/', core_views.contact, name="contact"),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT)