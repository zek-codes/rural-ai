from flask import Flask, render_template, request, redirect, url_for, flash
from utils.llm_interface import LLMInterface
import os

app = Flask(__name__)
app.secret_key = 'rural-ai-secret-key-change-in-production'

# Initialize the LLM interface globally
llm = None

def initialize_llm():
    """Initialize the LLM interface with error handling"""
    global llm
    try:
        llm = LLMInterface()
        print("✅ LLM initialized successfully")
        return True
    except FileNotFoundError:
        print("❌ Model file not found. Please download phi3.q4_K_M.gguf to the model/ folder")
        return False
    except Exception as e:
        print(f"❌ Failed to initialize LLM: {str(e)}")
        return False

@app.route('/', methods=['GET', 'POST'])
def index():
    """Main page that handles both display and form submission"""
    response = None
    error_message = None
    
    if request.method == 'POST':
        # Get the prompt from the form
        prompt = request.form.get('prompt', '').strip()
        
        if not prompt:
            error_message = "Please enter a question."
        else:
            # Check if LLM is initialized
            if llm is None:
                if not initialize_llm():
                    error_message = "AI model is not available. Please check that the model file is in the model/ folder."
                else:
                    # Generate response
                    try:
                        response = llm.generate_response(prompt)
                    except Exception as e:
                        error_message = f"Error generating response: {str(e)}"
            else:
                # Generate response
                try:
                    response = llm.generate_response(prompt)
                except Exception as e:
                    error_message = f"Error generating response: {str(e)}"
    
    return render_template('index.html', response=response, error_message=error_message)

@app.route('/health')
def health_check():
    """Health check endpoint"""
    status = {
        'status': 'healthy',
        'model_loaded': llm is not None and llm.is_model_loaded()
    }
    return status

@app.route('/about')
def about():
    """About page with information about Rural AI"""
    return render_template('about.html')

@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return render_template('error.html', error="Page not found"), 404

@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors"""
    return render_template('error.html', error="Internal server error"), 500

if __name__ == '__main__':
    print("🌾 Starting Rural AI Assistant...")
    
    # Try to initialize the LLM at startup
    initialize_llm()
    
    # Run the Flask app
    print("🚀 Starting Flask server...")
    print("📱 Access the app at: http://localhost:5000")
    print("🔗 Or from other devices: http://192.168.4.1:5000 (when on Pi hotspot)")
    
    app.run(
        debug=True, 
        host='0.0.0.0',  # Allow connections from other devices
        port=5000
    )