import openai
import config

# Set OpenAI API Key
openai.api_key = config.OPENAI_API_KEY

def predict_glycan_function(glycan_sequence):
    """
    Sends glycan sequence to OpenAI API to predict its biological function.
    """
    prompt = f"""
    Given the following glycan structure in IUPAC format, predict its biological function. 
    Consider its role in immune signaling, cell adhesion, or disease progression.
    
    Glycan Structure: {glycan_sequence}
    
    Provide a brief explanation of its potential function.
    """

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    
    return response["choices"][0]["message"]["content"]

if __name__ == "__main__":
    print("Glycan Function Predictor")
    glycan_seq = input("Enter a glycan sequence in IUPAC format: ")
    
    prediction = predict_glycan_function(glycan_seq)
    
    print("\nPredicted Function:")
    print(prediction)
