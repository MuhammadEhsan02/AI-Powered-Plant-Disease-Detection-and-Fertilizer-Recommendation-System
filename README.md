# 🌱 AI-Powered Plant Disease Detection & Fertilizer Recommendation System  

This repository presents an AI-driven solution for plant disease detection and fertilizer recommendations. The project leverages CNN-based image classification and a rule-based recommendation module for accurate and efficient predictions. The system is built with a user-friendly Flask GUI for real-time predictions and seamless deployment.  

---  

## **Features**  
- **Disease Detection**: Predict plant diseases using CNN-based image classification.  
- **Fertilizer Recommendation**: Suggest suitable fertilizers based on the disease and crop type.  
- **GUI Integration**: An interactive Flask-based interface for uploading images and viewing results.  
- **Static File Management**: Uploaded images are stored in the `static` folder for analysis and future reference.  
- **Supplementary Data**: Disease and supplement information for better understanding and usage.  
- **Deployment Ready**: Simplified setup for local or server deployment.  

---  

## **Repository Structure**  
- **Notebook**: Contains the code for model training and evaluation.  
- **App.py**: The main Flask application script.  
- **CNN**: Pre-trained model for plant disease detection.  
- **Templates**: HTML files for rendering the web interface.  
- **Static**: Folder to store images uploaded for predictions.  
- **Model File**: Saved model used for inference. [{Download Here}](https://www.kaggle.com/models/muhammadehsan02/plant_disease_model/)
- **Supplementary Files**: Additional disease and fertilizer information.  
- **Demo Video**: A live demonstration of the system in action.  

---  

## **Setup Instructions**  

1. **Clone the Repository**  
   ```bash
   git clone https://github.com/MuhammadEhsan02/AI-Powered-Plant-Disease-Detection-and-Fertilizer-Recommendation-System.git  
   ```  

2. **Install Dependencies**  
   ```bash
   pip install -r requirements.txt  
   ```  

3. **Run the Flask Application**  
   ```bash
   python App.py  
   ```  

4. **Access the Application**  
   Open `http://127.0.0.1:5000` in your web browser.  

---  

## **Links**  

- **Dataset**: [Download Here](https://www.kaggle.com/datasets/vipoooool/new-plant-diseases-dataset)  
- **Demo Video**: [Watch Live](https://drive.google.com/drive/folders/14UMt1qqau-qmToE9nMpYzDGki9hEpL_A?usp=sharing)  

---  

## **Future Goals**  
- Extend support for additional crops and diseases.  
- Optimize the model for faster inference and lower resource consumption.  
- Develop a mobile application for on-the-go disease detection.  
- Integrate IoT-based sensors for real-time monitoring.
- Enhance the fertilizer recommendation system with AI-based optimization techniques.  
- Collaborate with agricultural experts to refine disease and fertilizer datasets.  
- Expand deployment options, including integration with cloud services for scalability.  

---  

## **Usage Guide**  

1. **Upload an Image**  
   - Navigate to the web interface and upload an image of the plant leaf.  
   - The uploaded image will be stored in the `static` folder for analysis.  

2. **View Predictions**  
   - The system will analyze the uploaded image and display the predicted disease and recommended fertilizer.  

3. **Explore Supplementary Information**  
   - Utilize the provided CSV files for detailed disease and fertilizer insights.  

---  

## **Contact**  
For queries or feedback, feel free to reach out:  
- **Linkedin**: [Muhammad Ehsan](https://ae.linkedin.com/in/muhammad--ehsan)  

---  

I hope this project contributes to efficient and accessible agricultural practices! 🌾  

