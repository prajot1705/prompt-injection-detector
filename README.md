markdown
# Prompt Injection Detector using Machine Learning

A lightweight tool that detects potentially malicious prompt injections in Large Language Model (LLM) inputs. 
Built using Python, Scikit-learn, and Streamlit, this project classifies prompts as either **safe** or **malicious** 
based on real-time user input.

## 🚀 Features
- Detects prompt injection attacks using ML
- Real-time prediction with confidence scores
- Built with TF-IDF + Logistic Regression
- User-friendly Streamlit interface
- Works offline

## 📸 Demo

🎥 [Click to watch demo video](https://youtu.be/kDcdcEst1sA?si=3bC9zUkamzMsniv5)

## 🛠 Installation

bash
# Clone the repository
git clone https://github.com/your-username/prompt-injection-detector.git
cd prompt-injection-detector

# Create virtual environment
python -m venv venv
venv\Scripts\activate  # for Windows

# Install dependencies
pip install -r requirements.txt
`

## 🚦 Usage

bash
# Train the model (optional if already trained)
python model/detector.py

# Run the app
streamlit run main.py


## 📁 Folder Structure


.
├── model/
│   ├── detector.py         # Training script
│   └── prompt_detector.pkl # Trained model
├── main.py                 # Streamlit app
├── prompts.csv             # Dataset (safe & malicious)
├── requirements.txt
├── README.md


## 📊 Dataset Info

Dataset includes 400 prompts (200 safe, 200 malicious) used for training.

## 🔮 Future Scope

* Upgrade to deep learning (BERT, RoBERTa)
* Multilingual prompt support
* REST API version
* Browser extension integration

## 👥 Authors

* Jay Hatim
* Prajot Kurhade
* Sathaye College



---

Just replace:
- your-username with your GitHub username
- link-to-your-video with the actual YouTube or drive link to your demo
- screenshot.png with an actual screenshot file (you can upload this separately)
