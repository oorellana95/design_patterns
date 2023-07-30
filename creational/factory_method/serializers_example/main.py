from creational.factory_method.serializers_example.SerializerFactory import serializer_factory
from creational.factory_method.serializers_example.Song import Song

if __name__ == "__main__":
    song = Song('1', 'Water of Love', 'Dire Straits')
    print(serializer_factory.serialize(song, 'JSON'))
    print(serializer_factory.serialize(song, 'XML'))
    print(serializer_factory.serialize(song, 'YAML'))
