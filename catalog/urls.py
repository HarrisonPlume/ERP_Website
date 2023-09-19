from django.urls import path
from . import views
#Index
urlpatterns = [
    path("", views.index, name = "index"),
    path("classtimetable/", views.Gym_class.as_view(), name='classlist'),
    path("classupdate/", views.class_update, name="classupdate")
    ]

#Componet Prep urls
# urlpatterns += [
#     path("CPTasks/", views.CpTaskListView.as_view(), name="cptasks"),
#     path("CPTask/<int:pk>/", views.CPTaskDetailView.as_view(), 
#          name = "cptask-detail"),
#     path("CPTask/<int:pk>/updatestatus/", views.CPTaskStatusUpdate.as_view(), 
#          name = "cptask-update-status"),
#     path("CPTask/<int:pk>/delete/", views.CPTaskDelete.as_view(), 
#          name = "cptask-delete"),
#     path("CPTask/<int:pk>/StartTask", views.StartCPTask, 
#          name="startcptask"),
#     path("CPTask/<int:pk>/FinishTask", views.FinishCPTask, 
#        name="finishcptask"),
#     path('mask_feed', views.mask_feed, name='mask_feed'),
#     path("WorkOrderScan/", views.WorkOrderScan, name="Scan"),
#     path('ScanComplete/', views.ScanResult, name='Scan_Complete'),
#     ]
