from typing import Any, AnyStr, Dict, List, Optional, Union
import json
from senac_sig_wrapper.resources import BaseResource


class Classes(BaseResource):
    """Administration resource
    Use this resource to access the API routes related to the
    unit administration data.
    """

    def get_single_class(self, class_id=None):
        if not class_id:
            raise ValueError("Precisa informar o identificador da turma")
        return self.request.get(f"/api/turma/{class_id}")
    
    def get_open_spaces(self, class_id=None):
        if not class_id:
            raise ValueError("Precisa informar o identificador da turma")
        return self.request.get(f"/api/turma/vagas-disponiveis/{class_id}")
    