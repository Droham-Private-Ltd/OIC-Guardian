from django.db import models

# core/models.py

class Connection(models.Model):
    name = models.CharField(max_length=255)
    oic_identifier = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)


class Token(models.Model):
    connection = models.ForeignKey(Connection, on_delete=models.CASCADE)
    access_token = models.TextField()
    refresh_token = models.TextField()
    expires_at = models.DateTimeField()


class Log(models.Model):
    integration_name = models.CharField(max_length=255)
    event_type = models.CharField(max_length=50)  # request/response/error
    payload = models.JSONField()
    status = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)


class DedupKey(models.Model):
    integration_name = models.CharField(max_length=255)
    message_id = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Audit(models.Model):
    action = models.CharField(max_length=255)
    details = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)