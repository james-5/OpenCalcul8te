# OpenCalculate Project

## Overview
OpenCalculate is an open-source calculator application designed to perform a wide range of scientific and engineering calculations, including physics, astronomy, electromagnetism, chemistry, calculus, and fluid dynamics. This project features a user-friendly graphical interface built with Tkinter in Python, allowing users to compute values such as elastic collisions, Ohm's Law, parallax distances, pH levels, derivatives, integrals, and more, including a specialized orifice plate calculator for gas flow in imperial units.

## Project Transition
Initially, this project was developed in C++ due to its performance advantages and control over system resources. However, I decided to transition to Python for several reasons:
- **Ease of Development**: Python's simplicity and extensive libraries (e.g., Tkinter for GUI) accelerate development and prototyping.
- **Community Support**: Python has a larger community and better documentation, making it easier to troubleshoot and expand the project.
- **Cross-Platform Compatibility**: Python's portability reduces the effort needed to adapt the application across different operating systems.
Despite this shift, I plan to fork the original C++ version to maintain it as a separate project, preserving its performance benefits for users who prefer a compiled, high-efficiency solution.

## Compilation Instructions

### Linux
1. **Prerequisites**:
   - Ensure Python 3.x is installed (`python3 --version`).
   - Install Tkinter: `sudo apt-get install python3-tk` (for Debian/Ubuntu-based systems).
2. **Install Dependencies**:
   - No additional dependencies are required beyond the standard library.
3. **Compile and Run**:
   - Navigate to the project directory: `cd /path/to/OpenCalculate`.
   - Run the application: `python3 opencalculate.py`.
   - The GUI will launch, and you can select tabs to perform calculations.

### Windows
1. **Prerequisites**:
   - Install Python 3.x from [python.org](https://www.python.org/downloads/).
   - During installation, check "Add Python to PATH" and ensure Tkinter is included (it is by default with the standard installer).
2. **Install Dependencies**:
   - No additional packages are needed if using the official Python installer.
3. **Compile and Run**:
   - Open a Command Prompt or PowerShell.
   - Navigate to the project directory: `cd \path\to\OpenCalculate`.
   - Run the application: `python opencalculate.py`.
   - The GUI will appear, ready for use.

## Usage
- Launch the application using the instructions above.
- Use the home tab to navigate to different calculation categories.
- Input values in the provided fields, and click "Calculate" to see results.
- Clear fields with the "Clear" button and return to menus with "Back".

## Future Plans
- I will fork the C++ version to a separate repository for users interested in a compiled alternative.
- Enhance the orifice plate calculator with additional gas properties and unit conversions.
- Add more calculation modules.

## License
This project is open-source under the MIT License. See the `LICENSE` file for details.

## Contact
For questions or contributions, please open an issue on the GitHub repository or contact the maintainer.
