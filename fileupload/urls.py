from django.urls import path
from fileupload.views import FileUploadView, FileUploadDetailView

urlpatterns = [
    path('images', FileUploadView.as_view()),
    path('images/<int:pk>', FileUploadDetailView.as_view()),
]
