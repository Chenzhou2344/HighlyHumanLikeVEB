import json
import pandas as pd
import numpy as np
import krippendorff
import argparse
parser = argparse.ArgumentParser()
parser.add_argument(
    "--metric",
    type=str,
    default="aesthetic_quality",
    choices=["aesthetic_quality", "imaging_quality", "color", "object_class", "scene", "action","motion_effects","overall_consistency"],
)
args = parser.parse_args()

def statistic(scores):
    return np.mean([s[0] for s in scores]) - np.mean([s[1] for s in scores])


def bootstrap_confidence_interval(data, n_iterations=1000, confidence_level=0.99, sample_size=100000):
    """
    Calculates the confidence interval of a statistic using bootstrapping.
    
    Parameters:
    - data: List of pairs (model score, human score)
    - statistic_fn: Function to compute the statistic (e.g., mean difference)
    - n_iterations: Number of bootstrap iterations (default: 1000)
    - confidence_level: Confidence level for the interval (default: 0.95)
    
    Returns:
    - Lower and upper bounds of the confidence interval
    """
    # Store bootstrap sample statistics
    bootstrap_stats = []
    data_array = np.array(data)    
    # Perform bootstrap iterations
    for _ in range(n_iterations):
        # Resample the data with replacement
        indices = np.random.choice(len(data), size=sample_size, replace=True)
        bootstrap_sample = data_array[indices]
        
        # Calculate the statistic for this sample
        stat = statistic(bootstrap_sample)
        bootstrap_stats.append(stat)
    
    # Calculate percentiles for the confidence interval
    alpha = 1 - confidence_level
    lower_bound = np.percentile(bootstrap_stats, 100 * alpha / 2)
    upper_bound = np.percentile(bootstrap_stats, 100 * (1 - alpha / 2))
    
    return lower_bound, upper_bound


def load_json_data(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)  # Load the JSON data
    return data

# Example usage
#file_path = 'aesthetic_quality_1.json'
#data_1 = load_json_data(file_path)
#file_path = 'imaging_quality_1.json'
#data_2 = load_json_data(file_path)
file_path = '../Human_anno/stable/'+args.metric + '_new.json'
data = load_json_data(file_path)

# Flatten the data into a single dictionary
def flatten_data(row):
    flattened = {'prompt_en': row['prompt_en']}
    
    # Flatten the 'videos', 'gpt4o_eval', and 'baseline_score' dictionaries
    for key, subdict in row['videos'].items():
        flattened[f'video_{key}'] = subdict
        
    for key, subdict in row['gpt4o_eval'].items():
        flattened[f'gpt4o_eval_{key}'] = subdict
        
    for key, subdict in row['baseline_score'].items():
        flattened[f'baseline_score_{key}'] = subdict

    for key, subdict in row['multiagent_score'].items():
        flattened[f'multiagent_score_{key}'] = subdict
    
    # Unpack each list in 'human_anno' into separate columns
    for key, subdict in row['human_anno'].items():
        flattened[f'human_anno_{key}'] = subdict  # First score
        
    return flattened

# Convert the data to a DataFrame
#flattened_data_1 = [flatten_data(row) for row in data_1]
#flattened_data_2 = [flatten_data(row) for row in data_2]
#flattened_data = flattened_data_1 + flattened_data_2
flattened_data = [flatten_data(row) for row in data]
# Create a DataFrame from the flattened data
df = pd.DataFrame(flattened_data)
# Display the DataFrame
print(df)
### Krippendorff's Alpha
models = ['cogvideox5b', 'gen3', 'kling', 'videocrafter2', 'pika', 'show1', 'lavie']
human_scores = []
gpt_scores = []
single_gpt_scores = []
for model in models:
    column_name = f'human_anno_{model}'
    scores = np.vstack(df[column_name].apply(np.array).values).T[:4]
    human_scores.append(scores)
    gpt_score = df[f'multiagent_score_{model}'].values
    gpt_scores.append(gpt_score)
    single_gpt_score = df[f'gpt4o_eval_{model}'].values
    single_gpt_scores.append(single_gpt_score)

human_scores = np.hstack(human_scores)
gpt_scores = np.hstack(gpt_scores)
single_gpt_scores = np.hstack(single_gpt_scores)
alpha_human = krippendorff.alpha(reliability_data=human_scores, level_of_measurement='interval')
alpha_all = krippendorff.alpha(reliability_data=np.vstack([human_scores[:4], gpt_scores]), level_of_measurement='interval')
alpha_single = krippendorff.alpha(reliability_data=np.vstack([human_scores[:4], single_gpt_scores]), level_of_measurement='interval')
print(f"Krippendorff's alpha: 4 human: ", alpha_human, ";4 human&1 multiagent: ",alpha_all, ";4 human&1gpt: ", alpha_single)
### Confidence Interval
for col in df.columns:
    if col.startswith('human'):
        df=df.explode(col) 
models = ['cogvideox5b', 'gen3', 'kling', 'videocrafter2', 'pika', 'show1', 'lavie']
confidence_level = 0.99
score_pairs = []
for model in models:
    for index, row in df.iterrows():
        score_pairs.append((row[f'multiagent_score_{model}'], row[f'human_anno_{model}'])) 
print(np.mean([s[0] for s in score_pairs]) - np.mean([s[1] for s in score_pairs]))
lower_ci, upper_ci = bootstrap_confidence_interval(score_pairs, n_iterations=100, sample_size=10000, confidence_level=confidence_level)
print(f"{confidence_level} confidence interval for the mean difference: ({lower_ci}, {upper_ci}) for model {model}")
