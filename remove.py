import os
import requests

API_KEY = "cPYLFTp76GhsSGQuvFGWkUcM"
ENDPOINT = "https://api.remove.bg/v1.0/removebg"

def remove_bg_batch(input_folder, output_folder="no_albahaca_sin_fondo_resultado"):
    os.makedirs(output_folder, exist_ok=True)

    for file in os.listdir(input_folder):
        if file.lower().endswith((".png", ".jpg", ".jpeg")):
            input_path = os.path.join(input_folder, file)
            output_path = os.path.join(output_folder, f"no_bg_{file}.png")

            with open(input_path, "rb") as img:
                res = requests.post(
                    ENDPOINT,
                    files={"image_file": img},
                    data={"size": "auto"},
                    headers={"X-Api-Key": API_KEY},
                )

            if res.status_code == 200:
                with open(output_path, "wb") as out:
                    out.write(res.content)
                print(f"✔ Procesado: {file}")
            else:
                print(f"❌ Error con {file}: {res.text}")


if __name__ == "__main__":
    remove_bg_batch("no_albahaca sin fondo/")
