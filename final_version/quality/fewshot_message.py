frames = "frames extraced from the videos"

prompt_template =  """
<instructions>
        ### Task Description:
        You are now an Video Evaluation Expert in evaluating generated videos and need to evaluate the videos from different models.
        During the evaluation, you must strictly adhere to 'Evaluation Criteria'.and 'Evaluation Steps'.

        ### Evaluation Criteria:
        You will evaluate the image quality of each video, focusing on low-level distortions present in the frames. 
        Image quality involves:
        1. **Clarity**: Evaluate the clarity of the video, as this is the most critical factor in image quality.
        2. **Noise**: Evaluate the presence and level of noise in the video.
        3. **Brightness**: Evaluate whether the brightness is reasonable and determine the extent of any overexposure.

   
        ### Scoring Range:
        Assign a score from 1 to 5 for each video, with 5 representing the highest quality, based on the 'Evaluation Criteria':
        1. **Very Poor Quality (score=1)**: Significant distortion, severe blurriness, numerous noise spots, excessive brightness, resulting in a very poor viewing experience.
        2. **Poor Quality (score=2)**: Noticeable distortions, blurriness, and interference from noise spots, leading to an unnatural viewing experience.
        3. **Moderate Quality (score=3)**: Clarity meets standard definition, with minor distortions, some noise spots, and slight overexposure, resulting in an average experience.
        4. **Good Quality (score=4)**: Clarity reaches high definition, with very few distortions, providing a good viewing experience.
        5. **Excellent Quality (score=5)**: Clarity is at full high definition, with no distortions, delivering an excellent viewing experience.

"""
model = "model you are evaluating"

examplemodels = [x for x in ['cogvideox5b','kling', 'gen3','videocrafter2', 'pika', 'show1', 'lavie'] if x != model]


messages=[
            {
            "role": "system", "content":
                prompt_template
                }
                ,
            {
                "role": "user", "content":[
           "According to **Important Notes** in system meassage, there are examples from other models.\n",
            *[item for examplemodel in examplemodels for item in [
                "This example is from model {} \n".format(examplemodels.index(examplemodel)+1),
                {"type": "image_url", "image_url": {"url": f'data:image/jpg;base64,{frames[examplemodel][0]}', "detail": "low"}}
            ]],              
            
            "These are the frames from the video you are evaluating. \n",
                *map(lambda x: {"type": "image_url", 
                    "image_url": {"url": f'data:image/jpg;base64,{x}', "detail": "low"}},frames[model]),    

            "Assuming there are a video ' scoring 'x',provide your analysis and explanation in the output format as follows:\n"
            "- video: x ,because ..."
              ],
                }
            ]