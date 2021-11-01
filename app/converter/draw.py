import xml.etree.ElementTree as ET


def draw_xml(filename, xml_document):
    document_invoice = ET.Element('Document-Invoice')

    invoice_header = ET.SubElement(document_invoice, 'Invoice-Header')
    ET.SubElement(invoice_header, 'InvoiceNumber').text = \
        str(xml_document.invoice_header.invoice_number)
    ET.SubElement(invoice_header, 'InvoiceDate').text = \
        str(xml_document.invoice_header.invoice_date.isoformat())
    ET.SubElement(invoice_header, 'SalesDate').text = \
        str(xml_document.invoice_header.sales_date.isoformat())
    ET.SubElement(invoice_header, 'InvoiceCurrency').text = \
        'PLN'
    ET.SubElement(invoice_header, 'InvoicePaymentDueDate').text = \
        str(xml_document.invoice_header.invoice_payment_due_date.isoformat())
    ET.SubElement(invoice_header, 'InvoicePaymentTerms').text = \
        str((xml_document.invoice_header.invoice_payment_due_date - xml_document.invoice_header.sales_date).days)
    ET.SubElement(invoice_header, 'DocumentFunctionCode').text = \
        'O'
    ET.SubElement(invoice_header, 'Remarks').text = \
        str(xml_document.invoice_header.remarks)

    order = ET.SubElement(invoice_header, 'Order')

    ET.SubElement(order, 'BuyerOrderNumber').text = \
        str(xml_document.invoice_header.order.buyer_order_number)
    ET.SubElement(order, 'BuyerOrderDate').text = \
        str(xml_document.invoice_header.order.buyer_order_date.isoformat())

    delivery = ET.SubElement(invoice_header, 'Delivery')

    ET.SubElement(delivery, 'DeliveryLocationNumber').text = \
        str(xml_document.invoice_header.delivery.delivery_location_number)
    ET.SubElement(delivery, 'DeliveryDate').text = \
        str(xml_document.invoice_header.delivery.delivery_date.isoformat())
    ET.SubElement(delivery, 'DespatchNumber').text = \
        str(xml_document.invoice_header.delivery.despatch_number)
    ET.SubElement(delivery, 'DespatchAdviceNumber').text = \
        str(xml_document.invoice_header.delivery.despatch_advice_number)

    invoice_parties = ET.SubElement(document_invoice, 'Invoice-Parties')

    buyer = ET.SubElement(invoice_parties, 'Buyer')

    ET.SubElement(buyer, 'ILN').text = \
        str(xml_document.invoice_parties.buyer.iln)
    ET.SubElement(buyer, 'TaxID').text = \
        str(xml_document.invoice_parties.buyer.tax_id)
    ET.SubElement(buyer, 'AccountNumber').text = \
        str(xml_document.invoice_parties.buyer.account_number)
    ET.SubElement(buyer, 'Name').text = str(xml_document.invoice_parties.buyer.name)
    ET.SubElement(buyer, 'StreetAndNumber').text = \
        str(xml_document.invoice_parties.buyer.street_and_number)
    ET.SubElement(buyer, 'CityName').text = \
        str(xml_document.invoice_parties.buyer.city_name)
    ET.SubElement(buyer, 'PostalCode').text = \
        str(xml_document.invoice_parties.buyer.postal_code)
    ET.SubElement(buyer, 'Country').text = \
        str(xml_document.invoice_parties.buyer.country)

    payer = ET.SubElement(invoice_parties, 'Payer')

    ET.SubElement(payer, 'ILN').text = \
        str(xml_document.invoice_parties.buyer.iln)
    ET.SubElement(payer, 'TaxID') \
        .text = str(xml_document.invoice_parties.buyer.tax_id)
    ET.SubElement(payer, 'AccountNumber').text = \
        str(xml_document.invoice_parties.buyer.account_number)
    ET.SubElement(payer, 'Name').text = \
        str(xml_document.invoice_parties.buyer.name)
    ET.SubElement(payer, 'StreetAndNumber').text = \
        str(xml_document.invoice_parties.buyer.street_and_number)
    ET.SubElement(payer, 'CityName').text = \
        str(xml_document.invoice_parties.buyer.city_name)
    ET.SubElement(payer, 'PostalCode').text = \
        str(xml_document.invoice_parties.buyer.postal_code)
    ET.SubElement(payer, 'Country').text = \
        str(xml_document.invoice_parties.buyer.country)

    invoicee = ET.SubElement(invoice_parties, 'Invoicee')

    ET.SubElement(invoicee, 'ILN').text = \
        str(xml_document.invoice_parties.buyer.iln)
    ET.SubElement(invoicee, 'TaxID').text = \
        str(xml_document.invoice_parties.buyer.tax_id)
    ET.SubElement(invoicee, 'AccountNumber').text = \
        str(xml_document.invoice_parties.buyer.account_number)
    ET.SubElement(invoicee, 'Name').text = \
        str(xml_document.invoice_parties.buyer.name)
    ET.SubElement(invoicee, 'StreetAndNumber').text = \
        str(xml_document.invoice_parties.buyer.street_and_number)
    ET.SubElement(invoicee, 'CityName').text = \
        str(xml_document.invoice_parties.buyer.city_name)
    ET.SubElement(invoicee, 'PostalCode').text = \
        str(xml_document.invoice_parties.buyer.postal_code)
    ET.SubElement(invoicee, 'Country').text = \
        str(xml_document.invoice_parties.buyer.country)

    seller = ET.SubElement(invoice_parties, 'Seller')

    ET.SubElement(seller, 'ILN').text = \
        str(xml_document.invoice_parties.seller.iln)
    ET.SubElement(seller, 'TaxID').text = \
        str(xml_document.invoice_parties.seller.tax_id)
    ET.SubElement(seller, 'AccountNumber').text = \
        str(xml_document.invoice_parties.seller.account_number)
    ET.SubElement(seller, 'CodeByBuyer').text = \
        str(xml_document.invoice_parties.seller.code_by_buyer)
    ET.SubElement(seller, 'Name').text = \
        str(xml_document.invoice_parties.seller.name)
    ET.SubElement(seller, 'StreetAndNumber').text = \
        str(xml_document.invoice_parties.seller.street_and_number)
    ET.SubElement(seller, 'CityName').text = \
        str(xml_document.invoice_parties.seller.city_name)
    ET.SubElement(seller, 'PostalCode').text = \
        str(xml_document.invoice_parties.seller.postal_code)
    ET.SubElement(seller, 'Country').text = \
        str(xml_document.invoice_parties.seller.country)
    ET.SubElement(seller, 'UtilizationRegisterNumber').text = \
        str(xml_document.invoice_parties.seller.utilization_register_number)
    ET.SubElement(seller, 'CourtAndCapitalInformation').text = \
        str(xml_document.invoice_parties.seller.court_and_capital_information)

    payee = ET.SubElement(invoice_parties, 'Payee')

    ET.SubElement(payee, 'ILN').text = \
        str(xml_document.invoice_parties.seller.iln)
    ET.SubElement(payee, 'TaxID').text = \
        str(xml_document.invoice_parties.seller.tax_id)
    ET.SubElement(payee, 'AccountNumber').text = \
        str(xml_document.invoice_parties.seller.account_number)
    ET.SubElement(payee, 'Name').text = \
        str(xml_document.invoice_parties.seller.name)
    ET.SubElement(payee, 'StreetAndNumber').text = \
        str(xml_document.invoice_parties.seller.street_and_number)
    ET.SubElement(payee, 'CityName').text = \
        str(xml_document.invoice_parties.seller.city_name)
    ET.SubElement(payee, 'PostalCode').text = \
        str(xml_document.invoice_parties.seller.postal_code)
    ET.SubElement(payee, 'Country').text = \
        str(xml_document.invoice_parties.seller.country)

    seller_headquarters = ET.SubElement(invoice_parties, 'SellerHeadquarters')

    ET.SubElement(seller_headquarters, 'ILN').text = \
        str(xml_document.invoice_parties.seller.iln)
    ET.SubElement(seller_headquarters, 'TaxID').text = \
        str(xml_document.invoice_parties.seller.tax_id)
    ET.SubElement(seller_headquarters, 'AccountNumber').text = \
        str(xml_document.invoice_parties.seller.account_number)
    ET.SubElement(seller_headquarters, 'Name').text = \
        str(xml_document.invoice_parties.seller.name)
    ET.SubElement(seller_headquarters, 'StreetAndNumber').text = \
        str(xml_document.invoice_parties.seller.street_and_number)
    ET.SubElement(seller_headquarters, 'CityName').text = \
        str(xml_document.invoice_parties.seller.city_name)
    ET.SubElement(seller_headquarters, 'PostalCode').text = \
        str(xml_document.invoice_parties.seller.postal_code)
    ET.SubElement(seller_headquarters, 'Country').text = \
        str(xml_document.invoice_parties.seller.country)

    invoice_lines = ET.SubElement(document_invoice, 'Invoice-Lines')

    for line_of_invoice in xml_document.invoice_lines:
        line = ET.SubElement(invoice_lines, 'Line')

        line_item = ET.SubElement(line, 'Line-Item')

        ET.SubElement(line_item, 'LineNumber').text = \
            str(line_of_invoice.line_item.line_number)
        ET.SubElement(line_item, 'EAN').text = \
            str(line_of_invoice.line_item.ean)
        ET.SubElement(line_item, 'BuyerItemCode').text = \
            str(line_of_invoice.line_item.buyer_item_code)
        ET.SubElement(line_item, 'SupplierItemCode').text = \
            str(line_of_invoice.line_item.supplier_item_code)
        ET.SubElement(line_item, 'ItemDescription').text = \
            str(line_of_invoice.line_item.item_description)
        ET.SubElement(line_item, 'ItemType').text = \
            str(line_of_invoice.line_item.item_type)
        ET.SubElement(line_item, 'InvoiceQuantity').text = \
            str(line_of_invoice.line_item.invoice_quantity)
        ET.SubElement(line_item, 'UnitOfMeasure').text = \
            str(line_of_invoice.line_item.unit_of_measure)
        ET.SubElement(line_item, 'InvoiceUnitPacksize').text = \
            str(line_of_invoice.line_item.invoice_unit_packsize)
        ET.SubElement(line_item, 'PackItemUnitOfMeasure').text = \
            str(line_of_invoice.line_item.pack_item_unit_of_measure)
        ET.SubElement(line_item, 'InvoiceUnitNetPrice').text = \
            str(line_of_invoice.line_item.invoice_unit_net_price)
        ET.SubElement(line_item, 'TaxRate').text = \
            str(line_of_invoice.line_item.tax_rate)
        ET.SubElement(line_item, 'TaxCategoryCode').text = \
            str(line_of_invoice.line_item.tax_category_code)

        tax_reference = ET.SubElement(line_item, 'TaxReference')

        ET.SubElement(tax_reference, 'ReferenceType').text = \
            str(line_of_invoice.line_item.tax_reference.reference_type)
        ET.SubElement(tax_reference, 'ReferenceNumber').text = \
            str(line_of_invoice.line_item.tax_reference.reference_number)

        ET.SubElement(line_item, 'TaxAmount').text = \
            str(line_of_invoice.line_item.tax_amount)
        ET.SubElement(line_item, 'NetAmount').text = \
            str(line_of_invoice.line_item.net_amount)

        line_order = ET.SubElement(line, 'Line-Order')

        ET.SubElement(line_order, 'BuyerOrderNumber').text = \
            str(line_of_invoice.line_order.buyer_order_number)
        ET.SubElement(line_order, 'BuyerOrderDate').text = \
            str(line_of_invoice.line_order.buyer_order_date.isoformat())

        line_delivery = ET.SubElement(line, 'Line-Delivery')

        ET.SubElement(line_delivery, 'DeliveryLocationNumber').text = \
            str(line_of_invoice.line_delivery.delivery_location_number)
        ET.SubElement(line_delivery, 'DeliveryDate').text = \
            str(line_of_invoice.line_delivery.delivery_date.isoformat())
        ET.SubElement(line_delivery, 'DespatchNumber').text = \
            str(line_of_invoice.line_delivery.despatch_number)
        ET.SubElement(line_delivery, 'DespatchAdviceNumber').text = \
            str(line_of_invoice.line_delivery.despatch_advice_number)

    invoice_summary = ET.SubElement(document_invoice, 'Invoice-Summary')

    ET.SubElement(invoice_summary, 'TotalLines').text = \
        str(len(xml_document.invoice_lines))
    ET.SubElement(invoice_summary, 'TotalNetAmount').text = \
        str(xml_document.invoice_summary.total_net_amount)
    ET.SubElement(invoice_summary, 'TotalTaxableBasis').text = \
        str(xml_document.invoice_summary.total_taxable_basis)
    ET.SubElement(invoice_summary, 'TotalTaxAmount').text = \
        str(xml_document.invoice_summary.total_tax_amount)
    ET.SubElement(invoice_summary, 'TotalGrossAmount').text = \
        str(xml_document.invoice_summary.total_gross_amount)
    ET.SubElement(invoice_summary, 'GrossAmountInWords').text = \
        str(xml_document.invoice_summary.gross_amount_in_words)

    tax_summary = ET.SubElement(invoice_summary, 'Tax-Summary')

    for tax_sumary_row in xml_document.invoice_summary.tax_summary.tax_summary_line:
        tax_summary_line = ET.SubElement(tax_summary, 'Tax-Summary-Line')
        ET.SubElement(tax_summary_line, 'TaxRate').text = \
            str(tax_sumary_row.tax_rate)
        ET.SubElement(tax_summary_line, 'TaxCategoryCode').text = \
            str(tax_sumary_row.tax_category_code)
        ET.SubElement(tax_summary_line, 'TaxAmount').text = \
            str(tax_sumary_row.tax_amount)
        ET.SubElement(tax_summary_line, 'TaxableBasis').text = \
            str(tax_sumary_row.taxable_basis)
        ET.SubElement(tax_summary_line, 'TaxableAmount').text = \
            str(tax_sumary_row.taxable_amount)
        ET.SubElement(tax_summary_line, 'GrossAmount').text = \
            str(tax_sumary_row.gross_amount)

    tree = ET.ElementTree(document_invoice)

    tree.write(filename, encoding='UTF-8', short_empty_elements=False)
    print(f'Operacja zakończyła się sukcesem.\nUtworzono plik {filename}.')
