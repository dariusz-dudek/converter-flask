from app.converter.containers.add_contractor import add_contractor_all
from app.converter.containers.calculate_sumary import Sumary
from app.converter.draw import draw_xml
from pyexcel.exceptions import FileTypeNotSupported

class AddFunction:
    @staticmethod
    def load_file(converter, xml_doc, name, ext):

        try:
            converter.read(f'app/static/uploaded_files/input{ext}', xml_doc)
            add_contractor_all(xml_doc)
            Sumary.calculate_sumary(xml_doc)
            draw_xml(f'app/static/result/{name}.xml', xml_doc)
            return True, ''
        except FileNotFoundError as e:
            return False, e
        except FileTypeNotSupported as e:
            return False, e
        except IndexError as e:
            return False, e




