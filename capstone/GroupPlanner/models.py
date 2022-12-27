from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Group(models.Model):

    # Group Name
    groupName = models.CharField(max_length=50)
    
    # When was the Group created
    timestamp = models.DateTimeField(auto_now_add = True)
    
    # Who created the Group (admin)
    groupAdmin = models.CharField(max_length=50,blank=True, null=True)
    
    # Members (ManyToMany relationship with User model and relatedname="memebrs")
    members = models.ManyToManyField(User, blank=True)
    
    # Type of Group 
    category = models.CharField(max_length=15)
    
    
    def __str__(self):
        return f"Group: {self.groupName} created by {self.groupAdmin} on {self.timestamp} about {self.category} "
    
    
class GroupActivities(models.Model):
    
    # title of the activity
    title = models.CharField(max_length=100)
    
    # When was the activity created
    timestamp = models.DateTimeField(auto_now_add = True)
    
    # Meeting time of the activity
    meeting_time = models.DateTimeField(blank=True)
    
    # location of the meeting
    location = models.CharField(max_length=100, blank=True)
    
    # Who created the Group (admin)
    activity_creator = models.CharField(max_length=50,blank=True, null=True)
    
    # instructions
    instructions = models.TextField()
    
    # private field for us to know which Group this activity belongs to
    groupName = models.CharField(max_length=50, blank=True)
    
    
    def __str__(self):
        createdOn = self.timestamp.strftime("%b %d %Y, %I:%M %p")
        return f"Activity: {self.title}, created by {self.activity_creator} on {createdOn}. Meeting Time - {self.meeting_time} , Location - {self.location}"
    
    
class ActivityStatus(models.Model):
    
    # who is the user
    user = models.CharField(max_length=50)
    
    # private field for us to know which Group this activity belongs to
    groupName = models.CharField(max_length=50, blank=True)
    
    # comments
    comment = models.CharField(max_length=150,blank=True, null=True)
    
    # user is In?
    Iamin = models.BooleanField(blank=True, null=True)
    
    # user is Out?
    Iamout = models.BooleanField(blank=True, null=True)
        
        
        
    
    def __str__(self):
        
        if self.Iamin == True and self.Iamout == False:
            return f"user: {self.user} is In for {self.groupName}. Comments: {self.comment}"
        
        else:
            
            return f"user: {self.user} is NOT In for {self.groupName}. Comments: {self.comment}"