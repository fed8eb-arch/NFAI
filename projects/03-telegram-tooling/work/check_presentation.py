"""Check slide count and the presence of editable text in a PowerPoint file."""

import argparse
from pathlib import Path

from pptx import Presentation
from pptx.enum.shapes import MSO_SHAPE_TYPE
from pptx.exc import PackageNotFoundError
from zipfile import BadZipFile


def has_editable_text(shapes):
    for shape in shapes:
        if shape.has_text_frame and shape.text.strip():
            return True
        if shape.has_table and any(cell.text.strip() for cell in shape.table.iter_cells()):
            return True
        if shape.shape_type == MSO_SHAPE_TYPE.GROUP and has_editable_text(shape.shapes):
            return True
    return False


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("presentation", type=Path)
    parser.add_argument("--slides", type=int, required=True, help="Requested slide count")
    args = parser.parse_args()
    if args.slides < 1:
        parser.error("Expected a positive slide count")
    try:
        slides = Presentation(args.presentation).slides
        count = len(slides)
        editable = sum(has_editable_text(slide.shapes) for slide in slides)
    except (OSError, PackageNotFoundError, BadZipFile, ValueError, KeyError) as error:
        parser.exit(2, f"Cannot open PowerPoint file: {error}\n")
    print(f"Slides: {count}/{args.slides}")
    print(f"Slides with editable text: {editable}/{count}")
    return int(count != args.slides or editable == 0)


if __name__ == "__main__":
    raise SystemExit(main())
