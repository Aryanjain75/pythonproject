import os
import PyPDF2
import tkinter as tk
from tkinter import filedialog


class PDFMerger:
    def __init__(self, master):
        self.master = master
        self.master.title("PDF Merger")
        self.master.geometry("300x150")

        self.file_list = []

        self.label = tk.Label(self.master, text="Select PDF files to merge:")
        self.label.pack(pady=10)

        self.button = tk.Button(self.master, text="Browse files", command=self.browse_files)
        self.button.pack(pady=5)

        self.merge_button = tk.Button(self.master, text="Merge files", command=self.merge_files)
        self.merge_button.pack(pady=10)

        self.master.mainloop()

    def browse_files(self):
        filetypes = [("PDF files", "*.pdf")]
        files = filedialog.askopenfilenames(filetypes=filetypes)
        self.file_list = list(files)

    def merge_files(self):
        if not self.file_list:
            return

        output_filename = filedialog.asksaveasfilename(defaultextension=".pdf")
        if not output_filename:
            return

        output_pdf = PyPDF2.PdfFileWriter()

        for filename in self.file_list:
            with open(filename, "rb") as input_pdf:
                input_pdf_reader = PyPDF2.PdfFileReader(input_pdf)
                for page_num in range(input_pdf_reader.getNumPages()):
                    output_pdf.addPage(input_pdf_reader.getPage(page_num))

        with open(output_filename, "wb") as output_pdf_file:
            output_pdf_writer = PyPDF2.PdfWriter(output_pdf_file)
            output_pdf_writer.write(output_pdf)

        self.file_list = []
        tk.messagebox.showinfo("PDF Merger", "Files merged successfully.")


if __name__ == "__main__":
    root = tk.Tk()
    app = PDFMerger(root)
