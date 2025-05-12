import fitz  # PyMuPDF
import pymupdf
import os

# Function to save image pairs from a PDF into a structured folder
def save_pdf_as_image_pairs(pdf_path, target_directory):
    os.makedirs(target_directory, exist_ok=True)
    doc = fitz.open(pdf_path)

    for i in range(0, len(doc) - 1, 2):
        pair_folder = os.path.join(target_directory, f"pair_{(i//2) + 1:03}")
        os.makedirs(pair_folder, exist_ok=True)

        # Save odd-numbered page as question
        question_path = os.path.join(pair_folder, "question.png")
        doc[i].get_pixmap(dpi=150).save(question_path)

        # Save even-numbered page as answer
        answer_path = os.path.join(pair_folder, "answer.png")
        doc[i + 1].get_pixmap(dpi=150).save(answer_path)

    return target_directory

# Example usage: Save to /mnt/data/image_flashcard_pairs/
output_folder_path = "image_flashcard_pairs"
pdf_input_path = "Physics Flashcards.pdf"
save_pdf_as_image_pairs(pdf_input_path, output_folder_path)

output_folder_path
