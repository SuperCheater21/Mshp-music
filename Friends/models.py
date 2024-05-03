from django.db import models
from Users.models import Profile


class FriendList(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE,related_name="profile")
    friends = models.ManyToManyField(Profile, blank=True, related_name="friends")


    def __str__(self):
        return self.profile.user.username

    def get_friends(self):
        return self.friends.all()

    def count_friends(self):
        return self.friends.all().count()


STATUS_CHOICES = {
    ('send','send'),
    ('accepted', 'accepted'),
    ('rejected', 'rejected')

}

class Relationship(models.Model):
    sender = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="sender")
    receiver = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="receiver")
    status = models.CharField(max_length=8, choices=STATUS_CHOICES)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender}-{self.receiver}-{self.status}"





