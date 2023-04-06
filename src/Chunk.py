class Chunk:
    def __init__(self, chunk_id, chunk_type, properties):
        self.chunk_id = chunk_id
        self.chunk_type = chunk_type
        self.properties = properties

    def update_property(self, key, value):
        self.properties[key] = value

    def remove_property(self, key):
        if key in self.properties:
            del self.properties[key]
