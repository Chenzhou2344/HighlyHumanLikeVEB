frames = "frames extraced from the videos"
model = "model you are evaluating"
examplemodels = [x for x in ['cogvideox5b','kling', 'gen3','videocrafter2', 'pika', 'show1', 'lavie'] if x != model]

prompt_template4GPT4o =  """
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

system_message_image4GPT4omini ="""
                ## Role: Image Quality Evaluation Expert

                ## Role Profile:
                - Response language: English
                - Description: You are an expert specializing in the evaluation of image quality, focusing on static image quality. You are familiar with all aspects of image quality and have an in-depth understanding of how to systematically evaluate image quality.

                ## Goals:
                - Based on user input from different video generation models' generated video frames, as well as the evaluation results of these video images, consider whether the Evaluation results are reasonable to assist in the evaluation of video image quality.
                - Output an evaluation of the existing evaluation results for each model, identifying issues that do not match the actual video frames.
                - Must combine the video frames with the corresponding evaluation results to provide a comprehensive and objective evaluation.

                ## Skills:
                1. Possess strong image quality evaluation capabilities.
                2. Familiar with all aspects of image quality evaluation.
                3. Have strong logical analysis skills.
                4. Have strong expressive abilities.
                """

system_message_aesthetic4GPT4omini = """
        ## Role: Aesthetic Quality Evaluation Expert

        ## Role Profile:
        - Response language: English
        - Description: You are an expert specializing in the evaluation of aesthetic quality, focusing on static aesthetic quality. You are familiar with all aspects of aesthetic quality and have an in-depth understanding of how to systematically evaluate aesthetic quality.

        ## Goals:
        - Based on user input from different video generation models' generated video frames, as well as the evaluation results of these video images, consider whether the Evaluation results are reasonable to assist in the evaluation of video aesthetic quality.
        - Output an evaluation of the existing evaluation results for each model, identifying issues that do not match the actual video frames.
        - Must combine the video frames with the corresponding evaluation results to provide a comprehensive and objective evaluation.

        ## Skills:
        1. Possess strong aesthetic quality evaluation capabilities.
        2. Familiar with all aspects of aesthetic quality evaluation.
        3. Have strong logical analysis skills.
        4. Have strong expressive abilities.
        """

messages_first_step=[
            {
            "role": "system", "content":
                prompt_template4GPT4o
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

eval_res = {    "0": {
        "cogvideox5b": "- video: 4, because the frames from the video show good clarity with minimal distortions. The colors are vibrant, and there is a slight presence of noise, but it does not significantly impact the viewing experience. The brightness is well-balanced, providing a high-definition quality overall.",
        "kling": "- video: 4, because the frames show good clarity with high definition. There are very few distortions, and the brightness is well-balanced, providing a good viewing experience. There is minimal noise, making the video quality quite high.",
        "gen3": "- video: 4, because the frames exhibit good clarity with minimal distortions. The colors are vibrant, and the details on the grapes are well-defined. There is a slight overexposure in some areas, but it does not significantly detract from the overall quality. The noise level is low, providing a pleasant viewing experience.",
        "videocrafter2": "- video: 4, because the frames show high definition clarity with very few distortions. The colors are vibrant, and there is minimal noise. The brightness is well-balanced, providing a good viewing experience.",
        "pika": "- video: 3, because the frames show moderate quality. The clarity is acceptable but not sharp, with some noticeable blurriness. There is a slight presence of noise, and the brightness is somewhat overexposed, affecting the overall viewing experience.",
        "show1": "- video: 2, because the frames show noticeable blurriness and lack of clarity. The images are not sharp, and there is some noise present. The brightness is slightly overexposed, affecting the overall viewing experience.",
        "lavie": "- video: 2, because the frames show noticeable blurriness and lack of clarity. The images are not sharp, and there is a slight overexposure, which affects the overall viewing experience. The quality is poor compared to the examples, with significant room for improvement in clarity and brightness balance."
    }}

messages_second_step=[
        {
        "role": "system", "content":
        system_message_image4GPT4omini,
        }
        ,
        {
        "role": "user", "content": [
        "According to  your **Goals**in system meassage, there are examples and evaluation results from video generation models.\n",
        *[item for examplemodel in examplemodels for item in [
            "This example is from model '{}' \n".format(examplemodel),
            {"type": "image_url", "image_url": {"url": f'data:image/jpg;base64,{frames[examplemodel][0]}', "detail": "low"}}
        ]],                 
        "The evaluation results of these examples are as follows:\n",
        *map(lambda x: f"model: {x}, evaluation result: {eval_res[x]}\n", examplemodels),
        
        "Assuming there are videos you think should score 'x',provide your analysis and explanation in the output format as follows:\n",
        *map(lambda x: f"- {x}: should be scored x,because...\n", examplemodels),

            ],
            }
        ]

helpeval = {"0": {
        "cogvideox5b": "- cogvideox5b: should be scored 4, because the clarity is high with minimal distortions, vibrant colors, and well-balanced brightness. The slight noise present does not significantly detract from the overall quality, maintaining a high-definition viewing experience.",
        "kling": "- kling: should be scored 4, because the frames exhibit good clarity and high definition. The minimal distortions and well-balanced brightness contribute to a good viewing experience, with very little noise affecting the quality.",
        "gen3": "- gen3: should be scored 3, because while the frames show good clarity and vibrant colors, the slight overexposure in some areas detracts from the overall quality. The details are well-defined, but the overexposure impacts the viewing experience, warranting a slightly lower score.",
        "videocrafter2": "- videocrafter2: should be scored 4, because the frames demonstrate high-definition clarity with minimal distortions. The vibrant colors and well-balanced brightness provide a good viewing experience, with very little noise present.",
        "pika": "- pika: should be scored 3, because the frames show moderate quality with acceptable clarity, but noticeable blurriness affects the sharpness. The slight presence of noise and overexposure in brightness impacts the overall viewing experience, justifying a middle score.",
        "show1": "- show1: should be scored 2, because the frames exhibit noticeable blurriness and lack of clarity. The images are not sharp, and the presence of noise, along with slight overexposure, significantly affects the viewing experience.",
        "lavie": "- lavie: should be scored 2, because the frames also show noticeable blurriness and lack of clarity. The images are not sharp, and the slight overexposure further detracts from the overall quality, indicating significant room for improvement in clarity and brightness balance."
    }}

messages_final_step=[
            {
            "role": "system", "content":
                prompt_template4GPT4o
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
                    "image_url": {"url": f'data:image/jpg;base64,{x}', "detail": "low"}},frames[modelname]), 
                    
            "Your previous evaluation is as follows:\n",
            eval_res[str(i)][modelname],
            "And the following is the analysis of the previous evaluation from a image quality evaluator played by gpt4omini, which may help you to evaluate the video.\n",          
            "Attention: The following analysis is may not be accurate. Just for reference and evaluate the video according to your own judgment.\n",
            helpeval[str(i)][modelname],
            "Assuming there are a video ' scoring 'x',provide your analysis and explanation in the output format as follows:\n"
            "- video: x ,because ..."
              ]
            }
        ]

final_result = {
        "0": {
        "cogvideox5b": "- video: 4, because the frames from the video exhibit good clarity with minimal distortions. The colors are vibrant, and there is a slight presence of noise, but it does not significantly impact the viewing experience. The brightness is well-balanced, providing a high-definition quality overall.",
        "kling": "- video: 4, because the frames show good clarity with high definition. There are very few distortions, and the brightness is well-balanced, providing a good viewing experience. There is minimal noise, making the video quality quite high.",
        "gen3": "- video: 4, because the frames exhibit good clarity with minimal distortions. The colors are vibrant, and the details on the grapes are well-defined. There is a slight overexposure in some areas, but it does not significantly detract from the overall quality. The noise level is low, providing a pleasant viewing experience.",
        "videocrafter2": "- video: 4, because the frames exhibit high-definition clarity with very few distortions. The colors are vibrant, and there is minimal noise. The brightness is well-balanced, providing a good viewing experience.",
        "pika": "- video: 3, because the frames show moderate quality. The clarity is acceptable but not sharp, with some noticeable blurriness. There is a slight presence of noise, and the brightness is somewhat overexposed, affecting the overall viewing experience.",
        "show1": "- video: 2, because the frames exhibit noticeable blurriness and lack of clarity. The images are not sharp, and there is some noise present. The brightness is slightly overexposed, which significantly affects the overall viewing experience.",
        "lavie": "- video: 2, because the frames exhibit noticeable blurriness and lack of clarity. The images are not sharp, and there is a slight overexposure, which negatively impacts the overall viewing experience. Compared to the examples, the quality is poor, with significant room for improvement in terms of clarity and brightness balance."
    }
}