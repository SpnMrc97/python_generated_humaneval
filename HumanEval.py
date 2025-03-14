import os
import json
import re
from openai import OpenAI

# Paths
input_file = r"C:\Users\marco\Documents\TESI\Codice Generato Python\HumanEval.jsonl"
output_folder = r"C:\Users\marco\Documents\TESI\Codice Generato Python\HumanEval"

# Ensure the output folder exists
os.makedirs(output_folder, exist_ok=True)

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Read the JSONL file and process each line
with open(input_file, "r", encoding="utf-8") as file:
    for line in file:
        data = json.loads(line)
        task_id = data["task_id"].replace("/", "_")
        prompt = data["prompt"]
        entry_point = data["entry_point"]
        test_case = data["test"]
        
        # Generate Python code using OpenAI
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[{
                "role": "system",
                "content": (
                    "You are a senior Python developer. Convert the given Python function description into high-quality, "
                    "executable Python code. Ensure the logic remains equivalent and follow best coding practices."
                )
            },
            {"role": "user", "content": prompt}],
            temperature=0.7
        )
        
        generated_code = response.choices[0].message.content
        
        # Remove possible Markdown code blocks ```python ... ```
        match = re.search(r"```(?:python)?\n(.*?)\n```", generated_code, flags=re.DOTALL)
        if match:
            generated_code = match.group(1)
        
        # Truncate the code after the last return statement
        code_lines = generated_code.splitlines()
        last_return_line = next((i for i in range(len(code_lines)-1, -1, -1) if "return" in code_lines[i]), -1)
        if last_return_line != -1:
            code_lines = code_lines[:last_return_line + 1]
        generated_code = "\n".join(code_lines)
        
        # Create dynamic test case execution code
        test_code = f"""
import unittest

class GeneratedCodeTest(unittest.TestCase):
    def test_generated_code(self):
        check({entry_point})  # Execute the test case

if __name__ == "__main__":
    unittest.main(verbosity=2, exit=False)
"""
        
        # Combine the generated code with the test case execution code
        full_code = f"{generated_code.strip()}\n\n{test_case.strip()}\n\n{test_code}"
        
        # Write the Python code to a file
        output_code_path = os.path.join(output_folder, f"{task_id}.py")
        with open(output_code_path, "w", encoding="utf-8") as out_file:
            out_file.write(full_code.strip())
        
        print(f"Generated Python code for {task_id} saved in {output_code_path}")