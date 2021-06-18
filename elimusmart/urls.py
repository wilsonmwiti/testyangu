"""elimusmart URL Configuration"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
import object_tools
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

html_pdf_template=""
urlpatterns = [
    path('', include('website.urls')),
    path('',include('website.blog.urls')),
    path('',include('leads.urls')),
    path('',include('claims.urls')),
    path('',include('checkout.urls')),
    path('', include('authentication.accounts.urls')),
    path('', include('payments.mpesa.urls')),
    path('', include('customer.urls')),
    path('', include('agent.urls')),
    path('admin/', admin.site.urls),
    # 
    path('baton/', include('baton.urls')),#admin
    path('newsletter/', include('newsletter.urls')),#newsletters
    path('ckeditor/', include('ckeditor_uploader.urls')),#ck editor
    path('hijack/', include('hijack.urls', namespace='hijack')),#admin hijacking
    path('report/', include('report_builder.urls')),
    path('export_action/', include("admin_export_action.urls", namespace="admin_export_action")),#admin export  actions
    path('tracking/', include('tracking.urls')),#user tracking

]
# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# Serving the media files in development mode
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    urlpatterns += staticfiles_urlpatterns()