// app.js - basic p5.js image RGB manipulator
let img;
let rSlider, gSlider, bSlider;

function setup() {
  // temporary canvas before image loads
  const ctx = createCanvas(400, 200);
  ctx.elt.getContext("2d", { willReadFrequently: true });
  background(30);

  const input = document.getElementById("imgInput");
  input.addEventListener("change", handleFile);


    // Create sliders if they don't exist yet
    if (!rSlider) {
        rSlider = createSlider(0, 200, 100);
        gSlider = createSlider(0, 200, 100);
        bSlider = createSlider(0, 200, 100);
    }




  noLoop(); // don't run draw() until we have an image
}

function handleFile(event) {
  const file = event.target.files[0];
  if (!file) return;

  const reader = new FileReader();

  reader.onload = (e) => {
    // e.target.result is a dataURL
    loadImage(e.target.result, (loadedImage) => {
      img = loadedImage;
      console.log("Image loaded!", img);

      // Now that we know image size, resize canvas
      resizeCanvas(img.width, img.height + 80);
      pixelDensity(1);

        const sliderW = Math.min(300, img.width - 140);
        rSlider.style('width', sliderW + 'px');
        gSlider.style('width', sliderW + 'px');
        bSlider.style('width', sliderW + 'px');

        rSlider.position(10, img.height + 10);
        gSlider.position(10, img.height + 35);
        bSlider.position(10, img.height + 60);

      noSmooth();
      textSize(12);

      loop(); // start draw() now that everything is ready
    });
  };

  reader.readAsDataURL(file);
}

function draw() {
  background(30);

  if (!img) {
    fill(255);
    noStroke();
    text('Choose an image with the file input.', 10, 20);
    return;
  }

  img.loadPixels();
  const rMul = rSlider.value() / 100;
  const gMul = gSlider.value() / 100;
  const bMul = bSlider.value() / 100;

  for (let i = 0; i < img.pixels.length; i += 4) {
    img.pixels[i]   = constrain(img.pixels[i]   * rMul, 0, 255); // R
    img.pixels[i+1] = constrain(img.pixels[i+1] * gMul, 0, 255); // G
    img.pixels[i+2] = constrain(img.pixels[i+2] * bMul, 0, 255); // B
    // img.pixels[i+3] is alpha, leave as-is
  }

  img.updatePixels();
  image(img, 0, 0);

  fill(255);
  noStroke();
  text('R: ' + rSlider.value() + '%', rSlider.x + rSlider.width + 12, img.height + 28);
  text('G: ' + gSlider.value() + '%', gSlider.x + gSlider.width + 12, img.height + 53);
  text('B: ' + bSlider.value() + '%', bSlider.x + bSlider.width + 12, img.height + 78);
}
