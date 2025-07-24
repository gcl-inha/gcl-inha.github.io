import os
from PIL import Image

def resize_to_exact_size(
    input_dir: str,
    output_dir: str,
    target_width: int,
    target_aspect_ratio: float
):
    os.makedirs(output_dir, exist_ok=True)
    valid_extensions = ('.jpg', '.jpeg', '.png')

    target_height = int(target_width / target_aspect_ratio)

    for filename in sorted(os.listdir(input_dir)):
        if not filename.lower().endswith(valid_extensions):
            continue

        input_path = os.path.join(input_dir, filename)
        output_filename = os.path.splitext(filename)[0] + ".png"
        output_path = os.path.join(output_dir, output_filename)

        try:
            img = Image.open(input_path).convert("RGB")
        except Exception as e:
            print(f"[오류] {filename} 열기 실패 - {e}")
            continue

        # 비율 보존 없이 강제 리사이즈
        resized_img = img.resize((target_width, target_height), Image.LANCZOS)

        print(input_path, img.width/img.height)

        try:
            resized_img.save(output_path, "PNG")
        except Exception as e:
            print(f"[오류] 저장 실패: {filename} - {e}")

# 사용 예시
if __name__ == "__main__":
    resize_to_exact_size(
        input_dir="image2",            # 입력 폴더
        output_dir="output2",           # 출력 폴더
        target_width=800,              # 원하는 너비
        target_aspect_ratio=2.5 / 1      # 예: 4:3 → height = 384
    )
