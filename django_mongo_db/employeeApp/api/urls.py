from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from employeeApp.api.views import department_api, employee_api, save_file

urlpatterns = [
                  path('dept/', department_api, name='dept'),
                  path('dept/<int:id>/', department_api, name='dept2'),
                  path('emp/', employee_api, name='emp'),
                  path('emp/<int:id>/', employee_api, name='emp2'),
                  path('emp/file/', save_file, name='file'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
