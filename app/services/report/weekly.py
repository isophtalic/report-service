from docxtpl import DocxTemplate
from app.services.report.report import Report
from app.utils.time import format_timestamp
from datetime import datetime
import os
from settings.settings import Settings
from uuid import uuid4
from jinja2 import Template
import aspose.words as aw


class WeeklyReport(Report):
    def __init__(self, docx: DocxTemplate):
        self.__docx = docx

    def process(self, data: dict) -> dict:
        data["date_now"] = datetime.now().strftime("%m-%Y")
        data["organization"]["execution_time"]["start_time"] = format_timestamp(data["organization"]["execution_time"]["start"])
        data["organization"]["execution_time"]["end_time"] = format_timestamp(data["organization"]["execution_time"]["end"])
        data["overview"]["overview"]["density"] = overview_overview(self.__docx, data)
        data["overview"]["chart"]["chart_credential_domain"] = chart_credential(self.__docx, data["overview"]["chart"]["dl_credential"])
        # {{p overview.chart.chart_credential_domain }}
        # {{p overview.chart.chart_credential_account }}
        # {{p overview.chart.chart_vulnerability }}
        # {{p overview.chart.chart_document }}
        return  data



def overview_overview(docx: DocxTemplate, data: dict) -> list:
    list_items = []
    overviews = data["overview"]["overview"]
    for key, value in overviews.items():
        if key != "density":
            d = data["overview"]["overview"][key]
            d["name"] = get_name_overview_item(key)
            list_items.append(overview_item(docx, data["overview"]["overview"][key]))

    return list_items

def get_name_overview_item(key: str):
    match key:
        case "risk":
            return "Nguy cơ"
        case "dl-credential":
            return "Lộ lọt tài khoản"
        case "dl-credit-card":
            return "Lộ lọt thẻ tín dụng"
        case "dl-document":
            return "Lộ lọt tài liệu"
        case "brand-abuse":
            return "Lạm dụng thương hiệu"
        case "campaign-botnet":
            return "Botnet"
        case "investigate":
            return "Yêu cầu điều tra"
        case "campaign-campaign":
            return "Chiến dịch tấn công"
        case "open-port":
            return "Cổng dịch vụ đang mở"
    return None


def overview_item(docx: DocxTemplate, data: dict):
    temp_file_path = os.path.join(Settings.TemporaryFolder, f"{str(uuid4())}.docx")
    temp_docx = DocxTemplate(os.path.join(Settings.ComponentDir, "overview_item.docx"))
    temp_docx.render(data)
    temp_docx.save(temp_file_path)
    return docx.new_subdoc(temp_file_path)


def chart_credential(docx: DocxTemplate, data: dict):
    xml_template_path = os.path.join(Settings.ComponentDir, "column_chart_credential.xml")
    xml_template_context = None
    with open(xml_template_path, "r", encoding='utf-8') as f:
        xml_template_context = f.read()

    if xml_template_context is None:
        raise Exception(f"Something went wrong with when reading {xml_template_path}")

    template = Template(xml_template_context)
    applied_template = template.render(data)

    chart_file_xml = os.path.join(Settings.TemporaryFolder, f"{str(uuid4())}.xml")
    with open(chart_file_xml, "w", encoding='utf-8') as file:
        file.write(applied_template)

    chart_file_docx = os.path.join(Settings.TemporaryFolder, f"{str(uuid4())}.docx")
    chart_doc = aw.Document(chart_file_xml)
    chart_doc.save(chart_file_docx)

    return docx.new_subdoc(chart_file_docx)

