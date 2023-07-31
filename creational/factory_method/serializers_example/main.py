from creational.factory_method.serializers_example.serializer_factory import serializer_factory
from creational.factory_method.serializers_example.song import Song


def main_factory_method_serializers_example():
    song = Song('1', 'Water of Love', 'Dire Straits')
    print(serializer_factory.serialize(song, 'JSON'))
    print(serializer_factory.serialize(song, 'XML'))
    print(serializer_factory.serialize(song, 'YAML'))
