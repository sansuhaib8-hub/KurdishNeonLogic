import os

project_name = "KurdishNeonLogic"
folders = ["lib", "assets", "network", "docs"]

for folder in folders:
    os.makedirs(folder, exist_ok=True)
    print(f"فۆڵدەری {folder} دروستکرا")

with open("lib/main_game.py", "w") as f:
    f.write('def init_game():\n    print("یارییەکە دەستی پێکرد")\n\nif __name__ == "__main__":\n    init_game()\n')

with open("README.md", "w") as f:
    f.write(f"# {project_name}\nیاری لۆجیکی ئۆنلاین.")

print("هەموو فایلەکان بەسەرکەوتوویی دروستکران.")
