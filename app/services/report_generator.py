from docxtpl import DocxTemplate
import io
from io import BytesIO

from app.constants.constant import ReportType
from app.services.report.weekly import WeeklyReport


class ReportGenerator:
    def __init__(self, template_path: str):
        self.template_path = template_path
        self.type_report = None
        self.__docx = None

    def set_type_report(self, type_report: str):
        self.type_report = type_report
        self.__docx = DocxTemplate(self.template_path)
        return self

    def processing(self, data: dict) -> dict | None:
        match self.type_report:
            case ReportType.Weekly:
                return WeeklyReport(self.__docx).process(data)
        return None

    def docx_generate_buffer(self, data: dict) -> BytesIO | None:
        buffer = io.BytesIO()

        data = self.processing(data)
        if data is None or self.__docx is None:
            return None

        self.__docx.render(data, autoescape=True)
        # self.__docx.save(buffer)
        self.__docx.save("temp_file.docx")

        buffer.seek(0)
        return buffer