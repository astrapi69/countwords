# **Word Frequency Analyzer with GitHub Copilot**

This repository demonstrates a simple NLP-based Python project to analyze word frequency in a text file. The project uses **GitHub Copilot** to assist in code generation and speed up development.

---

## **Overview**

This Python application:
1. Reads a text file (e.g., from Project Gutenberg).
2. Cleans the text by converting it to lowercase and removing punctuation.
3. Tokenizes the text into words.
4. Counts the frequency of each unique word.
5. Displays the top N most frequent words in a bar chart using **Matplotlib**.
---

## **About This Project**

This project was created as part of an example exercise inspired by a book on using GitHub Copilot for coding assistance. 
It demonstrates how developers can leverage AI tools to streamline tasks like tokenization, analysis, and visualization.

---

## **Features**
- Demonstrates GitHub Copilot’s **code completion** and **chat capabilities**.
- Provides an introduction to **tokenization** and word frequency analysis.
- Generates a visual representation of word frequency using Matplotlib.

---

## **Prerequisites**

- **Python 3.8+** installed
- **Visual Studio Code** with the GitHub Copilot extension installed
- Required libraries:
    - `matplotlib`
    - `tkinter`

---

## **Setup Instructions**

1. **Clone the repository**:
   ```bash
   git clone https://github.com/astrapi69/countwords.git
   cd countwords
   ```

2. **Create a Python virtual environment**:
   ```bash
   python -m venv env
   source env/bin/activate    # For Linux/Mac
   .\env\Scripts\activate     # For Windows
   ```

3. **Install required dependencies**:
   ```bash
   pip install matplotlib tk
   ```

4. **Download the text file**:  
   Use a large text file for analysis. For example, download "Free Air" by Sinclair Lewis from Project Gutenberg:
   ```bash
   wget https://www.gutenberg.org/cache/epub/26732/pg26732.txt
   ```

5. **Run the application**:
   ```bash
   python main.py
   ```

---

## **How It Works**

1. **Read and Clean the Text**:  
   The application reads the text file, converts all text to lowercase, and removes punctuation.

2. **Tokenization**:  
   The text is split into words for analysis.

3. **Word Frequency Count**:  
   The script counts the occurrence of each word in the text.

4. **Visualization**:  
   The program generates a **bar chart** of the top N most frequent words using Matplotlib.

---

## **Example Output**

After running the program, you’ll see a bar chart similar to the one below:

```
Top 20 Words in the Text:
- 'the' : 1200 times
- 'and' : 950 times
...
```

---

## **Testing the Code**

To ensure the generated code works correctly:
- Verify the output using **unit tests**.
- Use performance checks (e.g., time execution for cleaning functions).
- Test edge cases, such as empty files or files with unusual characters.

---

## **Notes**
- The project demonstrates the power of **GitHub Copilot** in assisting development.
- AI-generated code must always be **verified** and tested to ensure accuracy and functionality.

---

## **License**
This project is released under the MIT License.

---

**Enjoy building, learning, and experimenting with GitHub Copilot!**