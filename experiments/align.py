import os

from aeneas.executetask import ExecuteTask
from aeneas.task import Task

config_string = 'task_language=spa|is_text_type=plain|os_task_file_format=json'
task = Task(config_string=config_string)
task.audio_file_path_absolute = os.path.abspath(os.path.join('data', 'cadiz_ch_1_audio.mp3'))
task.text_file_path_absolute = os.path.abspath(os.path.join('data', 'cadiz_ch_1_text.txt'))
task.sync_map_file_path_absolute = os.path.abspath('syncmap.json')

ExecuteTask(task).execute()
task.output_sync_map_file()
