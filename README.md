# 🌱 Rural AI

Rural AI is an offline-first AI assistant for rural education. It runs locally on a Raspberry Pi, turning it into a self-contained Wi-Fi hotspot and AI learning hub. Students connect to it wirelessly using their phones, tablets, or laptops — no internet required.

Designed to support digital learning in disconnected environments, Rural AI uses powerful open-source AI models to deliver interactive education in subjects like agriculture, science, and literacy.

## 🧠 What It Does

🔌 Runs offline on a Raspberry Pi (no internet or cloud needed)

📶 Broadcasts a Wi-Fi hotspot that users can connect to

🌐 Serves a local web app to any connected device

💬 Accepts student questions and responds with AI-powered answers

📚 Built for use in rural classrooms, community centers, and remote schools

## 🧠 AI Model Used

| Component | Model | Format | Notes |
|-----------|-------|--------|-------|
| Language Model | TinyLlama-1.1B-Chat-v1.0 | Hugging Face / GGUF | Open-source, instruction-tuned 1.1B parameter model with Apache 2.0 license. Optimized for Raspberry Pi with low memory usage. |
| (Optional) Speech-to-text | Whisper (tiny/base) | ONNX / PyTorch | Can be added for voice input in offline scenarios. |

## 🧰 Tech Stack

| Tool / Framework | Purpose |
|------------------|---------|
| Flask | Local web server and API backend |
| Transformers | Hugging Face library for TinyLlama inference |
| PyTorch | Deep learning framework for model execution |
| Hostapd + dnsmasq | Turns the Raspberry Pi into a Wi-Fi hotspot |
| Raspberry Pi OS | 64-bit OS environment for deployment |

## 📶 How It Works

1. Raspberry Pi runs the AI assistant using TinyLlama (1.1B parameters - optimized for resource efficiency).
2. The Pi also becomes a Wi-Fi hotspot (e.g., SSID: rural-ai).
3. Nearby users connect their devices to the Pi's Wi-Fi.
4. Opening a browser and visiting http://192.168.4.1 loads the Rural AI app.
5. Users can ask educational questions (e.g. "What is crop rotation?") and receive answers instantly — all without internet access.

## Project Structure

```
rural-ai/
├── app.py                  # Main Flask application
├── model/
│   └── tinyllama/          # TinyLlama model files (auto-downloaded)
├── utils/
│   └── llm_interface.py    # LLM interaction module
├── static/
│   └── style.css           # Frontend styling
├── templates/
│   └── index.html          # Web interface template
├── requirements.txt        # Python dependencies
└── README.md              # This file
```
├── utils/
│   └── llm_interface.py    # LLM interaction module
├── static/
│   └── style.css           # Frontend styling
├── templates/
│   └── index.html          # Web interface template
├── requirements.txt        # Python dependencies
└── README.md              # This file
```

## 📦 Installation (on Raspberry Pi 4 or 5)

### Quick Setup
```bash
git clone https://github.com/your-username/rural-ai
cd rural-ai
bash setup.sh        # Sets up TinyLlama and installs dependencies
sudo bash wifi-hub.sh # Turns the Pi into a Wi-Fi hotspot
python3 app.py        # Starts the Flask server
```

### Manual Setup
```bash
# Create virtual environment
python3 -m venv rural-ai-env
source rural-ai-env/bin/activate

# Install dependencies
pip install -r requirements.txt

# TinyLlama will auto-download on first run
python3 app.py
```

### Development Setup (Windows/Mac/Linux)

1. **Create Virtual Environment**
```bash
python -m venv rural-ai-env
rural-ai-env\Scripts\activate  # Windows
# source rural-ai-env/bin/activate  # Linux/Mac
```

2. **Install Dependencies**
```bash
pip install -r requirements.txt
```

3. **Model Setup (Automatic)**
TinyLlama will automatically download from Hugging Face on first run (~2.2GB):
- **Model:** `TinyLlama/TinyLlama-1.1B-Chat-v1.0`
- **Source:** Hugging Face Transformers
- **License:** Apache 2.0

4. **Run the Application**
```bash
python app.py
```

The application will start on `http://localhost:5000`

## 🌍 Example Use Cases

🧑🏽‍🏫 Teacher assistant for lesson prep or in-class Q&A

🧑🏽‍🌾 Explains agriculture topics (e.g. irrigation, rainfall)

🧒🏽 Self-paced learning for students using shared devices

🧠 Local language AI (supports English, with potential for local language fine-tuning)

## 🧪 Example Conversation

**Student:** What is compost, and how do I make it?

**Rural AI:** Compost is decomposed organic matter that enriches soil. To make it:
1. Collect vegetable scraps, fruit peels, and dry leaves
2. Layer them in a pile or bin
3. Add some soil and water to keep it moist
4. Turn the pile every few weeks
5. In 2-3 months, you'll have rich, dark compost for your garden!

## 🚀 Model Alternatives

### Option 1: Hugging Face Transformers (Recommended)
```bash
# Uses transformers library - easiest setup
pip install transformers torch
```

### Option 2: GGUF with llama.cpp (Lower Memory)
```bash
# Download quantized model for Raspberry Pi
wget https://huggingface.co/TheBloke/TinyLlama-1.1B-Chat-v1.0-GGUF/resolve/main/tinyllama-1.1b-chat-v1.0.q4_k_m.gguf
```

### Option 3: Ollama (Local API)
```bash
# Install Ollama and pull TinyLlama
curl -fsSL https://ollama.ai/install.sh | sh
ollama pull tinyllama
```

## 💾 System Requirements

### Minimum (Raspberry Pi 4)
- **RAM:** 4GB (2GB possible with swap)
- **Storage:** 8GB SD card minimum
- **Model Size:** ~600MB (quantized GGUF)

### Recommended (Raspberry Pi 5)
- **RAM:** 8GB
- **Storage:** 32GB+ SD card
- **Model Size:** ~2.2GB (full TinyLlama model)

## Features

- **Web-based Chat Interface**: Clean, responsive UI for interacting with the AI
- **Local Model**: Runs entirely offline using TinyLlama
- **Rural/Agriculture Focus**: Optimized for rural living and farming questions
- **Real-time Responses**: Fast inference with 1.1B parameter model
- **Low Resource Usage**: Optimized for Raspberry Pi deployment

## Usage

1. Open your browser and go to `http://localhost:5000` (or `http://192.168.4.1` on Pi hotspot)
2. Type your questions about farming, agriculture, or rural living
3. Press Enter or click Send to get AI responses
4. The conversation history is maintained during your session

## Customization

- **Model**: Switch between Hugging Face, GGUF, or Ollama implementations
- **Styling**: Modify `static/style.css` to change the appearance
- **Prompts**: Update the system prompts in `utils/llm_interface.py` for different specializations

## 🔧 Performance Tuning

### For Raspberry Pi 4 (4GB RAM)
```python
# Use quantized model in llm_interface.py
torch_dtype=torch.float16
device_map="cpu"
```

### For Raspberry Pi 5 (8GB RAM)
```python
# Can use full precision
torch_dtype=torch.float32
device_map="auto"
```

## Troubleshooting

### Model Loading Issues
```bash
# Clear cache and reinstall
pip cache purge
pip install --upgrade transformers torch
```

### Memory Issues on Pi
```bash
# Increase swap space
sudo dphys-swapfile swapoff
sudo nano /etc/dphys-swapfile  # Set CONF_SWAPSIZE=2048
sudo dphys-swapfile setup
sudo dphys-swapfile swapon
```

### Wi-Fi Hotspot Problems
```bash
# Restart networking services
sudo systemctl restart hostapd
sudo systemctl restart dnsmasq
```

## 🔄 Future Plans

🎙️ Add voice input/output with Whisper + TTS

🧑🏽‍🏫 Local curriculum modules and quizzes

🌐 Syncable content updates over USB or mesh

📱 Progressive Web App (PWA) for offline mobile access

🌍 Multi-language support for local languages

Want help getting started with your classroom setup? Reach out or clone the repo and build your own Rural AI learning hub today.

## 📜 License

- **Code:** MIT License
- **Model:** TinyLlama-1.1B-Chat-v1.0 – Apache 2.0 license
- **Framework:** Transformers library – Apache 2.0 license

## 🤝 Contributing

Want to help improve Rural AI for educational access? 

1. Fork the repository
2. Create your feature branch
3. Test on Raspberry Pi hardware
4. Submit a pull request

---

**Ready to bring AI education to rural communities?** Clone the repo and start building your offline learning hub today! 🌾🤖

🧑🏽‍🏫 Local curriculum modules and quizzes

🌐 Syncable content updates over USB or mesh

Want help getting started with your classroom setup? Reach out or clone the repo and build your own Rural AI learning hub today.

## 📜 License

- **Code**: MIT License
- **Model**: Phi-3-mini-4B-Instruct – MIT license

## Contributing

Feel free to submit issues and enhancement requests!
