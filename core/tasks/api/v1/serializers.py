from tasks.models import Task
from rest_framework import serializers


class TasksSerializers(serializers.ModelSerializer):
    absolute_urls = serializers.SerializerMethodField()

    class Meta:
        model = Task
        read_only_fields = ['user']
        fields = ['id', 'user', 'title', 'description', 'is_completed', 'created_at', 'absolute_urls']

    def get_absolute_urls(self, obj):
        request = self.context.get('request')
        return request.build_absolute_uri(obj.pk)

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)

    def to_representation(self, instance):
        request = self.context.get('request')
        rep = super().to_representation(instance)
        if request and request.parser_context and request.parser_context.get('kwargs', {}).get('pk'):
            rep.pop('absolute_urls', None)
        else:
            rep.pop('created_date', None)
            rep.pop('updated_date', None)
            rep.pop('created_at', None)
            rep.pop('description', None)
        return rep
