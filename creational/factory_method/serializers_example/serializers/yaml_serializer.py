import yaml
from creational.factory_method.serializers_example.serializers.json_serializer import JsonSerializer


class YamlSerializer(JsonSerializer):
    def to_str(self):
        return yaml.dump(self._current_object)
