from prompt.overall import *
from prompt.color import *
from prompt.motion_effects import *
from prompt.imaging_quality import *
from prompt.aesthetic_quality import *
from prompt.temporal_consistency import *
from prompt.object_class import *
from prompt.scene import *
from prompt.action import *

prompt = {
    "overall_consistency": overall_prompt,
    "color": color_prompt,
    "motion_effects": motion_effects_prompt,
    "imaging_quality": imaging_quality_prompt,
    "aesthetic_quality": aesthetic_quality_prompt,
    "temporal_consistency": temporal_consistency_prompt,
    "object_class": object_class_prompt,
    "scene": scene_prompt,
    "action": action_prompt

 }