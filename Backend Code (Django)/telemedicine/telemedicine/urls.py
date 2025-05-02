from django.conf.urls.i18n import i18n_patterns
from django.urls import path, include
from django.views.i18n import set_language
from django.contrib import admin

urlpatterns = [
    path('set-language/', set_language, name='set_language'),
]

urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('consultations/', include('consultations.urls')),
    path('payments/', include('payments.urls')),
    path('messaging/', include('messaging.urls')),
    path('extras/', include('extras.urls')),
    path('legal/', include('legal.urls')),
    path('listings/', include('listings.urls')),
    path('', include('accounts.urls')),
)
