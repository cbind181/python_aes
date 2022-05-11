# Description
This program is a simple demonstration and benchmark of the AES-CBC encryption algorithm implemented in Python 3 (3.10.4) using `pip` as the package manager.

# Expected Behavior
Upon running the program, be patient and allow it a few seconds to complete its first encryption and decryption pass. The time this takes will vary from system to system. The program will run 20 passes of encryption and decryption on a target text (`.txt`) file and print the times each time it completes a pass. It will then print an average encryption and decryption times and the best encryption and decryption times upon completing all 20 runs.

# How to Run
## Installation
In order to run this program, you will need to have Python 3 (version 3.10.4 or later) installed and the latest version of `pip`. You can follow the installation instructions [here](https://www.python.org/downloads/). The project was built and ran on Linux, so that is what the rest of the guide will reference for execution.

## Compilation and Execution
In order to run the program, you first must navigate to the project folder and edit the `aes.py` file to use the correct file path to run the encryption and decryption processes on. Replace the file path with the **full path** to your file in the `enc.encrypt_file()` and `enc.decrypt_file()` method calls on lines 76 and 79 respectively. Be sure to add the `.enc` to your file in the decryption method so that the program knows which file to decrypt, since the program will end up moving the data between the two files/file paths you specified. Be sure to save the file upon making your changes.
<br><br>
Next, make sure that you install the dependencies for Python by navigating to the project folder and running `pip install -r requirements.txt`. This command will install the dependencies that are listed in the `requirements.txt` file.
<br><br>
Finally, execute the program by running `python3 aes.py` in the terminal.
