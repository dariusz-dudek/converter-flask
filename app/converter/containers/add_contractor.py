from app.converter.containers.api import RegonApi


def add_contractor_buyer(xml_document):
    contractor = RegonApi(xml_document.invoice_parties.buyer.tax_id)
    xml_document.invoice_parties.buyer.name = contractor.get_name()
    xml_document.invoice_parties.buyer.street_and_number = contractor.get_street_and_number()
    xml_document.invoice_parties.buyer.city_name = contractor.get_city_name()
    xml_document.invoice_parties.buyer.postal_code = contractor.get_postal_code()
    xml_document.invoice_parties.buyer.country = contractor.get_country_code()


def add_contractor_payer(xml_document):
    contractor = RegonApi(xml_document.invoice_parties.payer.tax_id)
    xml_document.invoice_parties.payer.name = contractor.get_name()
    xml_document.invoice_parties.payer.street_and_number = contractor.get_street_and_number()
    xml_document.invoice_parties.payer.city_name = contractor.get_city_name()
    xml_document.invoice_parties.payer.postal_code = contractor.get_postal_code()
    xml_document.invoice_parties.payer.country = contractor.get_country_code()


def add_contractor_invoicee(xml_document):
    contractor = RegonApi(xml_document.invoice_parties.invoicee.tax_id)
    xml_document.invoice_parties.invoicee.name = contractor.get_name()
    xml_document.invoice_parties.invoicee.street_and_number = contractor.get_street_and_number()
    xml_document.invoice_parties.invoicee.city_name = contractor.get_city_name()
    xml_document.invoice_parties.invoicee.postal_code = contractor.get_postal_code()
    xml_document.invoice_parties.invoicee.country = contractor.get_country_code()


def add_contractor_seller(xml_document):
    contractor = RegonApi(xml_document.invoice_parties.seller.tax_id)
    xml_document.invoice_parties.seller.name = contractor.get_name()
    xml_document.invoice_parties.seller.street_and_number = contractor.get_street_and_number()
    xml_document.invoice_parties.seller.city_name = contractor.get_city_name()
    xml_document.invoice_parties.seller.postal_code = contractor.get_postal_code()
    xml_document.invoice_parties.seller.country = contractor.get_country_code()


def add_contractor_payee(xml_document):
    contractor = RegonApi(xml_document.invoice_parties.payee.tax_id)
    xml_document.invoice_parties.payee.name = contractor.get_name()
    xml_document.invoice_parties.payee.street_and_number = contractor.get_street_and_number()
    xml_document.invoice_parties.payee.city_name = contractor.get_city_name()
    xml_document.invoice_parties.payee.postal_code = contractor.get_postal_code()
    xml_document.invoice_parties.payee.country = contractor.get_country_code()


def add_contractor_seller_headquarters(xml_document):
    contractor = RegonApi(xml_document.invoice_parties.seller_headquarters.tax_id)
    xml_document.invoice_parties.seller_headquarters.name = contractor.get_name()
    xml_document.invoice_parties.seller_headquarters.street_and_number = contractor.get_street_and_number()
    xml_document.invoice_parties.seller_headquarters.city_name = contractor.get_city_name()
    xml_document.invoice_parties.seller_headquarters.postal_code = contractor.get_postal_code()
    xml_document.invoice_parties.seller_headquarters.country = contractor.get_country_code()


def add_contractor_all(xml_document):
    add_contractor_buyer(xml_document)
    add_contractor_payer(xml_document)
    add_contractor_invoicee(xml_document)
    add_contractor_seller(xml_document)
    add_contractor_payee(xml_document)
    add_contractor_seller_headquarters(xml_document)
