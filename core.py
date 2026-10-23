# Brain of our Project

# Ollama Prompt(System Prompt)

# Connect to Ollama so the app can ask a local language model for help.
import ollama

# Instruction for the AI. How it is should behave and what kind to give.
# Tell the AI to answer data questions with one line of pandas code.

# System Prompt:

PROMPT = '''You are a data analysis. You get a DataFrame called df.
Write ONE line of pandas code that answer the question.
Eply with the code only. No explanation, No ``` marks.


Example: what is the total sale by region?
result = df.groupby('region')['sales'].sum()
'''

# function that will send our coide into the model and return us the output including pandas.
# Send the user's question and a small preview of the data to the AI.

def ask_question(df,question):
    message = f"Columns: {list(df.columns)}\nSample rows:\n{df.head(3)}\nquestion: {question}"
    response = ollama.chat(model = "llama3.2",messages = [
        {'role':'system',"content":PROMPT},
        {'role':'user',"content": message}
    ])
    code = response['message']['content']
    return code.replace("```python","").replace("```","").strip()


# Function that runs the AI code on our data and return the proper answer.
# Run the AI-generated code with the dataframe available as `df`.
def run_code(df,code):
    data = {'df':df}
    try:
        exec(code,data)
        return data['result']
    except Exception as error:
        return f"Error:{error}"


    
