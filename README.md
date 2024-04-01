# Data Recovery

## Overview

Data Recovery is a Python-based command-line tool designed to recover deleted files from various storage devices. Utilizing byte-level scanning, it identifies files based on their unique signatures, offering a chance to restore files that have been inadvertently deleted or lost.

## Key Features

- **Multiple File Type Support**: Out-of-the-box support for recovering JPEG, PNG, and PDF files with the ability to easily add more file types.
- **User-Friendly Interface**: Simple command-line prompts guide the user through the recovery process, making it accessible to users with varying levels of technical expertise.
- **Flexible and Extensible**: Designed for easy extension, allowing developers to add support for additional file types by defining new byte signatures.

## Tools and Libraries Used

- **Python**: The core language used for developing this application.
- **itertools, sys, os**: Essential Python libraries for efficient looping, system operations, and file management.
- **time**: Used to manage timing for the loading animation.
- **threading**: Enables concurrent execution of the loading animation and the scanning process, improving the tool's efficiency.

## How to Use

1. Clone the repository or download the source code to your local machine.
2. Open your terminal or command prompt.
3. Navigate to the directory containing the Data Recovery tool.
4. Run the tool using Python with the command: `python main.py`
5. Follow the on-screen prompts to select the drive, specify the file type to recover, and provide the destination directory for recovered files.

## Extending Data Recovery

To add support for additional file types:

1. Open `recover.py`.
2. Locate the `get_byte_sequences` function.
3. Add a new entry to the `sequences` dictionary with the key as the file extension (e.g., "txt") and the value as a tuple containing the byte start and end sequences for the file type.

Example:

```python
"txt": (b'START_SEQUENCE', b'END_SEQUENCE'),
