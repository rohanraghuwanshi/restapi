from rest_framework import serializers

from app.models import Status

class StatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = Status
        fields = [
            "user",
            "content",
            "image"
        ]
        read_only_fields = ['user']

    def validate(self, data):
        content = data.get("content", None)
        if content == "":
            content = None
        image = data.get("image", None)
        if content is None and image is None:
            raise serializers.ValidationError("Content or image is required.")

        return data