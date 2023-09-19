from rest_framework import serializers
from .models import Checklist, CheckListItem

class ChecklistItemSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = CheckListItem
        fields = '__all__'

class ChecklistSerializer(serializers.ModelSerializer):
    items = ChecklistItemSerializer(source='checklistitem_set',many=True, read_only=True)
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Checklist
        fields = '__all__'


    # title = serializers.CharField()
    # is_deleted = serializers.BooleanField()
    # is_archived = serializers.BooleanField()
    # created_on = serializers.DateField()
    # updated_on = serializers.DateField()

# class ChecklistItemSerializer(serializers.Serializer):
#     class Meta:
#         model = CheckListItem
#         fields = ('text', 'is_checked', 'created_on', 'updated_on', 'Checklist')