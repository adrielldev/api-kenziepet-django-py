from groups.models import Group
from traits.models import Trait
from rest_framework import serializers
from groups.serializers import GroupSerializer
from traits.serializers import TraitSerializer
from animals.models import Animal

class AnimalSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    age = serializers.CharField()
    weight = serializers.CharField()
    age_in_human_years = serializers.SerializerMethodField()
    sex = serializers.CharField() 
    group = GroupSerializer(many=False)
    traits = TraitSerializer(many=True)

    def create(self,validated_data:dict):

        group_data = validated_data.pop('group')
        trait_data = validated_data.pop('traits')

        g = Group.objects.get_or_create(group_data)[0]
        animal = Animal.objects.create(**validated_data,group = g)
        for trait in trait_data:
            t = Trait.objects.get_or_create(name=TraitSerializer(trait).data['name'])[0]

            animal.traits.add(t)
        return animal

    def update(self,instance:Animal,validated_data:dict):
        instance.name = validated_data.get('name',instance.name)
        instance.age = validated_data.get('age',instance.age)
        instance.weight = validated_data.get('weight',instance.weight)
        instance.save()

        return instance
    def get_age_in_human_years(self,obj):
        return obj.convert_dog_age_to_human_years()




