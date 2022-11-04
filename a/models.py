from django.db import models as m

from django.contrib.auth.models import User

from uuid import uuid4 as u4

class N(m.Model):

    uid = m.UUIDField(default = u4)

    u = m.ForeignKey(User, on_delete = m.CASCADE)

    t = m.CharField(max_length = 300, blank = True)

    c = m.TextField(max_length = 1000000, blank = True)

    p = m.BooleanField(default = False)

    ca = m.DateTimeField(auto_now_add = True)

    ua = m.DateTimeField(auto_now = True)


    def __str__(self):

        if self.t:

            return f"{self.t} by {self.u.username}"
        
        else:

            return f"Unnamed by {self.u.username}"

    class Meta:

        ordering = ['-p', '-ua']
        verbose_name = 'Note'