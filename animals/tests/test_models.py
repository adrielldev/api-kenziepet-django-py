from django.test import TestCase
from animals.models import Animal
from groups.models import Group
from traits.models import Trait




class AnimalTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.group_data = {"name": "cão", "scientific_name": "canis familiaris"}
        cls.trait_data = {"name": "peludo"}
        cls.group = Group.objects.create(**cls.group_data)
        animal_data={
        "name": "Beethoven",
        "age": 1,
        "weight": 30.0,
        "sex": "Macho",
        "group": cls.group
        }
        

        cls.animal = Animal.objects.create(**animal_data)
        trait = Trait.objects.create(**cls.trait_data)
        cls.animal.traits.add(trait)
        cls.traits = [Trait.objects.create(name='peludo' + str(i)) for i in range(20)]
    
    def test_animals_data(self):
        """Validate animals data"""
        animal = self.animal
        self.assertEqual('Beethoven',animal.name)
        self.assertEqual(1,animal.age)
        self.assertEqual(30.0,animal.weight)
        self.assertEqual("Macho",animal.sex)
        self.assertEqual("cão",animal.group.name)

    def test_dog_age_to_human_years(self):
        """Test the method to convert the dog age to human years"""
        animal = self.animal
        dog_age = animal.convert_dog_age_to_human_years()
        self.assertEqual(31.0,dog_age)
    
    # one to many group with animals

    def test_animal_cannot_have_more_than_one_group(self):
        group_two_data = {"name": "gato", "scientific_name": "felinus familiaris"}
        group_two = Group.objects.create(**group_two_data)
        self.animal.group = group_two
        self.assertEqual(self.animal.group.name,'gato')
        self.assertNotEqual(self.animal.group.name,'cão')

    def test_group_can_be_in_more_than_one_animal(self):
        trait_data = {"name":"a"}
        animal_two_data={
        "name": "Mozart",
        "age": 2,
        "weight": 30.0,
        "sex": "Macho",
        "group": self.group,
        }

        animal_two = Animal.objects.create(**animal_two_data)
        trait= Trait.objects.create(**trait_data)
        animal_two.traits.add(trait)
        # same group in both animals
        self.assertEqual(animal_two.group.name,'cão')
        self.assertEqual(animal_two.group.scientific_name,'canis familiaris')
        self.assertEqual(self.animal.group.name,'cão')
        self.assertEqual(self.animal.group.scientific_name,'canis familiaris')



    # many to many animal with traits

    def test_animal_can_have_multiple_traits(self):
        for trait in self.traits:
            self.animal.traits.add(trait)
        # +1 pois eu adiciono um trait logo no setup para conseguir testar os atributos
        self.assertEqual(len(self.traits) + 1,self.animal.traits.count())