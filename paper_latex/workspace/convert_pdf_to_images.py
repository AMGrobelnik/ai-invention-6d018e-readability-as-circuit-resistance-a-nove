#!/usr/bin/env python3
"""
Convert PDF pages to PNG images for visual inspection.
Uses pymupdf (fitz) for PDF rendering at 150 DPI.
"""

import os
import sys

# Try to import pymupdf
try:
    import fitz
except ImportError:
    try:
        import PyMuPDF as fitz
    except ImportError:
        print("Error: pymupdf not installed. Install with: pip install pymupdf")
        sys.exit(1)

def pdf_to_images(pdf_path, output_dir, dpi=150):
    """
    Convert each page of a PDF to a PNG image.
    
    Args:
        pdf_path: Path to the PDF file
        output_dir: Directory to save images
        dpi: Resolution in DPI (150 is good for visual inspection)
    """
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Open the PDF
    doc = fitz.open(pdf_path)
    print(f"PDF has {len(doc)} pages")
    
    # Convert each page
    zoom = dpi / 72  # 72 DPI is the base PDF resolution
    mat = fitz.Matrix(zoom, zoom)
    
    for page_num in range(len(doc)):
        page = doc[page_num]
        pix = page.get_pixmap(matrix=mat)
        
        # Save as PNG
        output_path = os.path.join(output_dir, f"page_{page_num + 1:02d}.png")
        pix.save(output_path)
        print(f"Saved page {page_num + 1}: {output_path}")
    
    doc.close()
    print(f"\nDone! Converted {len(doc)} pages to {output_dir}/")

if __name__ == "__main__":
    pdf_path = "./paper.pdf"
    output_dir = "./page_images"
    
    if not os.path.exists(pdf_path):
        print(f"Error: {pdf_path} not found!")
        sys.exit(1)
    
    pdf_to_images(pdf_path, output_dir, dpi=150)
