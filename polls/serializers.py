from rest_framework import serializers

from .models import Poll, Choice, Vote

"""
Serialization and Deserialization
The first thing we need for our API is to provide a way to serialize 
model instances into representations. Serialization is the process of 
making a streamable representation of the data which we can transfer 
over the network. Deserialization is its reverse process. 
"""

class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = '__all__'


class ChoiceSerializer(serializers.ModelSerializer):
    votes = VoteSerializer(many=True, required=False)

    class Meta:
        model = Choice
        fields = '__all__'


class PollSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True, read_only=True, required=False)

    class Meta:
        model = Poll
        fields = '__all__'