from service_timer_manager import ServiceTimerManager

class SimpleScheduler:
    def __init__(self, title: str, command: str, on_calendar: str, overwrite: bool = False):
        self.title = title
        self.command = command
        self.on_calendar = on_calendar
        self.overwrite = overwrite
    
    def schedule(self):
        self.service_timer_manager = ServiceTimerManager(
            service_filename=f"{self.title}.service",
            service_description=self.title,
            command=self.command,
            timer_filename=f"{self.title}.timer",
            timer_description=self.title,
            on_calendar=self.on_calendar,
            overwrite=self.overwrite,
        )
        self.service_timer_manager.schedule()

        
if __name__ == '__main__':
    import os 
    title='sleep_time'
    sc = SimpleScheduler(
        title=title,
        command='shutdown now',
        on_calendar='daily',
        overwrite=True,
    )
    sc.schedule()
    # os.remove(f'/etc/systemd/system/{title}.service')
    # os.remove(f'/etc/systemd/system/{title}.timer')   