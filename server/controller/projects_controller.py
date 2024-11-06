from typing import List

from server.schemas.project_schema import NewProjectRequest, ProjectResponse, ProjectRequest


class ProjectsController:
    def __init__(self):
        pass

    def create(self,  new_project: NewProjectRequest) -> ProjectResponse:
        pass

    def get_list(self, limit: int, offset: int) -> List[ProjectResponse]:
        pass

    def get_by_id(self, id: int) -> ProjectResponse:
        pass

    def update(self, id: int, new_data: ProjectRequest) -> ProjectResponse:
        pass

    def delete(self, id: int) -> None:
        pass
