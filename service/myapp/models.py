from django.db import models


class Query(models.Model):
    number = models.CharField(max_length=50, null=False, default=None)
    latitude = models.IntegerField(null=False, default=None)
    longitude = models.IntegerField(null=False, default=None)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Query {self.id}"


class ExternalServerResponse(models.Model):
    number = models.CharField(max_length=50, null=False, default=None)
    latitude = models.IntegerField(null=False, default=None)
    longitude = models.IntegerField(null=False, default=None)
    result = models.BooleanField()

    def __str__(self):
        return f"Response for Query {self.number}"
