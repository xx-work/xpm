from rest_framework import serializers, viewsets, status
from rest_framework.response import Response
from rest_framework.serializers import raise_errors_on_nested_writes
import traceback
from rest_framework.utils import html, model_meta, representation
from mgsd.api.utils import get_content_type_for_model, log

from django.conf import settings
AUTH_USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')


class XmodelSerializer(serializers.ModelSerializer):

    readonly_fields = ('id', )

    class Meta:
        model = object
        fields = '__all__'
        depth = 2

    # Default `create` and `update` behavior...
    def create(self, validated_data):
        raise_errors_on_nested_writes('create', self, validated_data)
        ModelClass = self.Meta.model
        info = model_meta.get_field_info(ModelClass)
        many_to_many = {}
        for field_name, relation_info in info.relations.items():
            if relation_info.to_many and (field_name in validated_data):
                many_to_many[field_name] = validated_data.pop(field_name)
        try:
            instance = ModelClass.objects.create(**validated_data)
        except TypeError:
            tb = traceback.format_exc()
            msg = (
                    'Got a `TypeError` when calling `%s.objects.create()`. '
                    'This may be because you have a writable field on the '
                    'serializer class that is not a valid argument to '
                    '`%s.objects.create()`. You may need to make the field '
                    'read-only, or override the %s.create() method to handle '
                    'this correctly.\nOriginal exception was:\n %s' %
                    (
                        ModelClass.__name__,
                        ModelClass.__name__,
                        self.__class__.__name__,
                        tb
                    )
            )
            raise TypeError(msg)

        if many_to_many:
            for field_name, value in many_to_many.items():
                field = getattr(instance, field_name)
                field.set(value)

        self.log('create', instance)
        return instance

    def update(self, instance, validated_data):
        raise_errors_on_nested_writes('update', self, validated_data)
        info = model_meta.get_field_info(instance)
        for attr, value in validated_data.items():
            if attr in info.relations and info.relations[attr].to_many:
                field = getattr(instance, attr)
                field.set(value)
            else:
                setattr(instance, attr, value)
        instance.save()
        self.log('update', instance)
        return instance

    def __delete__(self, instance):
        instance.delete()
        self.log('delete', instance)

    def log(self, action_flag, instance):
        request = self.context["request"]
        try:
            user = request.user
        except:
            user = get_content_type_for_model(AUTH_USER_MODEL).objects.all()[0]
        ModelClass = self.Meta.model
        log(action_flag, user, request, action_flag + str(ModelClass._meta.verbose_name ), instance)


class XModelViewSet(viewsets.ModelViewSet):

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()

        try:
            user = request.user
        except:
            user = get_content_type_for_model(AUTH_USER_MODEL).objects.all()[0]
        log('delete', user, request, '删除' + str(instance._meta.verbose_name), instance)
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
