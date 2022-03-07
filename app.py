from flask import Flask, render_template
import random

app = Flask(__name__)

# list of PXL images
images = [
    "https://www.pxl.be/Assets/website/pxl_algemeen/afbeeldingen/pxl_beeld_1.jpg",
    "https://www.pxl.be/Assets/website/pxl_algemeen/afbeeldingen/grotere_versie/1314_logo_pxl_bol.png",
    "https://www.pxl.be/Assets/website/pxl_algemeen/afbeeldingen/grotere_versie/1314_logo_pxl_hogeschool.png",
    "https://www.pxl.be/Assets/website/pxl_algemeen/afbeeldingen/grotere_versie/logo_PXL_University%20of%20applied%20sciences%20and%20arts.png",
    "https://www.pxl.be/Assets/website/pxl_algemeen/afbeeldingen/grotere_versie/1314_do_en_donts.jpg",
    "https://www.pxl.be/assets/afbeeldingen_algemeen/opleidingen/pxl_business/Business.jpg",
    "https://www.pxl.be/assets/afbeeldingen_algemeen/opleidingen/pxl_digital/applicatieontwikkeling.jpg",
    "https://www.pxl.be/assets/afbeeldingen_algemeen/opleidingen/pxl_education/Education.jpg",
    "https://www.pxl.be/assets/afbeeldingen_algemeen/opleidingen/pxl_tech/1314_groenmanagement_kbl1.jpg",
    "https://www.pxl.be/assets/afbeeldingen_algemeen/opleidingen/pxl_mad/grafischontwerp.jpg",
    "https://www.pxl.be/assets/afbeeldingen_algemeen/opleidingen/pxl_healthcare/Healthcare.jpg",
    "https://www.pxl.be/assets/afbeeldingen_algemeen/levenslang_leren/1314_vervolgopleidingen_405x270%20.jpg"
]


@app.route('/')
def index():
    url = random.choice(images)
    return render_template('index.html', url=url)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
