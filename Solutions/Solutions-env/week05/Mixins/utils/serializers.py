import json

class Jsonable(object):

    def __set_up_output_dict(self):
        
        attributes = self.__dict__
        
        output = {}
        
        output.update({"dict": attributes})

        class_name = self.__class__.__name__
        output.update({"class_name": f'{class_name}'})

        return output

    def to_json(self, ind = 4):
        output = self.__set_up_output_dict()
        return json.dumps(output, indent = ind)

    @classmethod
    def from_json(cls, json_string):
        pass

class Xmlable(object):
    def to_xml(self):
        pass
    @classmethod
    def from_xml(cls, xml_string):
        pass