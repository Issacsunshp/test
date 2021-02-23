from django.urls import path,include
import ocr_letters
from . import views
urlpatterns = [
    path('',views.main),
    path('result/',views.result)
]