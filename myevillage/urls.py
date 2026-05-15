from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),

    # Homepage
    path('', TemplateView.as_view(template_name='delivery-free-lite/index.html'), name='home'),

    # API Routes
    path('api/auth/', include('accounts.urls')),
    path('api/services/', include('village_services.urls')),
    path('api/governance/', include('governance.urls')),
    path('api/healthcare/', include('healthcare.urls')),
    path('api/education/', include('education.urls')),
    path('api/farming/', include('farming.urls')),
    path('api/market/', include('market.urls')),
    path('api/energy/', include('energy.urls')),
    path('api/contact/', include('contact.urls')),
    path('api/donations/', include('donations.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static('/assets/', document_root=str(settings.BASE_DIR / 'frontend' / 'delivery-free-lite' / 'assets'))