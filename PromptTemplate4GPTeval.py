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
            During the evaluation, you must strictly adhere to 'Evaluation Criteria' and 'Evaluation Steps'..

            ### Evaluation Criteria:
            You will evaluate the color consistency between the video and the text prompt. 
            Color consistency involves:
            1. **Overall Consistency**: Whether the color is consistent with the text prompt and remain consistent throughout the entire video and there are no abrupt changes in color.
            2. **Correct Allocation**: Whether the color is on the right object or background.

            ###Important Notes:
            And you should also pay attention to the following notes:
            1.The watermark in the video should not be a negative factor in the evaluation.
            2.The style of the video should not be a negative factor in the evaluation.            

            ### Scoring Range
            Then based on the above considerations, you need to assign a specific score from 1 to 3 for each video(from 1 to 3, with 3 being the highest quality,using increments of 1) according to the 'Scoring Range':

            1. Poor consistency - The generated object is incorrect or cannot be recognized or the color on the object does not match the text prompt at all.(e.g., yellow instead of red).
            2. Moderate consistency - The correct color appears in the video, but it's not perfect. The specific conditions are:
                -Condition 1: Incorrect allocation (e.g., color on the background, not the object).
                -Condition 2: Instability (e.g., sudden color changes).
                -Condition 3: Confusion (e.g., part of the object has the right color, but it's not dominant).
                -Condition 4: Blending (e.g., object color merging with the background).
                -Condition 5: Similarity (e.g., pink instead of purple).
            3.  Good consistency  - The color is highly consistent with the text prompt, the color in the entire video is stable, the color distribution is correct, there are no sudden changes or inconsistencies in color, and there are no issues mentioned in the moderate consistency category.

            ### The Output Format:
            Finally for the evaluation results, you should assign a score to each video and provide the reason behind the scores.
            Assuming there are 1 video input from model 'A' scoring 'x',the format is:
            <output format>
            Final Scores:
            - A: x ,because ...
            </output format>
                
            <example>
            Assuming there are 1 video input from model 'gen2' scoring '3',the format is:
            Final Scores:
            - gen2: 3 , because ...
            </example>
                
            ### Evaluation Steps
            1. **Understand the Task**:
            - Familiarize yourself with the purpose of the evaluation: to assess the aesthetic quality of generated videos based on the given criteria.
            2. **Review the Video**:
            - Watch the video carefully, focusing on visual elements and overall artistic merit.
            3. **Evaluate Overall Consistency**:
            - Evaluate whether the arrangement of people or objects is reasonable and pleasing, avoiding any psychological discomfort.
            4. **Evaluate Correct Allocation**:
            - Analyze the appropriateness and effectiveness of color choices, noting any discordant colors.
            5. **Assign a Score**:
            - Based on your evaluation, assign a score from 1 to 3 for each video according to the 'Scoring Range'.
            6. **Provide Justification**:
            - After assigning a score, explain your reasoning with specific examples from the video that influenced your decision.
            7. **Document the Evaluation**:
            - Use the 'Output Format' to document your evaluation.

</instructions>
"""


Prompt4Object_class = """
<instructions>
            ### Task Description:
            You are now an Video Evaluation Expert in evaluating generated videos.
            During the evaluation, you must strictly adhere to 'Evaluation Criteria'.

            ### Evaluation Criteria:
            You are required to evaluate the object class consistency between the video and the text prompt. Don't think about quantity consistency.
            Object class consistency refers to the consistency in object between the video and the provided text prompt.
            About how to evaluate this metric,after you watching the frames of videos,you should first consider the following:
            1.Whether the objects mentioned in the text were correctly and clearly generated.
            2.Whether the video focuses on only a part of the object.
            3.Whether the appearance and structure of the generated objects conform to objective reality and human subjective cognition.

            
            ###Important Notes:
            And you should also pay attention to the following notes:
            1.Focus solely on the object's consistency; disregard any considerations related to quantity consistency.
            2.If the video focuses on only a part of the object, it should be considered Moderate consistency.
            

            ### Scoring Range
            Then based on the above considerations, you need to assign a specific score from 1 to 3 for each video(from 1 to 3, with 3 being the highest quality,using increments of 1) according to the 'Scoring Range':

            1. Poor consistency (score=1)- Completely unrecognizable as the specified object.The object is not discernible at all.
            2. Moderate consistency (score=2)- The object can barely be recognized or is generated imperfectly.The specific conditions are:
                - Condition 1 : A similar object with a related function or structure is generated, (e.g., a "snowboard" instead of "skis", a “unicycle” instead of a “bicycle,”)
                - Condition 2 : The object cannot be accurately recognized, (e.g. Uncertain words such as "appears to, seemingly" appear in the video description).
                - Condition 3 : The object in the video is blurred and inconspicuous, making it difficult to recognize.
                - Condition 4 : The video focuses on only a part of the object. (e.g. generating a human hand instead of a whole person.)
                - Condition 5 : More than 3 frames in the video are missing the object.
                - Condition 6 : The appearance of the object changes significantly. (e.g., a person sometimes has facial features and sometimes does not.)
            3. Good consistency (score=3)- The object category is consistently correct throughout the video, the object is complete, clear, obvious, and remains visible in the video and there are no issues mentioned in the moderate consistency category.


            ### The Output Format:
            Finally for the evaluation results, you should assign a score to each video and provide the reason behind the scores.
            Assuming there are 1 video input from model 'A' scoring 'x',the format is:
            <output format>
            Final Scores:
            - A: x ,because ...
            </output format>
                
            <example>
            Assuming there are 1 video input from model 'gen2' scoring '3',the format is:
            Final Scores:
            - gen2: 3 , because ...
            </example>
"""


Prompt4Scene = """
<instructions>
        ### Task Description:
        You are a Video Evaluation Expert tasked with evaluating the scene generation capabilities of AI-generated videos. 
        Your evaluation should be based solely on the provided "Evaluation Criteria" and 'Evaluation Steps'.
        Each video should be assessed independently, without comparisons to others.

        ### Evaluation Criteria:
        You will assess the scene consistency between each video and the corresponding text prompt.
        Scene consistency involves:
        1. **Recognizability**: Can the scene described in the text be identified in the video?  
        2. **Realism**: Do the elements within the scene align with objective reality and human cognitive understanding?

        ### Important Notes:
        1. Watermarks in the video should not negatively impact your evaluation.  
        2. Acceptable video quality includes some blur or distortion as long as scene recognition is not compromised.  
        3. The style of the video should not be a negative factor in the evaluation.

        ### Scoring Range:
        1. **Poor Consistency (score=1)**: The scene is unrecognizable and disconnected from the text, making identification difficult.  
        2. **Moderate Consistency (score=2)**: The scene is recognizable but has issues, such as:
        - Showing only a part of the scene(e.g.,a bathroom showing only a sink and mirror).
        - Presenting a too broad view (e.g., generating a hospital building instead of the interior of a hospital).
        - Highlighting only specific features in close-up (e.g., a bakery showing only bread;a laboratory showing tubes).
        - Similarity to the scene but lacking complete accuracy.  
        3. **Good Consistency (score=3)**: The scene is clearly identifiable and matches human understanding of the objective world.
       
        ### Output Format:
        After evaluating, provide the scores along with your reasoning for each video. Specify which video corresponds to each score using descriptive labels.
        For four videos, the format is:
        A, B, C, D are the names of the video-generated models, and x, y, z, w are the scores assigned to each video.


        ### The Output Format:
        Finally for the evaluation results, you should assign a score to each video and provide the reason behind the scores.
        Assuming there are 1 video input from model 'A' scoring 'x',the format is:
        <output format>
        Final Scores:
        - A: x ,because ...
        </output format>
            
        <example>
        Assuming there are 1 video input from model 'gen2' scoring '3',the format is:
        Final Scores:
        - gen2: 3 , because ...
        </example>

        ### Evaluation Steps

        1. **Understand the Task**:
        - Familiarize yourself with the purpose of the evaluation: to assess the scene generation capabilities of AI-generated videos based on the given criteria.

        2. **Review the Video and Text Prompt**:
        - Watch the video carefully.
        - Read the corresponding text prompt to understand what scene should be represented.

        3. **Assess Recognizability**:
        - Determine if the scene described in the text can be clearly identified in the video.
        - Ask yourself: Does the video visually represent the scene mentioned in the prompt?

        4. **Evaluate Realism**:
        - Analyze the elements within the scene. Do they conform to objective reality and human cognitive understanding?
        - Consider whether the elements look plausible and make sense in the context of the scene.

        5. **Consider Important Notes**:
        - Remember that watermarks should not negatively impact your evaluation.
        - Accept some degree of blur or distortion if it does not hinder scene recognition.
        - The style of the video should not be a factor in your scoring.

        6. **Assign a Score**:
        - Based on your assessment,assign a score from 1 to 3 for each video based on 'Scoring Range'.

        7. **Provide Justification**:
        - After assigning a score, explain your reasoning.
        - Include specific examples from the video that led to your conclusion about the score.

        8. **Document the Evaluation**:
        -Use the 'Output format' to document your evaluation.


</instructions>
"""


Prompt4Action = """
<instructions>
        ### Task Description:
        You are a Video Evaluation Expert tasked with evaluating the action generation capabilities of AI-generated videos. 
        Your evaluation should be based solely on the provided "Evaluation Criteria" and 'Evaluation Steps'. 
        Each video should be assessed independently, without comparisons to others.

        ### Evaluation Criteria:
        You will assess the action consistency between each video and the corresponding text prompt.
        Action consistency involves:
        1. **Recognizability**: Can the action described in the text be identified in the video?
        2. **Realism**: Do the appearance and process of the actions align with objective reality and human understanding?  
        
        ### Important Notes:
        1. Watermarks in the video should not negatively impact your evaluation.  
        2. Acceptable video quality includes some blur or distortion as long as scene recognition is not compromised. 
        3. Focus on action consistency, without needing to evaluate dynamic performance or motion effects.
            Note: The evaluation of motion effects does not need to care the action consistency too much. The focus is on whether the motion effects of actions in the video conform to actual physical laws and human visual perception.


        ### Scoring Range:
        1. **Poor Consistency (score = 1)**: The action is unrecognizable or incorrect, making it impossible to identify or is erroneous.  
        2. **Moderate Consistency (score = 2)**: The action is recognizable but has issues, such as:
        - Significant deviation from reality in appearance or process.
        - Incomplete action, shown only partially in terms of perspective or timing.  
        3. **Good Consistency (score = 3)**: The action is fully consistent with the prompt, with no identified issues.
        

        ### The Output Format:
        Finally for the evaluation results, you should assign a score to each video and provide the reason behind the scores.
        Assuming there are 1 video input from model 'A' scoring 'x',the format is:
        <output format>
        Final Scores:
        - A: x ,because ...
        </output format>
            
        <example>
        Assuming there are 1 video input from model 'gen2' scoring '3',the format is:
        Final Scores:
        - gen2: 3 , because ...
        </example>

        ### Evaluation Steps

        1. **Understand the Task**:
        - Familiarize yourself with the evaluation's purpose: to assess the action generation capabilities of AI-generated videos based on the provided criteria.

        2. **Review the Video and Text Prompt**:
        - Carefully watch the video.
        - Read the corresponding text prompt to understand the intended actions.

        3. **Assess Recognizability**:
        - Determine if the action described in the text is clearly identifiable in the video.
        - Ask yourself: Does the video accurately represent the action mentioned in the prompt?

        4. **Evaluate Realism**:
        - Analyze the appearance and process of the actions. Do they align with objective reality and human understanding?
        - Consider whether the actions appear plausible and reasonable within the context.

        5. **Consider Important Notes**:
        - Watermarks should not negatively affect your evaluation.
        - Accept some degree of blur or distortion, as long as it does not hinder action recognition.
        - Focus on action consistency; do not evaluate dynamic performance or motion effects.

        6. **Assign a Score**:
        - Based on your assessment, assign a score from 1 to 3 for each video according to the 'Scoring Range'.

        7. **Provide Justification**:
        - After assigning a score, clearly explain your reasoning.
        - Include specific examples from the video that led to your conclusion about the score.

        8. **Document the Evaluation**:
        - Use the 'Output Format' to document your evaluation.




</instructions>
"""

Prompt4ImagingQuality = ["""
<instructions>
        ### Task Description:
        You are now an Video Evaluation Expert in evaluating generated videos and need to evaluate the videos from different models.
        During the evaluation, you must strictly adhere to 'Evaluation Criteria'.and 'Evaluation Steps'.
        Each video should be evaluated independently, without comparisons to others.

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
        
        ### Important Notes:
        In the evaluation, you will get example frames from other model and the frames from the video to be evaluted.
        The frames from the video to be evaluated are provided after the example frames. 
        You should evaluate all input frames but just need to provide the score for the video to be evaluated. 

        ### The Output Format:
        Finally for the evaluation results, you should assign a score to each video and provide the reason behind the scores.
        Assuming there are 1 video input from model 'A' scoring 'x',the format is:
        <output format>
        Final Scores:
        - A: x ,because ...
        </output format>
            
        <example>
        Assuming there are 1 video input from model 'gen2' scoring '3',the format is:
        Final Scores:
        - gen2: 3 , because ...
        </example>

"""
]
Prompt4AestheticQuality = """
<instructions>
        ### Task Description:
        You are a Video Evaluation Expert tasked with evaluating the image quality of generated videos. 
        Your evaluation should be based solely on the provided "Evaluation Criteria" and 'Evaluation Steps'.
        Each video should be evaluated independently, without comparisons to others.
        ### Evaluation Criteria:
        You are required to evaluate the aesthetic quality of the videos, which refers to the visual appeal and artistic merit of the footage.
        Aesthetic quality involves:
        1. **Structure**: Evaluate if the arrangement of people or objects is reasonable and pleasing, avoiding psychological discomfort.
        2. **Color Use**: Evaluate the appropriateness of color choices in the video.
        3. **Composition**: Determine if the composition effectively presents all necessary information.
        4. **Visual Appeal**: Evaluate the video's overall visual appeal and emotional expression.
        5. **Harmony**: Evaluate whether the video feels cohesive and harmonious as a whole.

        ### Scoring Range:
        Assign a score from 1 to 5 for each video based strictly on the 'Evaluation Criteria', with 5 representing the highest quality:

        1. **Very Poor Quality (score=1)**: Significant issues in color, composition, and clarity; lacks visual appeal and emotional expression; overall harmony is poor.
        2. **Poor Quality (score=2)**: Noticeable problems in specific aspects, such as discordant colors or poor composition, negatively affecting the overall aesthetic experience.
        3. **Moderate Quality (score=3)**: Average performance in most aspects; may have minor deficiencies, but provides a basic aesthetic experience.
        4. **Good Quality (score=4)**: Strong performance in color, composition, and clarity; offers a visually satisfying experience with reasonable emotional expression and creativity.
        5. **Excellent Quality (score=5)**: Excels in all aspects, with high standards in color, composition, and clarity; delivers strong visual impact and profound emotional expression, resulting in an outstanding aesthetic experience.

        ### Output Format:
        After evaluating, provide the scores along with your reasoning for each video. Specify which video corresponds to each score using descriptive labels.
        For four videos, the format is:
        A, B, C, D are the names of the video-generated models, and x, y, z, w are the scores assigned to each video.

        <output format>  
        Final Scores:  
        - A: x, because ...  
        - B: y, because ...  
        - C: z, because ...  
        - D: w, because ...  
        </output format>

        <example>
        Final Scores:
        - gen2: x , because ...
        - sora: y, because ...
        - T2V: z, because ...
        - videocrafter1: w, because...
        </example>

        ### Evaluation Steps:
        1. **Understand the Task**:
        - Familiarize yourself with the purpose of the evaluation: to assess the aesthetic quality of generated videos based on the given criteria.
        2. **Review the Video**:
        - Watch the video carefully, focusing on visual elements and overall artistic merit.
        3. **Evaluate Structure**:
        - Evaluate whether the arrangement of people or objects is reasonable and pleasing, avoiding any psychological discomfort.
        4. **Evaluate Color Use**:
        - Analyze the appropriateness and effectiveness of color choices, noting any discordant colors.
        5. **Check Composition**:
        - Determine if the composition effectively presents all necessary information and is visually appealing.
        6. **Evaluate Visual Appeal**:
        - Assess the overall visual appeal of the video and its ability to convey emotional expression.
        7. **Evaluate Overall Harmony**:
        - Evaluate the cohesiveness of the video as a whole, ensuring all elements work together harmoniously.
        8. **Assign a Score**:
        - Based on your assessment, assign a score from 1 to 5 for each video according to the 'Scoring Range'.
        9. **Provide Justification**:
        - After assigning a score, explain your reasoning with specific examples from the video that influenced your decision.
        10. **Document the Evaluation**:
            - Use the 'Output Format' to document your evaluation.

"""



Prompt4Motioneffects="""
<instructions>
            ### Task Description:
            You are now an Video Evaluation Expert in evaluating generated videos.
            During the evaluation, you must strictly adhere to 'Evaluation Criteria'.

            ### Evaluation Criteria:
            You are required to evaluate the motion effects of actions in videos.
            Motion effects refer to the naturalness, coherence, and realism of object movement in a video. This metric primarily assesses whether the dynamic effects displayed in the video conform to actual physical laws and human visual perception.
            About how to evaluate this metric,onsider the following:
                1.Whether the motion trajectories of objects are consistent with physical laws, such as inertia and gravity.
                2.Whether the dynamic blur associated with the motion of objects is coherent with the speed and direction of the movement.
                3.Whether the relationship between moving objects and their background is coherent, including occlusions and reflections that align with real-world expectations.
                4.Whether the changes in shadows and lighting as objects move are consistent with physical laws, enhancing the realism of the scene.
        
            ### Important Notes:
            Note: The evaluation of motion effects does not need to care the action consistency too much. The focus is on whether the motion effects of actions in the video conform to actual physical laws and human visual perception.
            
            ###Scoring Range
            You need to assign a specific score from 1 to 5 for each video (from 1 to 5, with 5 being the highest quality, using increments of 1) based strictly on the 'Evaluation Criteria':
            1: Very poor effects - The motion trajectories are significantly incorrect, or the main features of motion are so poorly generated that the motion is difficult to recognize. There is a clear violation of physical laws, and the dynamic blur is either absent or does not correspond with the motion at all.
            2: Poor effects - The motion trajectories are generated poorly, and the motion can only be barely recognized. The dynamic blur is inconsistent with the speed and direction of the movement, and there are noticeable issues with the coherence of the object's interaction with the background and lighting.
            3: Moderate effects - The motion effects are generally present, and the movement can be recognized, but there is one of the following issues:
                The motion smoothness is compromised, with noticeable frame-to-frame inconsistencies or abrupt changes that disrupt the flow of the movement.
                The motion blur is either underutilized or overused, not accurately reflecting the speed and direction of the movement, which affects the perception of realism.
                The motion consistency is partially maintained, but certain elements, such as the interaction between moving objects and their environment or the changes in shadows and lighting, are not fully convincing or are inconsistently portrayed.
            4: Good effects - The action can be recognized and the motion trajectories and dynamic blur are mostly coherent,but there are some parts of the motion is unnatural and does not conform to the human subjective understanding of changes in the objective world.
            5: Excellent effects - The action can be clearly recognized, and the motion trajectories are accurate, dynamic blur is appropriately applied, and the interaction of moving objects with their environment, including shadows and lighting, is seamlessly integrated and realistic.
           
            ### Evaluation Steps:
            Follow the following steps strictly while giving the response:
            1. Carefully read the 'Evaluation Criteria' and 'Scoring Range'. You will need to review the text prompt and watch the videos with these criteria in mind.
            2. Read the text prompt carefully,noting the scene mentioned in the text prompt.
            3. Watch the frames of videos generated by different models and analyze them in conjunction with the evaluation criteria and text prompt.
            4. Compare the differences between consecutive frames to understand the action process in the video.
            5. Analyze and evaluate the consistency of each video with the text prompt based on the evaluation criteria and think about the questions below step by step and then Score each video according to the 'Scoring Range':
                Whether the motion trajectories of objects are consistent with physical laws, such as inertia and gravity.
                Whether the dynamic blur associated with the motion of objects is coherent with the speed and direction of the movement.
                Whether the relationship between moving objects and their background is coherent, including occlusions and reflections that align with real-world expectations.
                Whether the changes in shadows and lighting as objects move are consistent with physical laws, enhancing the realism of the scene.
            6. Display the results in the specified 'Output Format'.

</instructions>
"""

Prompt4TemperalConsistency="""
<instructions>
            ### Task Description:
            You are now an Video Evaluation Expert in evaluating generated videos and have super power to perceive the changes between frames.
            During the evaluation, you must strictly adhere to 'Evaluation Criteria' and 'Evaluation Steps'..

            ### Evaluation Criteria:
            You will evaluate the temporal consistency between the video and the text prompt. 
            Temporal consistency is to measure **frame-to-frame** coherence in the video, focusing on the smoothness and stability of visual and semantic features across consecutive frames.
            The visual features includes color, brightness, texture and details.
            The semantic features  includes object class,positions, shapes, and scene layout.
            To evaluate this metric, you should focus on the following aspects:
                1.whether the texture flickering and color jitter in the video is noticeable.
                2.Whether the 2 kinds of features of the primary object changes unnaturally between consecutive frames.
                3.Whether the 2 kinds of features of the unimportant objects or background changes unnaturally between consecutive frames.
                
            ###Important Notes:
            And you should also pay attention to the following notes:
            1.The watermark in the video should not be a negative factor in the evaluation.
            2.The style of the video should not be a negative factor in the evaluation.            

            ### Scoring Range
            Then based on the above considerations, you need to assign a specific score from 1 to 5 for each video(from 1 to 5, with 5 being the highest quality,using increments of 1) according to the 'Scoring Range':
            1: Very poor consistency - There are many significant unnatural changes through the entire video making it difficult to understand the video.
            2: Poor consistency - The video content can be understood, but there are noticeable unnatural changes in the primary object in the video, significantly affecting the overall temporal consistency. 
            3: Moderate consistency - The video content is fully presented but there are minor noticeable inconsistencies or unnatural changes in unimportant objects, which affect the overall coherence.
            4: Good consistency - The video is complete and comprehensive without any noticeable inconsistency and unnatural changes on objects but there are noticeable texture flickering or color jitter in the visual features of background.
            5: Excellent consistency -  The video provides a full expression of the content and all visual and semantic features are consistent between consecutive frames, and there are no noticeable frame flickering in the video.


</instructions>
"""
