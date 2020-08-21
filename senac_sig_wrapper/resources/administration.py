from typing import Any, AnyStr, Dict, List, Optional, Union
import json
from senac_sig_wrapper.resources import BaseResource


class Administration(BaseResource):
    """Administration resource
    Use this resource to access the API routes related to the
    unit administration data.
    """

    def get_cities(self):
        response = self.request.get("/api/cidade")
        return response

    def get_person(self, param_cpf: str = ""):
        response = self.request.get(f"/api/pessoa-fisica/{param_cpf}")
        return response

    def get_business(self, param_cnpj: str = ""):
        response = self.request.get(f"/api/pessoa-juridica/{param_cnpj}")
        return response

    def get_op_unit(self, complete: bool = False):
        url = "/api/unidade-operativa"
        if complete:
            url = f"{url}/lista-completa"
        response = self.request.get(url)
        return response
