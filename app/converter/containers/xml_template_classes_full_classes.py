from dataclasses import dataclass
from datetime import date


@dataclass
class Order:
    buyer_order_number: str = ''              # Numer zamówienia
    supplier_order_number: str = ''           # Numer zamówienia według sprzedawcy
    buyer_order_date: date = date.today()           # Data zamówienia


@dataclass
class Reference:
    invoice_reference_number: str = ''        # Numer faktury korygowanej
    invoice_reference_date: date = date.today()     # Data faktury korygowanej


@dataclass
class DeliveryTerms:
    # Kod warunków dostawy lub transportu (INCOTERMS):
    # „04E” – płatne przy odbiorze
    # „EXW” – ex works
    # „FOR” – przekazane przewoźnikowi w określonym miejscu
    # „CPT” – opłacone do miejsca dostawy
    delivery_terms_code: str = ''
    # Sposób płatności kosztów transportu:
    # „DF” – określony przez kupującego i dostawcę
    # „PC” – opłacony z góry, obciążający klienta
    payment_method: str = ''


@dataclass
class Delivery:
    delivery_location_number: int = 0        # ILN lokalizacji dostawy (sklepu)
    tax_id: str = ''                          # NIP lokalizacji dostawy (sklepu)
    delivery_date: date = date.today()              # Data dostawy
    despatch_number: str = ''                 # Numer dostawy
    despatch_date: date = date.today()              # Data dokumentu dostawy
    despatch_advice_number: str = ''          # Numer awiza wysyłki
    name: str = ''                            # Nazwa Punktu Dostawy
    street_and_number: str = ''               # Ulica i numer
    city_name: str = ''                       # Miasto
    postal_code: str = ''                     # Kod pocztowy
    country: str = ''                         # Kraj (kodowane ISO 3166)
    delivery_terms: DeliveryTerms = DeliveryTerms()


@dataclass
class Returns:
    returns_notice_number: str = ''           # Numer zawiadomienia o zwrotach
    returns_notice_date: str = ''             # Data zawiadomienia o zwrotach


@dataclass
class InvoiceHeader:
    invoice_number: str = ''                  # Numer faktury
    invoice_date: date = date.today()               # Data faktury
    sales_date: date = date.today()                 # Data dostawy towarów lub wykonania usługi
    invoice_duplicate_date: date = date.today()     # Data duplikatu faktury
    invoice_currency: str = ''                # Waluta faktury
    invoice_payment_due_date: date = date.today()   # Data płatności
    invoice_payment_terms: int = 0           # Termin płatności (w dniach)
    invoice_payment_means: str = ''           # Sposób płatności: 10–gotówka 20–czek 42–przelew 97–kompensata
    payment_information: str = ''             # Adnotacja o podzielonej płatności
    deferred_payment: str = ''                # Tekstowy opis odroczonej płatności
    invoice_post_date: date = date.today()          # Data wpłynięcia do systemu
    document_function_code: str = ''          # Typ dokumentu: O–oryginał D–duplikat C–korekta R–duplikat korekty
    message_type: str = ''                    # Typ dokumentu: INV–faktura SB–rachunek własny
    correction_reason: str = ''               # Powód korekty
    remarks: str = ''                         # Uwagi
    order: Order = Order()
    reference: Reference = Reference()
    delivery: Delivery = Delivery()
    returns: Returns = Returns()


@dataclass
class Buyer:
    iln: int = 0                             # ILN Kupującego
    tax_id: str = ''                          # NIP Kupującego
    account_number: str = ''                  # Konto bankowe Kupującego
    name: str = ''                            # Nazwa Kupującego
    street_and_number: str = ''               # Ulica i numer
    city_name: str = ''                       # Miasto
    postal_code: str = ''                     # Kod pocztowy
    country: str = ''                         # Kraj (kodowane ISO 3166)


@dataclass
class Payer:
    iln: int = 0                             # ILN Płatnika
    tax_id: str = ''                          # NIP Płatnika
    account_number: str = ''                  # Konto bankowe Płatnika.
    name: str = ''                            # Nazwa Płatnika
    street_and_number: str = ''               # Ulica i numer
    city_name: str = ''                       # Miasto
    postal_code: str = ''                     # Kod pocztowy
    country: str = ''                         # Kraj (kodowane ISO 3166)


@dataclass
class Invoicee:
    iln: int = 0                             # ILN Odbiorcy Faktury
    tax_id: str = ''                          # NIP Odbiorcy Faktury
    account_number: str = ''                  # Konto bankowe Odbiorcy Faktury.
    name: str = ''                            # Nazwa Odbiorcy Faktury
    street_and_number: str = ''               # Ulica i numer
    city_name: str = ''                       # Miasto
    postal_code: str = ''                     # Kod pocztowy
    country: str = ''                         # Kraj (kodowane ISO 3166)


@dataclass
class ContactInformation:
    contact_id: str = ''                      # Id kontaktu
    contact_name: str = ''                    # Nazwa kontaktu
    phone_number: str = ''                    # Numer kontaktowy
    fax: str = ''                             # Fax
    electronic_mail: str = ''                 # Adres e-mail
    x400: str = ''                            # X400


@dataclass
class AccountingContactInformation:
    contact_id: str = ''                      # Id kontaktu
    contact_name: str = ''                    # Nazwa kontaktu
    phone_number: str = ''                    # Numer kontaktowy
    fax: str = ''                             # Fax
    electronic_mail: str = ''                 # Adres e-mail
    x400: str = ''                            # X400


@dataclass
class SalesAdministration:
    contact_id: str = ''                      # Id kontaktu
    contact_name: str = ''                    # Nazwa kontaktu
    phone_number: str = ''                    # Numer kontaktowy
    fax: str = ''                             # Fax
    electronic_mail: str = ''                 # Adres e-mail
    x400: str = ''                            # X400


@dataclass
class SalesRepresentative:
    contact_id: str = ''                      # Id kontaktu
    contact_name: str = ''                    # Nazwa kontaktu
    phone_number: str = ''                    # Numer kontaktowy
    fax: str = ''                             # Fax
    electronic_mail: str = ''                 # Adres e-mail
    x400: str = ''                            # X400


@dataclass
class Seller:
    iln: int = 0                             # ILN Sprzedawcy
    tax_id: str = ''                          # NIP Sprzedawcy
    account_number: str = ''                  # Konto bankowe Sprzedawcy
    financial_institution_name: str = ''      # Nazwa instytucji finansowej
    code_by_buyer: str = ''                   # Kod dostawcy wg Kupującego
    name: str = ''                            # Nazwa Sprzedawcy
    street_and_number: str = ''               # Ulica i numer
    city_name: str = ''                       # Miasto
    postal_code: str = ''                     # Kod pocztowy
    country: str = ''                         # Kraj (kodowane ISO 3166)
    utilization_register_number: str = ''     # Numer rejestrowy (utylizacyjny)
    court_and_capital_information: str = ''   # Oznaczenie sądu rejestrowego i numeru rejestru
    certificate_number: str = ''              # Numer certyfikatu
    contact_information: ContactInformation = ContactInformation()
    accounting_contact_information: AccountingContactInformation = AccountingContactInformation()
    sales_administration: SalesAdministration = SalesAdministration()
    sales_representative: SalesRepresentative = SalesRepresentative()


@dataclass
class Payee:
    iln: int = 0                             # ILN Odbiorcy Płatności
    tax_id: str = ''                          # NIP Odbiorcy Płatności
    account_number: str = ''                  # Konto Odbiorcy Płatności
    name: str = ''                            # Nazwa Odbiorcy Płatności
    street_and_number: str = ''               # Ulica i numer
    city_name: str = ''                       # Miasto
    postal_code: str = ''                     # Kod pocztowy
    country: str = ''                         # Kraj (kodowane ISO 3166)


@dataclass
class SellerHeadquarters:
    iln: int = 0                             # ILN Siedziby Sprzedawcy
    name: str = ''                            # Nazwa Siedziby Sprzedawcy
    street_and_number: str = ''               # Ulica i numer
    city_name: str = ''                       # Miasto
    postal_code: str = ''                     # Kod pocztowy
    country: str = ''                         # Kraj (kodowane ISO 3166)


@dataclass
class OrderedBy:
    iln: int = 0                             # ILN Zamawiającego
    tax_id: str = ''                          # NIP Zamawiającego
    account_number: str = ''                  # Konto bankowe Zamawiającego
    name: str = ''                            # Nazwa Zamawiającego
    street_and_number: str = ''               # Ulica i numer
    city_name: str = ''                       # Miasto
    postal_code: str = ''                     # Kod pocztowy
    country: str = ''                         # Kraj (kodowane ISO 3166)


@dataclass
class Sender:
    iln: int = 0                             # GLN Wysyłającego
    tax_id: str = ''                          # NIP Wysyłającego
    name: str = ''                            # Nazwa Wysyłającego
    street_and_number: str = ''               # Ulica i numer
    city_name: str = ''                       # Miasto
    postal_code: str = ''                     # Kod pocztowy
    country: str = ''                         # Kraj (kodowane ISO 3166)


@dataclass
class Receiver:
    iln: int = 0                             # GLN Odbierającego
    tax_id: str = ''                          # NIP Odbierającego
    name: str = ''                            # Nazwa Odbierającego
    street_and_number: str = ''               # Ulica i numer
    city_name: str = ''                       # Miasto
    postal_code: str = ''                     # Kod pocztowy
    country: str = ''                         # Kraj (kodowane ISO 3166)


@dataclass
class InvoiceParties:
    buyer: Buyer = Buyer()
    payer: Payer = Payer()
    invoicee: Invoicee = Invoicee()
    seller: Seller = Seller()
    payee: Payee = Payee()
    seller_headquarters: SellerHeadquarters = SellerHeadquarters()
    ordered_by: OrderedBy = OrderedBy()
    sender: Sender = Sender()
    receiver: Receiver = Receiver()


@dataclass
class TaxReference:
    reference_type: str = ''                  # Kod typu referencji: „SWW” lub „PKWiU”
    reference_number: str = ''                # Kod SWW lub PKWiU


@dataclass
class LineItem:
    line_number: int = 0                     # Numer linii
    order_line_number: int = 0               # Numer linii z zamówienia
    ean: str = ''                             # EAN produktu
    buyer_item_code: str = ''                 # Kod produktu wg nabywcy
    supplier_item_code: str = ''              # Kod produktu wg dostawcy
    manufacturer_item_code: str = ''          # Kod produktu wg producenta
    serial_number: str = ''                   # Numer serii
    customs_code: str = ''                    # Kod celny towaru
    item_description: str = ''                # Nazwa produktu
    # Identyfikator opakowania zwrotnego:
    # "CU" – jednostka handlowa
    # "RC" – opakowanie zwrotne
    # "IN" – jednostka fakturowana
    item_type: str = ''
    country_of_origin: str = ''               # Kraj pochodzenia
    grade: str = ''                           # Klasa produktu
    variety: str = ''                         # Odmiana
    payment_information: str = ''             # Informacje o płatności: “Mechanizm podzielonej płatności”
    # Typ produktu, dodatkowe informacje dotyczące
    # produktów z grupy warzywa i owoce. Zgodnie z rozporządzeniem Komisji EU nr 543/2011
    # należy w niektórych przypadkach przekazywać również informacje o np. klasie, typie
    # handlowym, odmianie itp
    product_type: str = ''
    product_size: str = ''                    # Rozmiar produktu
    product_color: str = ''                   # Kolor produktu
    special_conditions: str = ''              # Specjalne warunki
    invoice_quantity: float = 0              # Zafakturowana ilość
    unit_of_measure: str = ''                 # Jednostka miary
    invoice_unit_packsize: float = 0         # Liczba sztuk detalicznych w jednostce zbiorczej
    pack_item_unit_of_measure: str = ''       # Jednostka miary sztuki detalicznej w jednostce zbiorczej
    free_goods_quantity: float = 0           # Ilość towaru darmowego
    delivered_quantity: float = 0            # Dostarczona ilość
    invoice_unit_net_price: float = 0        # Cena netto
    invoice_unit_gross_price: float = 0      # Cena brutto
    invoice_unit_retail_price: float = 0     # Cena detaliczna
    invoice_unit_price_without_charges: float = 0    # Cena informacyjna przed uwzględnieniem opłaty cukrowej
    tax_rate: float = 0                      # Stawka VAT
    # Kod stawki:
    # "E" (exempt) - zwolniony
    # "S" (standard) - inna, wyrażona liczba ("standardowa")
    # "NA" (not applicable) – nie podlega "AE" (reverse charge)- odwrotne obciążenie
    tax_category_code: str = ''
    tax_reference: TaxReference = TaxReference()
    tax_amount: float = 0                    # Wartość VAT pozycji
    net_amount: float = 0                    # Wartość netto pozycji
    deposit_amount: float = 0                # Kwota kaucji za towary kaucjonowane
    previous_invoice_quantity: float = 0     # Zafakturowana ilość przed korektą
    previous_delivered_quantity: float = 0   # Dostarczona ilość przed korektą
    previous_invoice_unit_net_price: float = 0   # Cena netto przed korektą
    previous_tax_rate: float = 0             # Stawka VAT przed korektą
    # Kod stawki:
    # "E" (exempt) - zwolniony
    # "S" (standard) - inna, wyrażona liczba ("standardowa")
    # "NA" (not applicable) – nie podlega "AE" (reverse charge)- odwrotne obciążenie
    previous_tax_category_code: str = ''
    previous_tax_amount: float = 0           # Wartość VAT pozycji przed korektą
    previous_net_amount: float = 0           # Wartość netto pozycji przed korektą
    previous_deposit_amount: float = 0       # Kwota kaucji za towary kaucjonowane przed korektą
    correction_invoice_quantity: float = 0   # Zafakturowana ilość.Różnica pomiędzy wartością prawidłową a korygowaną
    correction_delivered_quantity: float = 0  # Dostarczona ilość. Różnica pomiędzy wartością prawidłową a korygowaną
    correction_invoice_unit_net_price: float = 0  # Cena netto. Różnica pomiędzy wartością prawidłową, a korygowaną
    correction_tax_amount: float = 0         # Wartość VAT pozycji.Różnica pomiędzy wartością prawidłową a korygowaną
    correction_net_amount: float = 0         # Wartość netto - różnica pomiędzy wartością prawidłową, a korygowaną
    correction_gross_amount: float = 0       # Wartość brutto - różnica pomiędzy wartością prawidłową, a korygowaną
    # Kwota kaucji za towary kaucjonowane – różnica pomiędzy wartością prawidłową, a korygowaną
    correction_deposit_amount: float = 0
    expiration_date: date = date.today()            # Data ważności
    production_date: date = date.today()            # Data produkcji
    best_before_date: date = date.today()           # Data przydatności do spożycia
    sales_date: date = date.today()                 # Data dostawy towarów lub wykonania usługi
    certificate_number: str = ''              # Numer certyfikatu
    correction_reason: str = ''               # Powód korekty
    utilization_fee: str = ''                 # Kwota kosztu gospodarowania odpadami (opłata utylizacyjna)


@dataclass
class LineOrder:
    buyer_order_number: str = ''              # Numer zamówienia
    supplier_order_number: str = ''           # Numer zamówienia według sprzedawcy
    buyer_order_date: date = date.today()           # Data zamówienia


@dataclass
class LineReference:
    invoice_reference_number: str = ''        # Numer faktury korygowanej
    invoice_reference_date: date = date.today()     # Data faktury korygowanej


@dataclass
class DeliveryTerms:
    # Kod warunków dostawy lub transportu (INCOTERMS):
    # „04E” – płatne przy odbiorze
    # „EXW” – ex works
    # „FOR” – przekazane przewoźnikowi w określonym miejscu
    # „CPT” – opłacone do miejsca dostawy
    delivery_terms_code: str = ''
    # Sposób płatności kosztów transportu:
    # „DF” – określony przez kupującego i dostawcę
    # „PC” – opłacony z góry, obciążający klienta
    payment_method: str = ''


@dataclass
class LineDelivery:
    delivery_location_number: str = ''        # ILN lokalizacji dostawy (sklepu)
    tax_id: str = ''                          # NIP lokalizacji dostawy (sklepu)
    delivery_date: date = date.today()              # Data dostawy
    despatch_number: str = ''                 # Numer dostawy
    despatch_date: date = date.today()              # Data dokumentu dostawy
    despatch_advice_number: str = ''          # Numer awiza wysyłki
    ship_from_location_number: str = ''       # ILN Punktu wysyłki
    name: str = ''                            # Nazwa Punktu Dostawy
    street_and_number: str = ''               # Ulica i numer
    city_name: str = ''                       # Miasto
    postal_code: str = ''                     # Kod pocztowy
    country: str = ''                         # Kraj (kodowane ISO 3166)
    delivery_terms: DeliveryTerms = DeliveryTerms()


@dataclass
class LineReturns:
    returns_notice_number: str = ''           # Numer zawiadomienia o zwrotach
    returns_notice_date: date = date.today()        # Data zawiadomienia o zwrotach


@dataclass
class Allowance:
    percentage: str = ''                      # Oprocentowanie obniżki
    allowance_amount: float = 0              # Wartość obniżki
    original_amount: float = 0               # Wartość sprzed obniżki


@dataclass
class LineAllowances:
    allowance: Allowance = Allowance()


@dataclass
class Charge:
    percentage: str = ''                      # Procent obciążenia
    charge_amount: float = 0                 # Wartość obciążenia
    original_amount: float = 0               # Wartość sprzed obciążenia
    special_service: str = ''                 # Kod identyfikujący usługę specjalną, np. TX = opłata cukrowa
    special_service_description: str = ''     # Opis usługi specjalnej


@dataclass
class LineCharges:
    charge: Charge = Charge()


@dataclass
class LineMeasurements:
    net_weight: float = 0                    # Waga netto


@dataclass
class Line:
    line_item: LineItem = LineItem()
    line_order: LineOrder = LineOrder()
    line_reference: LineReference = LineReference()
    line_delivery: LineDelivery = LineDelivery()
    line_returns: LineReturns = LineReturns()
    line_allowances: LineAllowances = LineAllowances()
    line_charges: LineCharges = LineCharges()
    line_measurements: LineMeasurements = LineMeasurements()


@dataclass
class InvoiceLines:
    line: Line = Line()


@dataclass
class TaxSummaryLine:
    tax_rate: float = 0                      # Stawka VAT
    # Kod stawki:
    # "E" (exempt) - zwolniony
    # "S" (standard) - inna, wyrażona liczba ("standardowa")
    # "NA" (not applicable) – nie podlega "AE" (reverse charge) - odwrotne obciążenie
    tax_category_code: str = ''
    tax_amount: float = 0                    # Suma VAT dla danej stawki
    taxable_basis: float = 0                 # Kwota podlegająca opodatkowaniu objęta daną stawką
    taxable_amount: float = 0                # Kwota netto objęta daną stawką
    gross_amount: float = 0                  # Kwota brutto objęta daną stawką
    previous_tax_rate: float = 0             # Stawka VAT przed korektą
    # Kod stawki:
    # "E" (exempt) - zwolniony
    # "S" (standard) - inna, wyrażona liczba ("standardowa")
    # "NA" (not applicable) – nie podlega "AE" (reverse charge) - odwrotne obciążenie
    previous_tax_category_code: str = ''
    previous_tax_amount: float = 0            # Suma VAT dla danej stawki przed korektą
    previous_taxable_amount: float = 0        # Kwota netto objęta daną stawką przed korektą
    # Suma VAT dla danej stawki – różnica pomiędzy wartością prawidłową, a korygowaną
    correction_tax_amount: float = 0
    # Kwota netto objęta daną stawką – różnica pomiędzy wartością prawidłową, a korygowaną
    correction_taxable_amount: float = 0
    # Kwota brutto objęta daną stawką – różnica pomiędzy wartością prawidłową, a korygowaną
    correction_gross_amount: float = 0


class TaxSummary:
    tax_summary_line: list[TaxSummaryLine] = []
    # def __init__(self, tax_summary_line: TaxSummaryLine = field(default_factory=[TaxSummaryLine()])):
    #     self.tax_summary_line = [tax_summary_line]


@dataclass
class DepositSummary:
    total_net_amount: float = 0               # Suma netto po doliczeniu kwoty za opakowania kaucjonowane
    total_gross_amount: float = 0             # Suma brutto po doliczeniu kwoty za opakowania kaucjonowane
    # Suma netto po doliczeniu kwoty za opakowania kaucjonowane przed korektą
    previous_total_net_amount: float = 0
    # Suma brutto po doliczeniu kwoty za opakowania kaucjonowane przed korektą
    previous_total_gross_amount: float = 0
    # Suma netto po doliczeniu kwoty za opakowania kaucjonowane – różnica pomiędzy wartością prawidłową, a korygowaną
    correction_total_net_amount: float = 0
    # Suma brutto po doliczeniu kwoty za opakowania kaucjonowane – różnica pomiędzy wartością prawidłową, a korygowaną
    correction_total_gross_amount: float = 0


@dataclass
class Charge:
    charge_number: str = ''                    # Numer obciążenia
    charge_amount: float = 0                  # Wartość obciążenia
    special_service: str = ''                  # Kod identyfikujący usługę specjalną, np. TX = opłata cukrowa
    special_service_description: str = ''      # Opis usługi specjalnej


@dataclass
class ChargeSummary:
    charge: Charge = Charge()


@dataclass
class InvoiceSummary:
    total_lines: int = 0                         # Ilość linii
    total_net_amount: float = 0                  # Suma netto
    total_taxable_basis: float = 0               # Suma podlegająca opodatkowaniu
    total_tax_amount: float = 0               # Suma VAT
    total_gross_amount: float = 0             # Suma brutto
    total_deposit_amount: float = 0           # Suma kaucji za towary kaucjonowane
    total_discount_amount: float = 0          # Wartość kwoty należnego upustu
    total_net_amout_without_charges: float = 0       # Suma netto bez dodatkowej opłaty
    previous_total_net_amount: float = 0      # Suma netto przed korektą
    previous_total_taxable_basis: float = 0   # Suma podlegająca opodatkowaniu przed korektą
    previous_total_tax_amount: float = 0      # Suma VAT przed korektą
    previous_total_gross_amount: float = 0    # Suma brutto przed korektą
    previous_total_deposit_amount: float = 0  # Suma kaucji za towary kaucjonowane przed korektą
    correction_total_net_amount: float = 0    # Suma netto.Różnica pomiędzy wartością prawidłową, a korygowaną
    # Suma podlegająca opodatkowaniu – różnica pomiędzy wartością prawidłową, a korygowaną
    correction_total_taxable_basis: float = 0
    correction_total_tax_amount: float = 0    # Suma VAT – różnica pomiędzy wartością prawidłową, a korygowaną
    correction_total_gross_amount: float = 0  # Suma brutto.Różnica pomiędzy wartością prawidłową a korygowaną
    # Suma kaucji za towary kaucjonowane – różnica pomiędzy wartością prawidłową, a korygowaną
    correction_total_deposit_amount: float = 0
    gross_amount_in_words: str = ''            # Suma brutto słownie
    tax_summary: TaxSummary = TaxSummary()
    deposit_summary: DepositSummary = DepositSummary()
    charge_summary: ChargeSummary = ChargeSummary()


class DocumentInvoice:
    invoice_header: InvoiceHeader = InvoiceHeader()
    invoice_parties: InvoiceParties = InvoiceParties()
    invoice_lines: list[InvoiceLines] = []
    invoice_summary: InvoiceSummary = InvoiceSummary()

    def add(self, item):
        return self.invoice_lines.append(item)

