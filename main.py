import json  

# Function to check if the question looks like math  
def does_this_look_like_math(my_text):  
    symbols = ["+", "-", "*", "/", "="]  # basic math signs  

    for each_symbol in symbols:  
        if each_symbol in my_text:
            return True  # Runs if it's true  
    return False  # Has to be here if it's false  

# This function kinda runs the whole thing  
def answer_this(question):  
    if not does_this_look_like_math(question):  
        return json.dumps({  
            "error": "Hmm... that doesn't really look like a math problem. Try again."  
        }, indent=4)  

    # Let's generate the response  
    response = professor_response(question)  # type: ignore # Wait... where's this function? 

    # Some debug print, just in case  
    print("DEBUG -> generated response:", response)  

    return json.dumps({"response": response}, indent=4)  

# Testing  
random_question = "If I had 15 dollars and spent 8, how much do I have left?"  
print(answer_this(random_question))  
# If this crashes, just give up and go get some coffee