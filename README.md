# Sudoku Book Generator
_Sudoku Adventure_

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Directory Structure](#directory-structure)
- [Installation](#installation)
- [Usage](#usage)
  - [Generating Sudoku Puzzles](#generating-sudoku-puzzles)
  - [Creating a PDF Book](#creating-a-pdf-book)
- [Customization](#customization)
- [Dependencies](#dependencies)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Introduction

The Sudoku Book Generator is a Python application that allows you to create Sudoku puzzle books in PDF format. It generates unsolved 9x9 Sudoku puzzles and assembles them into a book format, including a front cover and an optional back cover. Whether you want to entertain yourself or create Sudoku puzzle books for your children, this tool simplifies the process.

## Features

- Generates 9x9 unsolved Sudoku puzzles.
- Creates a PDF book consisting of 101 Sudoku puzzles.
- Includes a front cover with a fancy title.
- Supports customization of the front and back covers.
- User-friendly and easy to use.

## Directory Structure

```
sudoku_book_generator/
│
├── generate_sudoku.py
├── create_pdf.py
├── main.py
├── output/
└── fonts/  # Optional: Place your custom fonts here
```

The project directory is organized as follows:

- `generate_sudoku.py`: Contains the code for generating Sudoku puzzles.
- `create_pdf.py`: Contains the code for creating PDFs, including the cover pages.
- `main.py`: The main application script that orchestrates the generation and merging of PDFs.
- `output/`: A directory where generated PDF files will be saved.
- `fonts/`: (Optional) Place your custom fonts here for styling.

## Installation

To use the Sudoku Book Generator, follow these steps:

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/yourusername/SudokuBookGenerator.git
   ```

2. Navigate to the project directory:

   ```bash
   cd SudokuBookGenerator
   ```

3. Install the required dependencies (PyPDF2 and reportlab):

   ```bash
   pip install PyPDF2 reportlab
   ```

## Usage

### Generating Sudoku Puzzles

To generate a set of 101 unsolved Sudoku puzzles, run the following command:

```bash
python generate_sudoku.py
```

The generated puzzles will be stored in the `output/` directory as `sudoku_puzzles.json`.

### Creating a PDF Book

1. Open the `main.py` script.

2. Customize the front cover title (line 29) as desired:

   ```python
   create_front_cover("Your Custom Title")
   ```

3. Run the main script to create the Sudoku puzzle book, including the front cover:

   ```bash
   python main.py
   ```

The resulting PDF file, `sudoku_book_with_covers.pdf`, will contain the front cover, 101 Sudoku puzzles, and an optional back cover (if provided).

## Customization

- **Front Cover**: You can customize the front cover by changing the title, adding images, or modifying the fonts and styles. Refer to the `create_front_cover` function in `main.py` for customization options.

- **Back Cover**: Customize the back cover by adding content such as thank you messages, contact information, or any other details in the `create_back_cover` function in `main.py`.

- **Fonts**: If you want to use custom fonts for the covers or any other elements, place your font files in the `fonts/` directory and adjust the font settings in the code accordingly.

## Dependencies

- PyPDF2
- reportlab

You can install these dependencies using `pip` as described in the [Installation](#installation) section.

## Contributing

Contributions to the Sudoku Book Generator project are welcome! If you have ideas for improvements, feature requests, or bug reports, please feel free to create issues or pull requests on the GitHub repository.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

Thanks to the authors and contributors of the PyPDF2 and reportlab libraries.
