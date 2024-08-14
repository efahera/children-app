from .views import UploadChildrenCSVData
from django.urls import path

urlpatterns = [
    path('upload-csv/', UploadChildrenCSVData.as_view(), name='upload_csv_url'),
]
