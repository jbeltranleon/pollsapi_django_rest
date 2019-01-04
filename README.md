### What have we got with this? The PollSerializer class has a number of methods,

* is_valid(self, ..) method which can tell if the data is sufficient and valid to create/update a model instance.
* save(self, ..) method, which khows how to create or update an instance.
* create(self, validated_data, ..) method which knows how to create an instance. This method can be overriden to customize the create behaviour.
* update(self, instance, validated_data, ..) method which knows how to update an instance. This method can be overriden to customize the update behaviour.

> https://books.agiliq.com/projects/django-api-polls-tutorial/en/latest/serailizers.html