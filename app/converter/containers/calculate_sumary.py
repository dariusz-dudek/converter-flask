from app.converter.containers.xml_template_classes_full_classes import TaxSummaryLine


class Sumary:
    @staticmethod
    def calculate_sumary(xml_document):
        for row in xml_document.invoice_lines:
            if row.line_item.tax_rate not in \
                    [float(vat.tax_rate) for vat in xml_document.invoice_summary.tax_summary.tax_summary_line]:
                xml_document.invoice_summary.tax_summary.tax_summary_line.\
                    append(TaxSummaryLine(tax_rate=float(row.line_item.tax_rate), tax_category_code='S'))
            for vat_summary in xml_document.invoice_summary.tax_summary.tax_summary_line:
                if vat_summary.tax_rate == row.line_item.tax_rate:
                    vat_summary.taxable_basis += row.line_item.net_amount
        for tax_sumary_line in xml_document.invoice_summary.tax_summary.tax_summary_line:
            tax_sumary_line.taxable_amount = tax_sumary_line.taxable_basis
            tax_sumary_line.tax_amount = round(tax_sumary_line.taxable_basis * (tax_sumary_line.tax_rate / 100), 2)
            tax_sumary_line.gross_amount = round(tax_sumary_line.tax_amount + tax_sumary_line.taxable_basis, 2)
            xml_document.invoice_summary.total_taxable_basis += tax_sumary_line.taxable_basis
            xml_document.invoice_summary.total_net_amount += tax_sumary_line.taxable_amount
            xml_document.invoice_summary.total_tax_amount += tax_sumary_line.tax_amount
        xml_document.invoice_summary.total_gross_amount = \
            float(xml_document.invoice_summary.total_taxable_basis)\
            + float(xml_document.invoice_summary.total_tax_amount)
