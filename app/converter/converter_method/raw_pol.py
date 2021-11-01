from app.converter.containers.xml_template_classes_full_classes import LineItem, Line
from csv import reader
from datetime import date, timedelta
from app.repositories.iln import IlnRepository

SELLER_NIP = '8351001704'
BUYER_ID = '12025441021E'
BUYER_NIP = '6280012377'


class Rawpol:
    def read(self, filename, xml_document):
        with open(filename, encoding='Windows-1250') as file:
            db = IlnRepository()
            data = reader(file, delimiter=';')

            header = next(data)

            xml_document.invoice_parties.seller.tax_id = SELLER_NIP
            xml_document.invoice_parties.seller.iln = db.get_by_nip(SELLER_NIP)
            xml_document.invoice_parties.payee.tax_id = SELLER_NIP
            xml_document.invoice_parties.payee.iln = db.get_by_nip(SELLER_NIP)
            xml_document.invoice_parties.seller_headquarters.tax_id = SELLER_NIP
            xml_document.invoice_parties.seller_headquarters.iln = db.get_by_nip(SELLER_NIP)
            xml_document.invoice_header.invoice_number = f'FS{header[0]}{BUYER_ID}'
            xml_document.invoice_parties.buyer.tax_id = BUYER_NIP
            xml_document.invoice_parties.buyer.iln = db.get_by_nip(BUYER_NIP)
            xml_document.invoice_parties.payer.tax_id = BUYER_NIP
            xml_document.invoice_parties.payer.iln = db.get_by_nip(BUYER_NIP)
            xml_document.invoice_parties.invoicee.tax_id = BUYER_NIP
            xml_document.invoice_parties.invoicee.iln = db.get_by_nip(BUYER_NIP)
            xml_document.invoice_header.invoice_date = date.fromisoformat(header[1][:10])
            xml_document.invoice_header.sales_date = date.fromisoformat(header[1][:10])
            xml_document.invoice_header.invoice_payment_due_date = date.fromisoformat(header[1][:10]) + timedelta(days=10)

            for number, row in enumerate(data):
                xml_document.invoice_lines.append(Line(LineItem(
                        line_number=number + 1,
                        supplier_item_code=row[0],
                        item_description=row[0],
                        item_type='CU',
                        invoice_quantity=float(row[3].replace(',', '.')),
                        invoice_unit_net_price=float(row[4].replace(',', '.')),
                        net_amount=round(float(row[3].replace(',', '.')) * float(row[4].replace(',', '.')), 2),
                        tax_amount=round(float(row[3].replace(',', '.')) * float(row[4].replace(',', '.')) * float(row[6])/100, 2),
                        unit_of_measure=row[2],
                        tax_rate=float(row[6]),
                        ean=row[7],
                        tax_category_code='S'
                )))
