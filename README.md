# 📈 Universal Trend Analyzer

A simple **data analytics web application** that shows how trending any topic is on the internet.
Users can enter any keyword (for example: *IPL, Artificial Intelligence, Virat Kohli, Python*) and the application will display the **trend popularity percentage**, **trend graphs**, and **regional interest** using data from Google Trends.

The application is built using **Python**, **Streamlit**, and the **PyTrends API**.

---

## 🚀 Features

* 🔎 Search any topic or keyword
* 📊 Trend popularity percentage
* 📈 Trend interest over time (line graph)
* 🌍 Top regions searching for the topic
* 🖥 Interactive dashboard interface
* ⚡ Real-time trend data

---

## 🛠 Technologies Used

* Python
* Streamlit
* PyTrends
* Pandas
* Plotly

---

## 📂 Project Structure

```
trend-analyzer
│
├── app.py
├── requirements.txt
└── README.md
```

---

## ⚙ Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/trend-analyzer.git
cd trend-analyzer
```

Install required libraries:

```bash
pip install -r requirements.txt
```

---

## ▶ Run the Application

Start the Streamlit server:

```bash
streamlit run app.py
```

Open your browser and go to:

```
http://localhost:8501
```

---

## 📊 How It Works

1. The user enters a topic or keyword.
2. The application sends a request to Google Trends using the PyTrends API.
3. Google Trends returns popularity scores (0–100).
4. The system calculates the **average popularity percentage**.
5. The application displays:

   * Trend percentage
   * Interest over time graph
   * Regional search interest

---

## 📸 Example

Input:

```
IPL
```

Output:

* Trend Percentage: **78%**
* Interest Over Time Graph
* Top Regions Searching the Topic

---

## 💡 Future Improvements

* Multi-keyword trend comparison
* Sentiment analysis from social media
* Trending topic prediction using machine learning
* Real-time trending dashboard
* News integration for trending topics

---

## 📜 License

This project is open source and available under the **MIT License**.
