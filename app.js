// app.js - basic p5.js image RGB manipulator
let src;
let out;
let rSlider, gSlider, bSlider;

function preload() {
    // sample image hosted on p5js site
    src = loadImage('https://p5js.org/assets/learn/space.jpg');
}

function setup() {
    createCanvas(src.width, src.height + 80);
    pixelDensity(1);
    out = createImage(src.width, src.height);

    rSlider = createSlider(0, 200, 100);
    gSlider = createSlider(0, 200, 100);
    bSlider = createSlider(0, 200, 100);

    const sliderW = Math.min(300, src.width - 140);
    rSlider.style('width', sliderW + 'px');
    gSlider.style('width', sliderW + 'px');
    bSlider.style('width', sliderW + 'px');

    rSlider.position(10, src.height + 10);
    gSlider.position(10, src.height + 35);
    bSlider.position(10, src.height + 60);

    textSize(12);
    noSmooth();
}

function draw() {
    background(30);

    src.loadPixels();
    out.loadPixels();

    const rMul = rSlider.value() / 100;
    const gMul = gSlider.value() / 100;
    const bMul = bSlider.value() / 100;

    for (let i = 0; i < src.pixels.length; i += 4) {
        out.pixels[i]   = constrain(src.pixels[i]   * rMul, 0, 255); // R
        out.pixels[i+1] = constrain(src.pixels[i+1] * gMul, 0, 255); // G
        out.pixels[i+2] = constrain(src.pixels[i+2] * bMul, 0, 255); // B
        out.pixels[i+3] = src.pixels[i+3]; // A
    }

    out.updatePixels();
    image(out, 0, 0);

    fill(255);
    noStroke();
    text('R: ' + rSlider.value() + '%', rSlider.x + rSlider.width + 12, src.height + 28);
    text('G: ' + gSlider.value() + '%', gSlider.x + gSlider.width + 12, src.height + 53);
    text('B: ' + bSlider.value() + '%', bSlider.x + bSlider.width + 12, src.height + 78);
}