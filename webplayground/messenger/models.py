from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import m2m_changed


# Create your models here.
class Message(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    

    class Meta:
        ordering = ['created']

class TreadManager(models.Manager):
    def find(self, user1, user2):
        #self seria lo mismo que poner Thread.objects.all
        queryset = self.filter(users= user1).filter(users= user2)
        if len(queryset) > 0:
            return queryset[0]
        return None

    def find_or_create(self, user1, user2):
        thread = self.find(user1, user2)
        if thread is None:
            thread = Thread.objects.create()
            thread.users.add(user1, user2)
        return thread


class Thread(models.Model):
    users = models.ManyToManyField(User,related_name='threads')
    messages = models.ManyToManyField (Message)
    updated = models.DateTimeField(auto_now=True)

    objects = TreadManager()

    class Meta:
        ordering = ['-updated']


def messages_changed(sender,**kwargs):
    instance = kwargs.pop("instance",None)
    action = kwargs.pop("action",None)
    pk_set = kwargs.pop("pk_set",None)
    print(instance,action,pk_set)

    false_pk_set = set()
    if action is "pre_add":
        for msg_pk in pk_set:
            msg = Message.objects.get (pk = msg_pk)
            if msg.user not in instance.users.all():
                print("ups ({}) no forma parte del hilo ".format(msg.user))
                false_pk_set.add(msg_pk)
    
    #buscar los mensajes que  estan en el false_pk_set y los borramos del pk_set
    #con difeence_update es como si estuvieramos restando los unso de los otros
    pk_set.difference_update(false_pk_set)

    #forzar actualizacion haciendo un save
    instance.save()

m2m_changed.connect(messages_changed, sender=Thread.messages.through)
