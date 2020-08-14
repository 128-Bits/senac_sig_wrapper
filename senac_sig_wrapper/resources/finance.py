from typing import Any, Dict, Union
import json
from senac_sig_wrapper.resources import BaseResource


class Finance(BaseResource):
    """Finance resource
    Use this resource to access the API routes related to the
    unit finances data.
    """
    voucher_search_params = [
        "VigenciaInicial",
        "VigenciaFinal",
        "Estado",
        "Situacao"
    ]

    def get_voucher(self, params: Union[Dict[str, Any], None] = None):
        response = self.request.get(
            "/api/voucher/voucher-por-vigencia", 
            params=params
        )
        return response.json()
    

