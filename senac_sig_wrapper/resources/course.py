"""
GET
/api/eixo-tecnologico
Retorna uma lista simples de EixoTecnologico com Id e Nome para compor filtros.

GET
/api/modalidade
Retorna uma lista simples de Modalidades com Id e Nome.

GET
/api/plano-curso/para-divulgacao
Listagem Planos de Cursos do Regional para Divulgação Externa.

GET
/api/plano-curso/identificacao/
Detalhe de identificação de um Plano de Curso.

GET
/api/plano-curso/informacoes/
Detalhe de informações de um Plano de Curso.

GET
/api/plano-curso/requisitos/
Listagem de requisitos de um Plano de Curso.

GET
/api/plano-curso/organizacao-curricular/
Listagem da organização curricular de um Plano de Curso.

GET
/api/plano-curso/autorizacao/
Detalhe da autorização de um Plano de Curso.

GET
/api/plano-curso/material-pedagogico/
Detalhe do material pedagógio de um Plano de Curso.

GET
/api/plano-curso/ficha-tecnica/
Detalhe da ficha técnica de um Plano de Curso.

GET
/api/segmento
Retorna uma lista simples de Segmentos com Id, Nome e Situação.

GET
/api/unidade-curricular/detalhe/{unidadeCurricularId}
Detalhe da Unidade Curricular.
"""
from typing import Any, Dict, Union
from senac_sig_wrapper.resources import BaseResource


_CPBASE_URL = "/api/plano-curso"


class Course(BaseResource):
    """Course resource
    Use this resource to access the API routes related to the
    unit course data.
    """
    
    TECH_AXIS_URL = "/api/eixo-tecnologico"
    MODALITY_URL = "/api/modalidade"
    COURSES_FOR_PUBLIC_URL = "para-divulgacao"
    COURSE_PLAN_INFO_URL = f"{_CPBASE_URL}/identificacao/"
    COURSE_PLAN_DETAILS_URL = f"{_CPBASE_URL}/informacoes/"
    COURSE_PLAN_REQUIREMENTS_URL = f"{_CPBASE_URL}/requirements/"
    COURSE_PLAN_CURR_ORG_URL = f"{_CPBASE_URL}/organizacao-curricular/"
    COURSE_PLAN_AUTHORIZATION_URL = f"{_CPBASE_URL}/autorizacao/"
    COURSE_PLAN_MATERIAL_URL = f"{_CPBASE_URL}/material-pedagogico/"
    COURSE_PLAN_DATASHEET_URL = f"{_CPBASE_URL}/ficha-tecnica/"
    COURSE_SEGMENT_URL = "/api/segmento"
    COURSE_CURR_UNIT_DETAIL_URL = "/api/unidade-curricular/detalhe/"

    def get_segments(self):
        response = self.request.get(self.COURSE_SEGMENT_URL)
        return response.json





