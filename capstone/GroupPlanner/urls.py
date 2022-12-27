from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("createGroup", views.createGroup, name="createGroup"),
    path("createActivity/<int:groupId>", views.createActivity, name="createActivity"),
    path("showGroup/<int:groupId>", views.showGroup, name="showGroup"),
    path("addNewMember", views.addNewMember, name="addNewMember"),
    path("groupActivities/<int:groupId>", views.groupActivities, name="groupActivities"),
    path("addComments/<int:groupId>/<int:activityId>", views.addComments, name="addComments"),
    path("viewActivity/<int:groupId>/<int:activityId>", views.viewActivity, name="viewActivity")
]
