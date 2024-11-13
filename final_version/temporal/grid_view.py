from PromptTemplate4GPTeval import Prompt4TemperalConsistency
prompt_template = Prompt4TemperalConsistency

modelname = "modelname"
frames = "frames from the video"

messages=[
                {
                "role": "system", "content":
                    prompt_template
                    }
                    ,
                {
                    "role": "user", "content":[

            "The following images are concatenated by the key frames of the video.And one of the following images arranges 8 key frames per second from a video in a 1*8 grid view.\n" ,
            *map(lambda x: {"type": "image_url", 
                "image_url": {"url": f'data:image/jpg;base64,{x}', "detail": "low"}},frames[modelname]),    
            "The video most likely have some unnatural changes and frame flickering.Find unnatural changes and evaluate the temporal consistency of the video.\n",                       
            "Assuming there are a video scoring 'x',provide your analysis and explanation in the output format as follows:\n"
            "- video: x ,because ..."
              ],
                    }
                ]

res = {    "0": {
        "cogvideox5b": "- video: 4, because the video shows good temporal consistency with smooth transitions between frames. The primary object, a person walking, maintains consistent visual and semantic features, such as position and shape. However, there is slight texture flickering or color jitter in the background, which slightly affects the overall coherence. Despite this, there are no noticeable unnatural changes or frame flickering that significantly impact the viewing experience.",
        "kling": "- video: 3, because the primary object remains consistent across frames, but there are noticeable inconsistencies in the background. These changes slightly affect the overall coherence, indicating moderate temporal consistency.",
        "gen3": "- video: 3, because there are noticeable inconsistencies in the background, such as slight shifts and flickering, which slightly affect the overall coherence. The primary object remains relatively stable, but the background changes are enough to impact the temporal consistency.",
        "videocrafter2": "- video: 5, because the video shows excellent temporal consistency. The primary object, a person, maintains consistent visual and semantic features across all frames. There are no noticeable unnatural changes or frame flickering. The background remains stable, with no texture flickering or color jitter.",
        "pika": "- video: 5, because the video shows excellent temporal consistency. The visual and semantic features, including the primary object and background, remain stable across consecutive frames. There are no noticeable unnatural changes or frame flickering, ensuring smooth and coherent transitions throughout the video.",
        "show1": "- video: 3, because the primary object, a silhouette of a person, remains consistent in shape and position across frames. However, there are noticeable inconsistencies in the background, such as the trees and road, which slightly affect the overall coherence. These changes suggest moderate consistency with some unnatural variations in the background.",
        "lavie": "- video: 3, because there are noticeable inconsistencies in the background, such as changes in brightness and texture, which slightly affect the overall coherence. The primary objects (people) maintain their positions and movements consistently, but the background flickering is evident."
    },}