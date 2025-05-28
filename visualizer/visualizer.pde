char[] input = new char[1];
char[] output = new char[1];
String[] r = {"EKMFLGDQVZNTOWYHXUSPAIBRCJ", "AJDKSIRUXBLHWTMCQGZNPYFVOE", "BDFHJLCPRTXVZNYEIWGAKMUSQO"};
String reflect = "YRUHQSLDPXNGOKMIEBFZCWVJAT";
// Something about reflector, find out later

void setup() {
  size(800, 600);         // Set window size
  background(255); // Set background color
  textAlign(CENTER, CENTER);
  textSize(32);

  drawLetter(input[0], 200, height/2);
  drawLetter(output[0], 600, height/2);
  drawArrow(240, height/2, 550, height/2);
  
}

void draw() {
  if (keyPressed) {
    input[0] = key;
  }
  
  drawLetter(input[0], 200, height/2);
  drawLetter(output[0], 600, height/2);
}

void drawLetter(char letter, float xcor, float ycor) {
  fill(240);
  stroke(0);
  ellipse(xcor, ycor, 80, 80);
  fill(0);
  text(letter, xcor, ycor);
}

void drawArrow(float x1, float y1, float x2, float y2) {
  stroke(0);
  line(x1, y1, x2, y2);
  triangle(x2, y2+10, x2, y2-10, x2+10, y2);
}

int index(char c) {
  c = Character.toUpperCase(c);
  return ((int)c - (int)('A')) % 26;
}

char encode(char input, String plugboard, String rotors) {
  int order = index(input);
  // pb function, ignore plugboard
  for (int i = r.length - 1; i > -1; i--) {
    order = r[i].charAt((order + rotors.charAt(i)) % 26) - rotors.charAt(i);
    order %= 26;
  }
  // skipping reflector
}
