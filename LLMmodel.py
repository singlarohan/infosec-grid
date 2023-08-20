from transformers import AutoTokenizer, AutoModelForCausalLM
import transformers
import torch

model = "mrm8488/falcoder-7b" #tiiuae/falcon-40b-instruct
tokenizer = AutoTokenizer.from_pretrained(model)

pipeline = transformers.pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    torch_dtype=torch.bfloat16,
    trust_remote_code=True,
    device_map="auto",
)

def generate_response(prompt, len = 300):
    sequences = pipeline(
        prompt,
        max_length=len,
        do_sample=True,
        top_k=10,
        num_return_sequences=1,
        eos_token_id=tokenizer.eos_token_id,
    )
    for seq in sequences:
        return seq['generated_text']