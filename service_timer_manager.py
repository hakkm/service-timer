from timer import TimerManager
from service import ServiceManager

from dataclasses import dataclass


@dataclass(kw_only=True)
class ServiceTimerManager:
    # todo: manage directory when you put services and timers.
    # todo: what to do
    title: str = None

    service_filename: str = None
    service_description: str = None
    command_to_run: str

    timer_filename: str = None
    timer_description: str = None
    on_calendar: str

    def __post_init__(self):
        if self.title:
            self.service_filename = f"{self.title.replace(' ', '_')}.service"
            self.service_description = self.title
            self.timer_filename = f"{self.title.replace(' ', '_')}.timer"
            self.timer_description = self.title
        elif not (
            self.service_filename,
            self.service_description,
            self.timer_filename,
            self.timer_description,
        ):
            raise ValueError(
                "You must provide either a title or all service and timer attributes"
            )

    def schedule(self):
        self._create_service()
        self._create_timer()
        self.timer_manager.start_timer()

    def _create_service(self):
        self.service_manager = ServiceManager(
            filename=self.service_filename, 
            description=self.service_description, 
            command=self.command_to_run
        )
        self.service_manager.create_service_file()

    def _create_timer(self):
        self.timer_manager = TimerManager(
            filename=self.timer_filename,
            description=self.timer_description,
            on_calendar=self.on_calendar,
            service_manager=self.service_manager,
        )
        self.timer_manager.create_timer()


if __name__ == "__main__":
    service_timer_manager = ServiceTimerManager(
        title="shutdown my pc",
        command_to_run="systemctl suspend -i",
        on_calendar="18:05:00",
    )
    service_timer_manager.schedule()
