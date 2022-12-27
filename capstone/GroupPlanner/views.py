from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from annoying.functions import get_object_or_None
import json, datetime
from django.http import JsonResponse
from .models import User, Group, ActivityStatus, GroupActivities


def index(request):
    
    user = request.user.username
    userID = request.user.id
    
    
    try:
        myGroups = Group.objects.filter(groupAdmin=user)
    except Group.DoesNotExist:
        myGroups = None   
        
    try:
        otherGroups = Group.objects.filter(members=userID)
    except Group.DoesNotExist:
        otherGroups = None    
    
    
    return render(request, "GroupPlanner/index.html",{
        "myGroups": myGroups,
        "otherGroups": otherGroups
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "GroupPlanner/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "GroupPlanner/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "GroupPlanner/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "GroupPlanner/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "GroupPlanner/register.html")


@login_required
def createGroup(request):
    
    
    if request.method == "POST":
        
        groupName = request.POST["groupName"]
        category = request.POST["category"]
        user = User.objects.get(pk=request.user.id)
        
        print(groupName, category, user.username)
        
        NewGroup = Group()
        
        NewGroup.groupName = groupName
        NewGroup.category = category
        NewGroup.groupAdmin = user.username
        
        NewGroup.save()
        
        
        try:
            findGroup = Group.objects.get(groupName=groupName, groupAdmin=user.username)
            
            findGroup.members.add(user)
            print(findGroup)
            findGroup.save()
            
            
            print(findGroup)
        except Group.DoesNotExist:
            print("failed to add admin as the member!!")
        
        return render(request, "GroupPlanner/createGroup.html")
        
    else:
    
        return render(request, "GroupPlanner/createGroup.html")
    
@login_required
def showGroup(request, groupId):
    
    try:
        group = Group.objects.get(pk=groupId)
        numOfMembers = group.members.all().count()
        
        if numOfMembers > 0:
            members = group.members.all()
            
        else:
            members = None
            
        
        users_list = list(User.objects.all().exclude(pk=request.user.id))
    
        if members != None:
            for user in users_list:
                if user in members:
                    users_list.remove(user)
            
        # print(users_list)
    except Group.DoesNotExist:
        return HttpResponse(status=404) 
    
    # print(members)
    # print(numOfMembers)
  
    return render(request, "GroupPlanner/showGroup.html",{
        "group": group,
        "members": members,
        "numOfMembers": numOfMembers,
        "users_list": users_list
    })

@login_required
@csrf_exempt
def addNewMember(request):
    
    if request.method == "POST":
        
        # Check the content    
        data = json.loads(request.body)
        
        username = data.get("username", "")
        groupId = data.get("groupId", "")
        
        
        if username == "" or username == " ":        
            return JsonResponse({"result": "Username is invalid"}, status=400)
        
        checkGroup = get_object_or_None(Group, pk=groupId)
        
        if checkGroup is not None:
            
            
            try:
                
                user = User.objects.get(username=username)
                checkUser = list(checkGroup.members.all())
                print(checkUser, user)
                
                if user in checkUser:
                    return JsonResponse({"result": "user already a member"}, status=400) 
                
                checkGroup.members.add(user)
                print(checkGroup)
                checkGroup.save()
                
                return JsonResponse({"result": "saved"}, status=201) 
            except User.DoesNotExist:
                
                return JsonResponse({"result": "failed"}, status=201)         
        
@login_required    
def groupActivities(request, groupId):
    
    try:
        group = Group.objects.get(pk=groupId)
        
        activities = GroupActivities.objects.filter(groupName=group.groupName)
        
            
    except Group.DoesNotExist:
        return HttpResponse(status=404) 
    
    return render(request, "GroupPlanner/groupActivities.html",{
        "group": group,
        "activities": activities
    })
    
@login_required  
def createActivity(request, groupId):
    
    if request.method == "POST":
        
        
        try:
            group = Group.objects.get(pk=groupId)
        except Group.DoesNotExist:
            return HttpResponse(status=404) 
        
        
        title = request.POST["activity_title"]
        meeting_time = request.POST["activity_meetingTime"]  # returns as string, we can split by ":" and get hr, mins
        
        print(f"meeting time - {meeting_time}")
        d = datetime.datetime.strptime(meeting_time, '%Y-%m-%dT%H:%M')
        print(d)
        
        instructions = request.POST["activity_instructions"]
        location = request.POST["activity_location"]
        
        
        newActivity = GroupActivities()
        
        newActivity.activity_creator = request.user.username
        newActivity.title = title
        newActivity.instructions = instructions
        newActivity.groupName = group.groupName
        newActivity.location = location
        
        newActivity.meeting_time = d
        
        newActivity.save()
        print(newActivity)
        
        return HttpResponseRedirect(reverse("groupActivities", args=(groupId,)))
    
    
    else:
        try:
            group = Group.objects.get(pk=groupId)
                
        except Group.DoesNotExist:
            return HttpResponse(status=404) 
        
        return render(request, "GroupPlanner/createActivity.html",{
            "group": group
        })
        
@login_required
@csrf_exempt     
def viewActivity(request, groupId, activityId):
    print(groupId)
    print(activityId)
    
    if request.method == "POST" or request.method == "GET":
        
    
        try:
            group = Group.objects.get(pk=groupId)
            
            activity = GroupActivities.objects.get(pk=activityId)
            print(activity)
            
            comments = ActivityStatus.objects.filter(groupName=group.groupName)
            print(comments)
                
        except Group.DoesNotExist:
            return HttpResponse(status=404) 
        
        return render(request, "GroupPlanner/viewActivity.html",{
            "group": group,
            "activity": activity,
            "comments": comments
        })
    
@login_required
@csrf_exempt    
def addComments(request, groupId, activityId):
    
    if request.method == "POST":        
        
        try:
            group = Group.objects.get(pk=groupId)
            print(group)
            activity = GroupActivities.objects.get(pk=activityId)
            print(activity)
            
            user = request.user
            print(user)
                
        except Group.DoesNotExist:
            return HttpResponse(status=404) 
        
        # Check the content    
        data = json.loads(request.body)
        
        comment = data.get("comment", "")
        status = data.get("choice", "")
                        
        statusObject = ActivityStatus()
        
        statusObject.user = user.username
        statusObject.groupName = group.groupName
        statusObject.comment = comment
        
        if status == "yes":
            statusObject.Iamin = True
            statusObject.Iamout = False
        else:
            statusObject.Iamin = False
            statusObject.Iamout = True
            
        statusObject.save()
        
        return JsonResponse({"result": "comment saved", "user": user.username}, status=201) 
        
        
        
        
        
            
        
        
        
        
        
    
    