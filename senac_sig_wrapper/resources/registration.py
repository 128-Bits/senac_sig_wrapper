from typing import Any, Dict, Union
from senac_sig_wrapper.resources import BaseResource


class Registration(BaseResource):
    """Registration resource
    Use this resource to access the API routes related to the
    unit registration data.
    """

    DEMAND_TYPE_URL = "/api/demanda/tipos-de-demanda"
    COMMUNICATION_CHANNELS_URL = "/api/demanda/canais-de-comunicacao"
    STUDENTS_WITH_CLASS_URL = "/api/matricula/alunos-com-turma"
    STUDENTS_TO_INTEGRATE_URL = (
        "/api/matricula/alunos-para-integracao-office-365"
    )
    SEND_DEMAND_URL = "/api/demanda"

    REQUIRED_FIELDS = (
        "tipoDeRecursoId",
        "tipoDePessoaDaDemanda",
        "canalId",
        "numeroDoDocumento",
        "nome",
        "codigoDeArea",
        "numeroDoTelefone",
    )

    def get_demand_type(self):
        response = self.request.get(self.DEMAND_TYPE_URL)
        return response

    def get_communication_channels(self):
        response = self.request.get(self.COMMUNICATION_CHANNELS_URL)
        return response

    def send_demand(self, data: Union[Dict[str, Any], None] = None):
        if not data:
            raise ValueError(
                (
                    "Para registrar uma demanda preciso dos "
                    f"seguintes campos: {', '.join(self.REQUIRED_FIELDS)}"
                )
            )
        absent_fields = [
            field for field in self.REQUIRED_FIELDS if field not in data.keys()
        ]
        if absent_fields:
            raise ValueError(
                (
                    "Alguns campos obrigatórios não foram informados: "
                    f"{', '.join(absent_fields)}"
                )
            )
        response = self.request.post(self.SEND_DEMAND_URL, data)
        return response

    def get_students_with_class(self):
        response = self.request.get(self.STUDENTS_WITH_CLASS_URL)
        return response

    def get_students_to_integrate(self):
        response = self.request.get(self.STUDENTS_TO_INTEGRATE_URL)
        return response

