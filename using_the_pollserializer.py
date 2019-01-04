from polls.serializers import PollSerializer
from polls.models import Poll

# Creating

print('# Creating')

poll_serializer = PollSerializer(
                    data={"question": "Mojito or Caipirinha?",
                          "created_by": 1
                        }
                    )

print('Form is valid? -> ', poll_serializer.is_valid())
poll = poll_serializer.save()
print('id: {} created'.format(poll.pk))
print('Question: ', Poll.objects.get(pk=poll.pk).question)

# Editing

print('# Editing')

poll_serializer = PollSerializer(
                    instance=poll, 
                    data={"question": "Mojito, Caipirinha or margarita?", 
                          "created_by": 1
                        }
                    )
                    
print('Form is valid? -> ', poll_serializer.is_valid())
poll = poll_serializer.save()
print('id: {} updated'.format(poll.pk))
print('Question: ', Poll.objects.get(pk=poll.pk).question)