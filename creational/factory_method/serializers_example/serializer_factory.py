from creational.factory_method.serializers_example.serializers.json_serializer import JsonSerializer
from creational.factory_method.serializers_example.serializers.xml_serializer import XmlSerializer
from creational.factory_method.serializers_example.serializers.yaml_serializer import YamlSerializer


class SerializerFactory:

    def __init__(self, creators=None):
        self._creators = {} if creators is None else creators

    def serialize(self, serializable_object, key):
        serializer = self._get_serializer(key)
        serializable_object.serialize(serializer)
        return serializer.to_str()

    def _get_serializer(self, key):
        creator = self._creators.get(key)
        if not creator:
            raise ValueError(key)
        return creator()


serializer_factory = SerializerFactory(
    creators={
        'JSON': JsonSerializer,
        'XML': XmlSerializer,
        'YAML': YamlSerializer
    }
)
