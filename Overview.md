# Gen AI Adoption

**BonuslyCheckCreator** is an experimental tool entirely conceptualized and created with the assistance of ChatGPT. It explores the capabilities of AI to generate a complete solution, covering every step from design to development, including:

## What’s Included:

### AI-Generated Logo:
A custom Rubik's Cube logo with a Matrix-style flowing green code effect, designed to represent the innovative and modern approach of Rubiks Bank.

### Base PDF Check Design:
A professional check template created based on the logo, featuring customizable fields for payee, amount, date, memo, and more.

### Python Script for Customization:
A Python script (built with PyMuPDF) allowing seamless modifications to the generated check PDF. The script was structured to be user-friendly and follows Python best practices.

### Comprehensive Documentation:
A detailed README explaining the setup, environment configuration, and usage, making the tool accessible to both developers and non-technical users.

## The Experiment:
This project demonstrates the power of Generative AI to create an end-to-end solution, starting from creative assets like logos, moving through functional design like PDF generation, and culminating in editable, reusable code for practical use cases.

---

## Prompt

### Step 1:
Generate a Realistic Matrix-Effect Rubik's Cube Logo using Dall-e. Create a realistic and professional logo for "Rubiks Bank." The logo must include:  
- A Rubik's Cube with a Matrix-style effect: smooth, flowing green code streams, like in the movie "The Matrix."  
- The design should be modern.  
- The text "Rubiks Bank" must be integrated cleanly into the logo.  
- Provide the logo as a high-quality downloadable file.  
- Ensure text is in the logo.

---

### Step 2:
Design a professional PDF check for "Rubiks Bank" using the logo generated in Step 1. The check must include the following details:  

#### Bank Branding:  
- **Bank Name**: "Rubiks Bonusly Bank"  
- **Tagline**: "Innovating Cloud Bonusly Solutions"  
- The Matrix-effect Rubik's Cube logo at the top-left corner.  

#### Check Details:  
- **Payee**: "Pay to the Order of: Pablo Petracini"  
- **Currency**: Bonusly Points.  
- **Amount**: "10,000 Bonusly Points" displayed prominently in a bold, boxed section.  
- **Amount in Words**: "Ten Thousand Bonusly Points Only".  
- **Date**: Use today's date.  
- **Check Number**: "0031" displayed at the top-right corner.  
- **Memo Line**: Add "Recognition Bonus!!".  
- **Signature Line**: Include a clean label for "Authorized Signature" with space for signing.  

#### Additional Design Features:  
- Add a faint watermark of the Matrix-style Rubik's Cube logo in the center for a subtle security effect.  
- Include a simulated code line at the bottom for realism: `123456789 |: 987654321 || 1001`.  
- Add background text watermarks saying "Rubiks Bank authentic".  

Ensure the logo does not overlap any text.  
Review the design, and if everything looks good, generate the check as a wide-format PDF file and provide it as a downloadable link.

---

### Step 3:
Create a User-Friendly Python Script to Modify the PDF already generated.  

The script must be:  
1. **Reusable and Editable**: The following fields should be easy to update:  
   - Payee's Name  
   - Amount  
   - Amount in Words  
   - Check Number  
   - Memo Line  
   - Date  
2. **Logo Integration**: Keep the same logo and format of the PDF while allowing manipulation.  
3. **User-Friendly**: Ensure the script is structured so that even non-programmers can understand how to make changes. Use clear explanations.  
4. **Implementation**:  
   - Must use [PyMuPDF](https://pypi.org/project/PyMuPDF).  
   - Follow good Python practices.  
   - Add a small README file with instructions.

---

### Step 4:
Fine-tuning is done manually to align and adjust text perfectly.

---

### Step 5:
Create a comprehensive README file with all necessary documentation, including:
- Environment configuration.
- Python setup instructions.
- Usage details.
