from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import DedupKey

@api_view(['POST'])
def dedup_check(request):
    integration = request.data.get("integration_name")
    message_id = request.data.get("message_id")

    if not integration or not message_id:
        return Response({
            "status": "error",
            "error": "Missing required fields"
        }, status=400)

    if DedupKey.objects.filter(message_id=message_id).exists():
        return Response({
            "status": "success",
            "data": {"process": False}
        })

    DedupKey.objects.create(
        integration_name=integration,
        message_id=message_id
    )

    return Response({
        "status": "success",
        "data": {"process": True}
    })