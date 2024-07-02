from django.db import models


class Query(models.Model):
    number = models.CharField(max_length=50)
    latitude = models.FloatField()
    longitude = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Query {self.id}"


class ExternalServerResponse(models.Model):
    query = models.OneToOneField(Query, on_delete=models.CASCADE)
    result = models.BooleanField()

    def __str__(self):
        return f"Response for Query {self.query.id}"
