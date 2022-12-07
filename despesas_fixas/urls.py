from app import views
from django.contrib import admin
from django.urls import path
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('despesas_fixas/', views.lista_despesas),
    path('', RedirectView.as_view(url='/despesas_fixas/')),
    path('despesas_fixas/despesa/', views.nova_despesa),
    path('despesas_fixas/despesa/submit', views.submit_despesa),
    path('despesas_fixas/despesa/delete/<int:id_despesa>/', views.delete_despesa),
]
