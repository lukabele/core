from abc import ABC, abstractmethod
from typing import Any


class OperationRequest:
    pass  # Placeholder for real request data


class OperationResponse:
    pass  # Placeholder for real response data


class BaseManager(ABC):
    def execute(self, req: OperationRequest) -> OperationResponse:
        return self.do_execute(req)

    @abstractmethod
    def do_execute(self, req: OperationRequest) -> OperationResponse:
        pass


class UserManager(BaseManager):
    def do_execute(self, req: OperationRequest) -> OperationResponse:
        return OperationResponse()

    def addUser(self, info: Any):
        pass

    def exportData(self, format: str) -> str:
        return f"/path/to/export.{format}"


class ScheduleManager(BaseManager):
    def do_execute(self, req: OperationRequest) -> OperationResponse:
        return OperationResponse()

    def setSchedule(self, homeId: str, mode: str, cron: str):
        pass

    def getSchedule(self, homeId: str):
        return "*/5 * * * *"  # example cron string


class MultiHomeManager(BaseManager):
    def do_execute(self, req: OperationRequest) -> OperationResponse:
        return OperationResponse()

    def addHome(self, config: Any):
        pass

    def removeHome(self, homeId: str):
        pass


class ModeState(ABC):
    @abstractmethod
    def handleToggle(self):
        pass


class HomeState(ModeState):
    def handleToggle(self):
        print("Switching from Home mode")


class AwayState(ModeState):
    def handleToggle(self):
        print("Switching from Away mode")


class VacationState(ModeState):
    def handleToggle(self):
        print("Switching from Vacation mode")


class SleepingState(ModeState):
    def handleToggle(self):
        print("Switching from Sleeping mode")


class ModeManager(BaseManager):
    def __init__(self):
        self.state: ModeState = HomeState()

    def do_execute(self, req: OperationRequest) -> OperationResponse:
        return OperationResponse()

    def setMode(self, mode: str):
        if mode == "home":
            self.state = HomeState()
        elif mode == "away":
            self.state = AwayState()
        elif mode == "vacation":
            self.state = VacationState()
        elif mode == "sleeping":
            self.state = SleepingState()

    def getMode(self) -> str:
        return self.state.__class__.__name__
