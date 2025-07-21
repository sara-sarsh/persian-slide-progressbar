from PIL import Image, ImageDraw, ImageFont
import arabic_reshaper
from bidi.algorithm import get_display

def prepare_persian_text(text):
    """
    Prepare Persian text for proper rendering.
    """
    reshaped_text = arabic_reshaper.reshape(text)
    return get_display(reshaped_text)

def get_slide_progress(chapters, chapter_names, slides_per_chapter, font_path):
    """
    Generate progress bar images for slides with chapter names and bullet status.

    Parameters:
        chapters (int): Number of chapters.
        chapter_names (list): List containing the names of the chapters.
        slides_per_chapter (list): List containing the number of slides in each chapter.
        font_path (str): Path to the Persian font file.
    """
    total_slides = sum(slides_per_chapter)
    slide_count = 1

    for chapter_index, slides_in_chapter in enumerate(slides_per_chapter):
        for slide_number in range(1, slides_in_chapter + 1):
            # Create a blank transparent image
            width, height = 1920, 57
            image = Image.new("RGBA", (width, height), (255, 255, 255, 0))
            draw = ImageDraw.Draw(image)

            # Set font size and type
            try:
                font = ImageFont.truetype(font_path, 30)  # Increase font size for visibility
            except:
                font = ImageFont.load_default()

            # Calculate dynamic x_start based on image width, with extra space for the first chapter text
            extra_padding = 150  # Additional space for the first chapter text
            x_start = width - extra_padding  # Adjust padding from the right edge
            # y_text = 2
            y_bullet = 50
            circle_diameter = 10
            spacing = 15

            # Calculate total width occupied by bullets for the largest chapter
            total_bullet_width = (circle_diameter + spacing) * max(slides_per_chapter) - spacing

            # Initialize positions for chapter names
            chapter_x_positions = []

            # Draw chapter names and bullets
            for idx, chapter_name in enumerate(chapter_names):
                reshaped_name = prepare_persian_text(chapter_name)
                # Calculate the x position for the current chapter
                chapter_x = x_start - idx * (total_bullet_width + 100)  # Adjust spacing between chapters
                chapter_x_positions.append(chapter_x)

                # Adjust the chapter_x position to center the text above the bullets
                chapter_center_x = chapter_x - (slides_per_chapter[idx] - 1) * (circle_diameter + spacing) // 2

                # Calculate text width for right-to-left alignment
                text_bbox = draw.textbbox((0, 0), reshaped_name, font=font)
                text_width = text_bbox[2] - text_bbox[0]
                text_x = chapter_center_x - (text_width // 2)  # Center the text above the bullets

                # Draw chapter name centered above bullets
                # draw.text((text_x, y_bullet - circle_diameter - 30), reshaped_name, fill="black", font=font)
                draw.text((text_x, y_bullet - circle_diameter - 50), reshaped_name, fill="black", font=font)

            # Draw progress bullets for each chapter
            for idx, slides in enumerate(slides_per_chapter):
                chapter_x = chapter_x_positions[idx]
                for slide_idx in range(slides):
                    # Calculate x position for the current bullet
                    bullet_x = chapter_x - slide_idx * (circle_diameter + spacing)

                    # Determine the color based on the current slide
                    if slide_count == slide_idx + 1 + sum(slides_per_chapter[:idx]):
                        color = "#fb6f92"  # Highlight the current slide
                    elif slide_idx + 1 < slide_count - sum(slides_per_chapter[:idx]):
                        color = "#333F4C"  # Slides already visited
                    else:
                        color = "#59747B"  # Slides yet to be visited

                    # Draw the bullet as a circle
                    draw.ellipse(
                        [
                            (bullet_x, y_bullet - circle_diameter // 2),
                            (bullet_x + circle_diameter, y_bullet + circle_diameter // 2),
                        ],
                        fill=color,
                    )

            # Save image with slide number as the name
            image.save(f"slide_{slide_count}.png", dpi=(300, 300))
            slide_count += 1

# Example usage
if __name__ == "__main__":
    font_path = "/Users/sara/Library/Fonts/X Zar Bold.ttf"  # Path to Persian font

    chapters = int(input("Enter the number of chapters: "))
    chapter_names = []
    slides_per_chapter = []

    for i in range(chapters):
        chapter_name = input(f"Enter the name of chapter {i + 1}: ")
        chapter_names.append(chapter_name)
        slides = int(input(f"Enter the number of slides in chapter '{chapter_name}': "))
        slides_per_chapter.append(slides)

    get_slide_progress(chapters, chapter_names, slides_per_chapter, font_path)
    