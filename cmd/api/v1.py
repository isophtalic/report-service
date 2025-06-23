from fastapi import APIRouter, responses
from app.models.report import Report
from app.services.report_generator import ReportGenerator
from settings.settings import Settings


router = APIRouter()

@router.post("/gen_report")
def submit_report(data: Report):
    generator =  ReportGenerator(Settings.TemplateDir + "/weekly_template.docx").set_type_report(data.type)
    buffer = generator.docx_generate_buffer(data.model_dump())
    return responses.StreamingResponse(
        content=buffer,
        media_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        headers={"Content-Disposition": "attachment; filename=sales_report.docx"}
    )


@router.get("/")
def get_report():
    return {
        "status": "ok",
    }