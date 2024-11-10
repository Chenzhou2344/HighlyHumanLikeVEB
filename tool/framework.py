import os
import json
import os
from openai import OpenAI
import openai
from tool import videoreader
import json
# 创建一个OpenAI客户端实例
client = OpenAI(
    api_key="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",
    base_url="https://gateway.ai.cloudflare.com/v1/627f1b1f372e3a198dc32573bbc6f720/openai-gpt/openai"  # 替换为你的自定义API域
)

## Set the API key and model name
MODEL="gpt-4o-mini-2024-07-18"

class critic_agent:
    def __init__(self, model_name="gpt-4o-mini-2024-07-18"):
        self.model_name = model_name
        self.client = OpenAI(
            api_key="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",
            base_url="https://gateway.ai.cloudflare.com/v1/627f1b1f372e3a198dc32573bbc6f720/openai-gpt/openai"  # 替换为你的自定义API域
        )
        self.model = model_name
        self.system_message_image = """
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
        self.system_message_aesthetic = """
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