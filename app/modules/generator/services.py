from app.modules.generator.repositories import GeneratorRepository
from core.services.BaseService import BaseService


class GeneratorService(BaseService):
    def __init__(self):
        super().__init__(GeneratorRepository())
