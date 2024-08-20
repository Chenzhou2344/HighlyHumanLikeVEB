import av
import numpy as np
import torch
from transformers import VideoLlavaProcessor, VideoLlavaForConditionalGeneration


class VideoLlavaTool():
    def __init__(self, model_name_or_path, device_map="auto"):
        print(f"Loading model: {model_name_or_path}")
        self.processor = VideoLlavaProcessor.from_pretrained(model_name_or_path)
        self.model = VideoLlavaForConditionalGeneration.from_pretrained(
            model_name_or_path,
            torch_dtype=torch.float16,
            device_map=device_map,
            trust_remote_code=True
        ).eval()

    def read_video_pyav(self, video_path, num_frames=8):
        container = av.open(video_path)
        total_frames = container.streams.video[0].frames
        indices = np.arange(0, total_frames, total_frames / num_frames).astype(int)

        frames = []
        container.seek(0)
        start_index = indices[0]
        end_index = indices[-1]
        for i, frame in enumerate(container.decode(video=0)):
            if i > end_index:
                break
            if i >= start_index and i in indices:
                frames.append(frame)

        clip = np.stack([x.to_ndarray(format="rgb24") for x in frames])
        return clip

    def prepare_input(self, video_path, prompt):
        clip = self.read_video_pyav(video_path)
        prompt = f"A chat between a curious human and an artificial intelligence assistant. The assistant gives helpful, detailed, and polite answers to the human's questions. USER: <video>\n{prompt} ASSISTANT:"
        inputs = self.processor(text=prompt, videos=clip, return_tensors="pt")
        return inputs

    def generate(self, video_path, prompt, max_length=80):
        inputs = self.prepare_input(video_path, prompt).to(self.model.device)
        with torch.no_grad():
            output = self.model.generate(**inputs, max_length=max_length)
            response = self.processor.batch_decode(output, skip_special_tokens=True, clean_up_tokenization_spaces=False)[0]
            torch.cuda.empty_cache()
        return response.split('ASSISTANT:')[-1]
