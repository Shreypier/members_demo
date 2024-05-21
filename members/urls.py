
from django.urls import path
from members.views import show_members
from members.views import member_details

urlpatterns = [
    path('members/',show_members,name="all-members"),
    path('members/details/<int:id>/',member_details,name="detail-member")
]