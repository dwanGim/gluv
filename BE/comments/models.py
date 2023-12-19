from django.db import models
from users.models import User
from posts.models import CommunityPost 
from recruits.models import RecruitmentPost

class Comment(models.Model):
    user_id = models.ForeignKey('users.User', on_delete=models.CASCADE)
    recruit_id = models.ForeignKey(RecruitmentPost, on_delete=models.CASCADE, null=True, blank=True)
    post_id = models.ForeignKey(CommunityPost, on_delete=models.CASCADE, null=True, blank=True)
    content = models.TextField(max_length=100)
    to_user = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return f"Comment by {self.user}: {self.content}"

