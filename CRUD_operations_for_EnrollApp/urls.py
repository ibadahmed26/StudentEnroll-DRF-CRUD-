from django.contrib import admin
from django.urls import path, include
from enroll import views
from rest_framework.routers import DefaultRouter

# create router object
router = DefaultRouter()

# register stu_viewset in router
router.register('studentapiprivate', views.StudentViewsetprivate, basename='student')
router.register('studentapi', views.StudentViewsetpublic, basename='studentreadonly')
router.register('teacherapiprivate', views.TeacherViewsetprivate, basename='teacher')
router.register('teacherapi', views.TeacherViewsetpublic, basename='teacherreadonly')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),  
]
