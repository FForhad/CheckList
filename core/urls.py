from django.urls import path,include
from core.views import (
    ChecklistAPIView,
    ChecklistsAIPView,
    ChecklistItemCreateAPIView,
    ChecklistItemAPIView,

    )

urlpatterns = [
    path('api/checklist/', ChecklistAPIView.as_view()),
    path('api/checklist/<int:pk>', ChecklistsAIPView.as_view()),
    path('api/checklistItem/create/', ChecklistItemCreateAPIView.as_view()),
    path('api/checklistItem/<int:pk>', ChecklistItemAPIView.as_view()),
]
