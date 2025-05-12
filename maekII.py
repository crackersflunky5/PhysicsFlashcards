# Complete Python script with fullscreen functionality support in generated HTML

import os

def generate_flashcard_grid_with_fullscreen(pairs_folder, output_html_path):
    pair_folders = sorted([
        name for name in os.listdir(pairs_folder)
        if os.path.isdir(os.path.join(pairs_folder, name))
    ])

    html_start = """
<!DOCTYPE html>
<html lang='en'>
<head>
  <meta charset='UTF-8' />
  <meta name='viewport' content='width=device-width, initial-scale=1.0' />
  <title>Image Flashcards</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      background-color: #f0f4f8;
      display: flex;
      justify-content: center;
      align-items: center;
      flex-direction: column;
      padding: 20px;
      margin: 0;
    }
    .grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
      gap: 20px;
      width: 100%;
      max-width: 1000px;
    }
    .flashcard {
      perspective: 1000px;
      position: relative;
    }
    .flashcard-inner {
      position: relative;
      width: 100%;
      padding-top: 100%;
      transform-style: preserve-3d;
      transition: transform 0.6s;
      cursor: pointer;
    }
    .flashcard.flipped .flashcard-inner {
      transform: rotateY(180deg);
    }
    .flashcard-front,
    .flashcard-back {
      position: absolute;
      top: 0;
      left: 0;
      right: 0;
      bottom: 0;
      backface-visibility: hidden;
      display: flex;
      align-items: center;
      justify-content: center;
      border-radius: 10px;
      padding: 10px;
      background: white;
      box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
      overflow: hidden;
    }
    .flashcard-front img,
    .flashcard-back img {
      max-width: 100%;
      max-height: 100%;
      object-fit: contain;
    }
    .flashcard-back {
      transform: rotateY(180deg);
      background-color: #e0f7fa;
    }
    .expand-btn {
      position: absolute;
      bottom: 8px;
      right: 8px;
      background: rgba(255, 255, 255, 0.9);
      border: none;
      border-radius: 4px;
      cursor: pointer;
      font-size: 1.2rem;
      padding: 2px 6px;
      z-index: 2;
    }
    .modal {
      display: flex;
      align-items: center;
      justify-content: center;
      position: fixed;
      top: 0; left: 0;
      width: 100vw; height: 100vh;
      background: rgba(0, 0, 0, 0.9);
      z-index: 999;
      flex-direction: column;
    }
    .modal.hidden {
      display: none;
    }
    .modal img {
      max-width: 90vw;
      max-height: 80vh;
      object-fit: contain;
    }
    #close-modal {
      position: absolute;
      top: 20px;
      right: 30px;
      color: white;
      font-size: 2rem;
      cursor: pointer;
    }
  </style>
</head>
<body>
  <h1>Image Flashcards</h1>
  <div class='grid'>"""

    html_cards = ""
    for folder in pair_folders:
        q_path = f"{folder}/question.png"
        a_path = f"{folder}/answer.png"
        html_cards += f"""
    <div class='flashcard'>
      <div class='flashcard-inner'>
        <div class='flashcard-front'>
          <img src='{q_path}' alt='Question'>
          <button class='expand-btn'>🔍</button>
        </div>
        <div class='flashcard-back'>
          <img src='{a_path}' alt='Answer'>
        </div>
      </div>
    </div>"""

    html_end = """
  </div>

  <div id='fullscreen-modal' class='modal hidden'>
    <span id='close-modal'>&times;</span>
    <img id='fullscreen-img' src='' alt='Flashcard' />
  </div>

  <script>
    document.querySelectorAll('.flashcard').forEach(card => {
      card.addEventListener('click', () => {
        card.classList.toggle('flipped');
      });
    });

    document.querySelectorAll('.expand-btn').forEach(btn => {
      btn.addEventListener('click', (e) => {
        e.stopPropagation();
        const img = btn.closest('.flashcard-front').querySelector('img');
        document.getElementById('fullscreen-img').src = img.src;
        document.getElementById('fullscreen-modal').classList.remove('hidden');
      });
    });

    document.getElementById('close-modal').addEventListener('click', () => {
      document.getElementById('fullscreen-modal').classList.add('hidden');
    });

    document.getElementById('fullscreen-modal').addEventListener('click', () => {
      document.getElementById('fullscreen-modal').classList.add('hidden');
    });
  </script>
</body>
</html>"""

    with open(output_html_path, "w", encoding="utf-8") as f:
        f.write(html_start + html_cards + html_end)

    print(f"✅ HTML with fullscreen flashcards generated: {output_html_path}")

# Example usage:
# generate_flashcard_grid_with_fullscreen("/path/to/image_flashcard_pairs", "output.html")


# Save the script to a .py file
script_file_path = "fullscreen_flashcards.py"


script_file_path
