import os


class Settings:
    TemplateDir = os.environ.get("TEMPLATE_DIR", default=".\\templates")
    TemporaryFolder = os.environ.get("TEMP_DIR", default=".\\temp")
    ComponentDir = ".\\components"
