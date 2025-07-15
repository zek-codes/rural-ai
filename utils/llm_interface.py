import os
from pathlib import Path
from llama_cpp import Llama

class LLMInterface:
    """Interface for interacting with the AI model (TinyLlama)"""
    
    def __init__(self, model_path=None):
        """
        Initialize the LLM interface
        
        Args:
            model_path (str): Path to the model file. If None, uses default path.
        """
        if model_path is None:
            # Default path to the TinyLlama model
            # This path assumes the model is in rural-ai/model/tinyllama/
            self.model_path = Path(__file__).parent.parent / "model" / "tinyllama" / "tinyllama-1.1b-chat-v1.0.q4_k_m.gguf"
        else:
            self.model_path = Path(model_path)
        
        self.model = None
        self._load_model()
    
    def _load_model(self):
        """Load the model from the specified path"""
        if not self.model_path.exists():
            # Provide a more specific message if the model is not found
            raise FileNotFoundError(
                f"Model file not found at {self.model_path}. "
                "Please ensure 'tinyllama-1.1b-chat-v1.0.q4_k_m.gguf' is in the 'model/tinyllama/' directory."
            )
        
        try:
            # Load TinyLlama model with llama-cpp-python
            self.model = Llama(
                model_path=str(self.model_path),
                n_ctx=1024,  # Context window size
                n_threads=4, # Number of CPU threads to use
                verbose=False # Set to True for more detailed loading output
            )
            print(f"Model loaded successfully from {self.model_path}")
            
        except Exception as e:
            raise RuntimeError(f"Failed to load model: {str(e)}")
    
    def generate_response(self, prompt, max_tokens=200, temperature=0.7):
        """
        Generate a response from the model
        
        Args:
            prompt (str): Input prompt
            max_tokens (int): Maximum number of tokens to generate
            temperature (float): Sampling temperature (controls randomness)
            
        Returns:
            str: Generated response
        """
        if self.model is None:
            return "Error: Model not loaded"
        
        try:
            # Create a system prompt for rural/agriculture focus
            # This prompt guides the AI's behavior and specialization
            system_prompt = f"""You are a helpful AI assistant specializing in rural living, agriculture, and farming. 
Provide practical, clear answers about farming techniques, crop management, animal husbandry, and rural life.
Keep responses concise and helpful for farmers and rural communities."""
            
            # Full prompt for the model, combining system instructions and user input
            # This format is common for chat-tuned models like TinyLlama-Chat
            full_prompt = f"{system_prompt}\n\nHuman: {prompt}"
            
            # Generate response using the model
            response = self.model(
                prompt=full_prompt,
                max_tokens=max_tokens,
                temperature=temperature,
                stop=["Human:", "Assistant:"], # Stop generation when these tokens are encountered
                echo=False # Do not echo the prompt back in the response
            )
            
            # Extract the generated text from the model's response
            return response['choices'][0]['text'].strip()
            
        except Exception as e:
            return f"Error generating response: {str(e)}"
    
    def is_model_loaded(self):
        """Check if the model is successfully loaded"""
        return self.model is not None


# Convenience function for simple usage
def ask_ai(prompt, model_path=None):
    """
    Simple function to ask the AI a question using the LLMInterface
    
    Args:
        prompt (str): The question or prompt
        model_path (str): Optional path to model file (overrides default)
        
    Returns:
        str: AI response or an error message
    """
    try:
        llm_interface = LLMInterface(model_path)
        return llm_interface.generate_response(prompt)
    except Exception as e:
        return f"Error: {str(e)}"
