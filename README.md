**AI-Powered Plant Disease Detection and Fertilizer Recommendation System**

```markdown
# 🌱 AI-Powered Plant Disease Detection and Fertilizer Recommendation System  

This repository contains a comprehensive implementation of an **AI-Powered Plant Disease Detection and Fertilizer Recommendation System**. The system utilizes deep learning to identify plant diseases and offers fertilizer suggestions through a user-friendly Flask interface. It includes all necessary files, supplementary information, and resources for deployment and testing.

---

## **Features**
- **Disease Detection**: Deep learning-based identification of plant diseases using CNN.  
- **Fertilizer Recommendations**: Rule-based module to suggest fertilizers based on detected disease.  
- **Interactive GUI**: Upload plant images for real-time predictions and recommendations.  
- **Efficient Storage**: Uploaded images are stored in the `Static` directory for reference.  
- **Demo Video**: Watch the system in action through the attached demo video.  

---

## **Project Structure**
```
📂 AI-Plant-Disease-System  
│  
├── 📁 Templates               # HTML templates for the Flask app  
├── 📁 Static                  # Storage for uploaded images  
├── 📁 Model                   # Trained CNN model file  
├── 📁 CNN                     # CNN architecture and training scripts  
├── app.py                     # Flask application for GUI and backend logic  
├── Notebook                   # Jupyter notebook for training and predictions  
├── 📁 Data                    # Dataset files for plant disease classification  
├── 📁 Supplement Info         # CSV file with crop-disease mappings  
├── 📁 Demo Video              # Video demonstration of the system  
├── README.md                  # Project overview and usage instructions  
└── requirements.txt           # Python dependencies for the project  
```

---

## **How to Use**

### **1. Clone the Repository**
```bash
git clone https://github.com/MuhammadEhsan02/AI-Powered-Plant-Disease-Detection-and-Fertilizer-Recommendation-System.git
```

### **2. Install Dependencies**
Install required libraries using the `requirements.txt` file:  
```bash
pip install -r requirements.txt
```

### **3. Place the Dataset**
Download the dataset from the link below and place it in the `Data` directory:  
**[Plant Disease Dataset (Kaggle)](https://www.kaggle.com/datasets/vipoooool/new-plant-diseases-dataset)**

### **4. Run the Flask App**
Start the application by running the `app.py` file:  
```bash
python app.py
```
Access the app in your browser at `http://127.0.0.1:5000`.

---

## **Key Resources**
1. **Notebook**: Jupyter notebook for training the CNN model and testing predictions.  
2. **App.py**: Core application file for running the Flask GUI.  
3. **Model File**: Pre-trained CNN model for disease detection.  
4. **Static Folder**: Stores images uploaded through the GUI.  
5. **Disease Info**: Contains essential disease-related details for accurate recommendations.  
6. **Supplement Info**: CSV file with mappings of crops, diseases, and fertilizer suggestions.  
7. **Demo Video**: [Watch the Demo](https://drive.google.com/drive/folders/14UMt1qqau-qmToE9nMpYzDGki9hEpL_A?usp=drive_link).

---

## **Future Goals**
1. Expand dataset coverage for more crops and diseases.  
2. Integrate the system into a mobile application for field deployment.  
3. Enhance recommendation logic using expert systems or ML algorithms.  
4. Introduce multilingual support for better accessibility.  
5. Improve prediction efficiency and accuracy for real-world scenarios.  

---

## **License**
This project is open-source and licensed under the [MIT License](LICENSE).

---

## **Acknowledgments**
- **Dataset Source**: [Plant Disease Dataset (Kaggle)](https://www.kaggle.com/datasets/vipoooool/new-plant-diseases-dataset)  
- **Video Demo**: Attached for a detailed walkthrough of the system.  
- Python libraries like PyTorch, Flask, Pandas, and Matplotlib for enabling seamless development.  

``` 

This README ensures that all your files and resources are well-documented while maintaining a professional tone. Replace `<your-username>` with your GitHub username and add links where applicable.
