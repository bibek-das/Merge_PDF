import os
import subprocess
import sys

def ensure_pypdf2_installed():
    try:
        import PyPDF2
    except ImportError:
        print("PyPDF2 is not installed. Installing it now...")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "PyPDF2"])
            print("PyPDF2 has been successfully installed.")
        except Exception as e:
            print(f"Failed to install PyPDF2. Error: {e}")
            sys.exit(1)

def merge_pdfs_in_cwd(output_path):
    try:
        import PyPDF2

        # Get all PDF files in the current working directory
        pdf_files = [file for file in os.listdir(os.getcwd()) if file.endswith('.pdf')]

        if not pdf_files:
            print("No PDF files found in the current working directory.")
            return

        # Sort files lexicographically
        pdf_files.sort()
        print(f"PDF files to be merged (lexicographical order): {pdf_files}")

        pdf_writer = PyPDF2.PdfWriter()

        # Merge PDFs
        for pdf_file in pdf_files:
            with open(pdf_file, 'rb') as file:
                pdf_reader = PyPDF2.PdfReader(file)
                for page in pdf_reader.pages:
                    pdf_writer.add_page(page)

        # Write the merged PDF to the output file
        with open(output_path, 'wb') as output_file:
            pdf_writer.write(output_file)
        
        print(f"Merged PDF saved as: {output_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Ensure PyPDF2 is installed
    ensure_pypdf2_installed()

    # Ask the user for the output file name
    output_file_name = input("Enter the name for the merged PDF (e.g., merged.pdf): ").strip()
    if not output_file_name.endswith('.pdf'):
        print("Invalid file name. The output file name must end with '.pdf'.")
    else:
        merge_pdfs_in_cwd(output_file_name)
