from django.urls import path
from fileupload.views import FileUploadView


urlpatterns = [
    path('', FileUploadView.as_view()),
]
