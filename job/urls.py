from django.urls import path
from . import views

urlpatterns = [
    path('jobs', views.getAllJobs, name='jobs'),
    path('jobs/new', views.newJob, name='new_job'),
    path('jobs/<str:pk>', views.getJob, name='job'),
    path('jobs/<str:pk>/update', views.updateJob, name='update_job'),
    path('jobs/<str:pk>/delete', views.deleteJob, name='delete_job'),
    path('jobs/stats/<str:topic>', views.getTopicStatus, name='get_topic_stats'),
    path('jobs/<str:pk>/apply', views.applyToJob, name='apply_to_job'),
    path('me/jobs/applied', views.getCurrentUserAppliedJobs, name='current_user_applied_job'),

]