from django.urls import path
from .views import (HomePageView, AboutPageView,
                    PatientListView, PatientDetailView, PatientCreateView, PatientUpdateView, PatientDeleteView)

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('patient/', PatientListView.as_view(), name='patient'),
    path('blog/<int:pk>', PatientDetailView.as_view(), name='patient_detail'),
    path('blog/create', PatientCreateView.as_view(), name='patient_create'),
    path('blog/<int:pk>/edit', PatientUpdateView.as_view(), name='patient_update'),
    path('blog/<int:pk>/delete', PatientDeleteView.as_view(), name='patient_delete'),
]