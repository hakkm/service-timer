from scheduler import SimpleScheduler


super_productivity_scheduler = SimpleScheduler(
    title="obsidian",
    command="/home/khabir/AppImages/Obsidian-1.1.9.AppImage",
    on_calendar="13:56:00",
    overwrite=True,
)

super_productivity_scheduler.schedule()
