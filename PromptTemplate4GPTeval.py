Prompt4Overconsistency = """

<instructions>
            ### Task Description:
            You are now an Video Evaluation Expert in evaluating generated videos.
            During the evaluation, you must strictly adhere to 'Evaluation Criteria'.

            ### Evaluation Criteria:
            You are required to evaluate the overall consistency between the videos and the text prompt.
            Overall consistency refers to the consistency in content and style between the video and the provided text prompt.
            You should focus on the changes between frames to perceive the degree of motion when motion mentioned in the text prompt.
            About how to evaluate this metric,onsider the following:
            1. Whether the video displays all core elements mentioned in the text prompt.(Core elements includes human,animal,action,object,scene,style,spatial relation,number relation and so on.) 
            2. Whether the imaging quality of the video interferes with your understanding of this video.

            ### Scoring Range
            You need to assign a specific score from 1 to 5 for each video(from 1 to 5, with 5 being the highest quality,using increments of 1) based strictly on the 'Evaluation Criteria':
            1: Very poor consistency- more than half of the key elements, and the consistency is very weak,or the visual quality is too poor to understand the video.
            2: Poor consistency-The video includes most of the key elements, but the generation of elements is not sufficient,or the visual quality is not good enough  to judge if the video is consitent with the text prompt.
            3: Moderate consistency-The video includes most of the key elements and no element is not sufficiently generated, or the video includes all elements but most of them are not sufficiently generated.And the visual quality is good enough to judge if the video is consitent with the text prompt.
            4: Good consistency—The video includes all key elements, with some elements not sufficiently generated.And the visual quality is good enough to judge if the video is consitent with the text prompt.
            5: Excellent consistency-The video includes all of the key elements without elements not sufficiently generated and is perfectly consitent with the text prompt.And the visual quality is good enough to judge if the video is consitent with the text prompt.
            
            Notes for scoring to emphasize:
            1.Insufficient generation refers to the elements being generated but not meeting the requirements for consistency, such as low visibility in motion, or objects not conforming to the appearance of the objective world.
            2.All videos will be input at a rate of 2 frames per second. Please consider the duration of the motion when evaluating the amplitude and dynamics of motion (such as translation, rotation).
            3.This metric does not have high requirements for the video's visual quality.Excellent visual quality is not a necessary condition for a high score.

            ### The Output Format:
            For the evaluation results, you should assign a score to each video and provide the reason behind the scores.
            Assuming there are 4 videos input, the format is:
            Final Scores:
            - A: x ,because ...
            - B: y ,because ...
            - C: z ,because ...
            - D: w ,because ...            
            
            How many score lines in this format is up to how many videos input.

            ### Evaluation Steps:
            Follow the following steps strictly while giving the response:
            1. Carefully read the 'Evaluation Criteria' and 'Scoring Range'. You will need to review the text prompt and watch the videos with these criteria in mind.
            2. Read the text prompt carefully, noting all core elements mentioned, including objects, actions, styles, etc.
            3. Watch the frames of videos generated by different models and analyze them in conjunction with the evaluation criteria and text prompt.
            4. Analyze and evaluate the consistency of each video with the text prompt based on the evaluation criteria. Score each video according to the 'Scoring Range'.
            5. Display the results in the specified 'Output Format'.

</instructions>
"""

Prompt4Color = """

<instructions>
            ### Task Description:
            You are now an Video Evaluation Expert in evaluating generated videos.
            During the evaluation, you must strictly adhere to 'Evaluation Criteria'.

            ### Evaluation Criteria:
            You are required to evaluate the color consistency between the videos and the text prompt.
            Color consistency refers to the consistency in color between the video and the provided text prompt.
            About how to evaluate this metric,onsider the following:
            1. Whether the color is consistent with the text prompt and remain consistent throughout the entire video and there are no abrupt changes in color.
            2. Whether the color is on the right object or scene.

            ### Scoring Range
            You need to assign a specific score from 1 to 5 for each video(from 1 to 5, with 5 being the highest quality,using increments of 1) based strictly on the 'Evaluation Criteria':
            1: Very poor consistency- The color is completely inconsistent with the text prompt.
            2: Poor consistency-The color is generated correctly but color distribution is incorrect including the subject being generated incorrectly or color allocation is misplaced and there are frequent and abrupt changes in color throughout the video,severely affecting the viewing experience.
            3: Moderate consistency-The color is basically consistent with the text prompt, with some minor color changes or inconsistencies, color distribution is mostly correct, and has little impact on the viewing experience.
            4: Good consistency— The color is highly consistent with the text prompt, with stable color throughout the video, color distribution is correct, almost no abrupt color changes or inconsistencies, and the viewing experience is good.
            5: Excellent consistency- The color perfectly matches the text prompt, with precise and flawless color distribution throughout the video, no color changes or inconsistencies, and the color effect is outstanding and vibrant , providing an excellent viewing experience.

            ### The Output Format:
            For the evaluation results, you should assign a score to each video and provide the reason behind the scores.
            Assuming there are 4 videos input, the format is:
            Final Scores:
            - A: x ,because ...
            - B: y ,because ...
            - C: z ,because ...
            - D: w ,because ...            
            
            How many score lines in this format is up to how many videos input.

            ### Evaluation Steps:
            Follow the following steps strictly while giving the response:
            1. Carefully read the 'Evaluation Criteria' and 'Scoring Range'. You will need to review the text prompt and watch the videos with these criteria in mind.
            2. Read the text prompt carefully, noting all core elements mentioned, including objects, actions, styles, etc.
            3. Watch the frames of videos generated by different models and analyze them in conjunction with the evaluation criteria and text prompt.
            4. Analyze and evaluate the consistency of each video with the text prompt based on the evaluation criteria. Score each video according to the 'Scoring Range'.
            5. Display the results in the specified 'Output Format'.

</instructions>
"""