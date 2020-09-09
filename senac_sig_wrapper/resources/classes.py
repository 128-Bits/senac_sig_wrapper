from senac_sig_wrapper.resources import BaseResource


_CLASSES_BASE_URL = "/api/turma"


class Classes(BaseResource):
    """Administration resource
    Use this resource to access the API routes related to the
    unit administration data.
    """

    CLASS_LIST_URL = f"{_CLASSES_BASE_URL}"

    def get_list(self, params=None):
        response = self.request.get(self.CLASS_LIST_URL, params=params)
        return response

    def get_single_class(self, class_id=None):
        if not class_id:
            raise ValueError("Precisa informar o identificador da turma")
        return self.request.get(f"{_CLASSES_BASE_URL}/{class_id}")

    def get_open_spaces(self, class_id=None):
        if not class_id:
            raise ValueError("Precisa informar o identificador da turma")
        return self.request.get(
            f"{_CLASSES_BASE_URL}/vagas-disponiveis/{class_id}"
        )
