from typing import Annotated, List

from fastapi import APIRouter, Path, Query

from server.schemas.project_schema import NewProjectRequest, ProjectResponse, ProjectRequest

from server.controller import ProjectsController

from server.exceptions import InternalServerError, NotFound

router = APIRouter(prefix='/projects')
router.responses = {
    500: InternalServerError.as_dict(),
}
controller = ProjectsController()


@router.post(
    '',
    status_code=201,
    responses={
        201: {'description': 'Proyecto creado'},
    },
    description='Crea un proyecto nuevo con los campos pasados por Body Params. Falla si faltan alguno de los campos obligatorios'
)  # POST /projects
async def create(new_project: NewProjectRequest) -> ProjectResponse:
    return controller.create(new_project)


@router.get(
    '',
    status_code=200,
    responses={
        200: {'description': 'Retorna un listado de proyectos'},
    },
    description='Esta ruta retorna todo el listado de los proyectos, si no tienen nada retorna una lista vacia'
)  # Get /projects -> Calculo del offset es n*limit
async def get_list(limit: Annotated[int, Query(ge=1, le=1000)] = 10, offset: Annotated[int, Query(ge=0)] = 0) -> List[ProjectResponse]:
    return controller.get_list(limit, offset)


@router.get(
    '/{id}',
    status_code=200,
    responses={
        200: {'description': 'Proyecto encontrado'},
        404: NotFound.as_dict(),
        422: {'description': 'ID no es un entero valido'},
    },
    description='Retorna un proyecto por ID. Falla si el ID no existe'
)  # GET /projects/{id}
async def get_by_id(id: Annotated[int, Path(ge=1)]) -> ProjectResponse:
    return controller.get_by_id(id)


@router.patch(
    '/{id}',
    status_code=200,
    responses={
        200: {'description': 'Proyecto actualizado'},
        404: NotFound.as_dict(),
        422: {'description': 'ID no es un entero valido'},
    },
    description='Actualiza un proyecto con los campos pasados por Body Param. ID no es un entero valido'
)  # PATCH /projects/{id}
async def get_by_id(id: Annotated[int, Path(ge=1)], project: ProjectRequest) -> ProjectResponse:
    return controller.update(id, project)


@router.delete(
    '/{id}',
    status_code=204,
    responses={
        204: {'description': 'Proyecto eliminado'},
        404: NotFound.as_dict(),
        422: {'description': 'ID no es un entero valido'},
    },
    description='Elimina un proyecto con el ID pasado por Body Params. Falla si el ID no existe'
)  # DELETE /projects/{id}
async def get_by_id(id: Annotated[int, Path(ge=1)]) -> None:
    controller.delete(id)
