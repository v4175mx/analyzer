# Password Security Analyzer

#### Description:
The **Password Security Analyzer** is a tool I developed to increase online security awareness by assessing and validating the strength and security of passwords. My learning from the CS50 course and ongoing cybersecurity training has led to this project.

Throughout my cybersecurity training, I have come to realize the critical role that passwords play in protecting both personal and corporate data. This realization inspired me to create a tool that not only evaluates the strength of passwords, but also checks whether they have been compromised in past data breaches.

### Motivation:
My interest in cybersecurity started because I thought it was cool that you could potentially get into any digital space if you knew how. As I'm still relatively new to cybersecurity, I wanted to start with something basic but crucial — creating a tool that helps people generate and analyze strong passwords. This project is my first step towards using my skills to improve digital security and make it harder for the bad guys to break in.

### Features:
- **Password Strength Assessment**: Evaluates passwords based on length, character diversity, and common pattern usage.
- **Breach Check**: Utilizes the `pyhibp` API to determine if passwords are compromised in known data breaches.
- **Automated Dependency Installation**: Simplifies the user experience by automating the Python library installation process.

### How It Works:
- **Initialization**: Configures user agent settings for HTTP requests and initializes constants for password evaluation.
- **Password Class**: Implements a `Password` class that calculates various strength metrics and an overall strength score for passwords.
- **Security Integration**: Employs `pyhibp` for real-time breach analysis.

### Files Description:
- `analyser.py`: The core script that contains the password analysis, class definitions, strength evaluation algorithms and violation checks.

### Design Choices:
- **Choice of `pyhibp`**: Chosen for its reliable and current database of breached passwords, ensuring that our checks are accurate and meaningful.
- **Automated Installations**: Tackling automated installations was challenging but ultimately enhanced the setup process, making the application more accessible.

### Development Journey:
- **Challenges**: Automating the installation of dependencies was a complex feature to implement but provided a valuable learning experience in software setup automation.
- **Preference for CLI**: While future enhancements might include a GUI, my preference remains with the CLI for its simplicity and directness, which aligns well with the needs of more technical users.

### Future Enhancements:
- **Database Integration**: Plans to store passwords securely in a database using bcrypt for hashing and adding salts, enhancing the security and manageability of password data.
- **Maintaining CLI Focus**: While exploring GUI options, the emphasis will remain on refining and expanding the CLI to ensure it continues to meet the needs of users who prefer this approach.

### Installation:
Ensure Python is installed on your system. The script handles the installation of required libraries automatically. To run the project:
```bash
python analyzer.py
```
### Conclusion:

This Password Security Analyzer is just the beginning for me in cybersecurity. It's about using what I've learned to help others protect themselves online. I hope it's as useful to you as I've enjoyed building it.
