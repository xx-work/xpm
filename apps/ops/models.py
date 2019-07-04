from django.db import models
import uuid


class OpsInfo(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)


"""


"""