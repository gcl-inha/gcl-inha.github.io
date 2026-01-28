import os
from PIL import Image

def process_images(
    input_dir: str,
    output_dir: str,
    target_width: int,
    target_aspect_ratio: float
):
    os.makedirs(output_dir, exist_ok=True)
    valid_extensions = ('.jpg', '.jpeg', '.png')

    target_height = int(target_width / target_aspect_ratio)

    for filename in os.listdir(input_dir):
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

        # 원본 사이즈
        original_w, original_h = img.size
        original_aspect = original_w / original_h

        # 목표 영역 안에 들어가도록 리사이즈 (잘림 없이)
        if original_aspect > target_aspect_ratio:
            # 이미지가 더 넓음 → 너비 기준 맞추고 높이는 여유 있음
            scale = target_width / original_w
        else:
            # 이미지가 더 높음 → 높이 기준 맞추고 너비는 여유 있음
            scale = target_height / original_h

        new_w = int(original_w * scale)
        new_h = int(original_h * scale)
        resized_img = img.resize((new_w, new_h), Image.LANCZOS)

        # 흰색 배경 캔버스 생성
        canvas = Image.new("RGB", (target_width, target_height), (255, 255, 255))

        # 중앙 배치
        offset_x = (target_width - new_w) // 2
        offset_y = (target_height - new_h) // 2
        canvas.paste(resized_img, (offset_x, offset_y))

        try:
            canvas.save(output_path, "PNG")
            print(f"✅ 저장 완료: {output_path}")
        except Exception as e:
            print(f"[오류] 저장 실패: {filename} - {e}")

# 사용 예시
if __name__ == "__main__":
    process_images(
        input_dir="ttt",           # 입력 폴더
        output_dir="output",          # 출력 폴더
        target_width=1600,             # 원하는 너비
        target_aspect_ratio=2/1   # 예: 4:3 비율 → height = 384
    )
