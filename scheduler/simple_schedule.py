from service_timer_manager import ServiceTimerManager

class SimpleScheduler:
    def __init__(self, title: str, command: str, on_calendar: str):
        self.title = title
        self.command = command
        self.on_calendar = on_calendar
    
    def schedule(self):
        self.service_timer_manager = ServiceTimerManager(
            service_filename=f"{self.title}.service",
            service_description=self.title,
            command=self.command,
            timer_filename=f"{self.title}.timer",
            timer_description=self.title,
            on_calendar=self.on_calendar,
        )
        self.service_timer_manager.schedule()