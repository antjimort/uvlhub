from flamapy.core.models import VariabilityModel
from flamapy.metamodels.fm_metamodel.models import FeatureModel
from fm_generator.flamapy.metamodels.FMGenerator.operations.generate_models import (
    generate_single_model,
)
from fm_generator.flamapy.metamodels.FMGenerator.models.config import Params
from pathlib import Path
from flamapy.metamodels.fm_metamodel.transformations.uvl_writer import UVLWriter
from pathlib import Path
import os

class FmgeneratorModel(VariabilityModel):
    @staticmethod
    def get_extension() -> str:
        return "fm"

    params = Params()

    def __init__(self, params: Params = None) -> None:
        if params:
            self.params = params

    def generate_models(self, output_dir: str) -> list[FeatureModel]:
        """Genera los modelos en el directorio indicado y los devuelve como lista."""
        os.makedirs(output_dir, exist_ok=True)
        fms = [
            generate_single_model(self.params, i) for i in range(self.params.NUM_MODELS)
        ]
        for i, fm in enumerate(fms):
            output_file = Path(output_dir) / f"{self.params.NAME_PREFIX}{i}.uvl"
            UVLWriter(str(output_file), fm).transform()
            print(f"Modelo generado y exportado en: {output_file}")
        return fms
