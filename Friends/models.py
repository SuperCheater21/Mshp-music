from django.db import models
from django.conf import settings


class FriendList(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name="user")
    friends = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="friends")

    def __str__(self):
        return self.user.username

    def add_friend(self,account):
        if not account in self.friends.all():
            self.friends.add(account)

    def remove_friend(self, account):

        if account in self.friends.all():
            self.friends.remove(account)


    def unfriend(self,removee):
        remover_friends_list = self

        remover_friends_list.remove_friend(removee)

        removee_friends_list = FriendList.objects.get(user=removee)

        removee_friends_list.remove_friend(self.user)

    def is_friend(self,friend):


        if friend in self.friends.all():
            return True
        return False


class FriendRequest(models.Model):
    sender = models.ForeignKey(setting.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="sender")
    receiver = models.ForeignKey(setting.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="receiver")


    is_active = models.BooleanField(blank=True, null=False, default=True)

    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


    def accept(self):

        receiver_friend_list = FriendList.object.get(user=self.receiver)


        if receiver_friend_list:
            receiver_friend_list.add_friend(self.sender)
            sender_friend_list = FriendList.object.get(user=self.sender)
            if sender_friend_list:
                sender_friend_list.add_friend(self.receiver)
                self.is_active = False
                self.save()
    def decline(self):
        self.is_active = False
        self.save()

    def cancel(self):
        self.is_active = False
        self.save()



