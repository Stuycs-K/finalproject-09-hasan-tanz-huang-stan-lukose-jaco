import java.util.ArrayList;
String alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
char[] letters = new char[9];
String[] r = {"EKMFLGDQVZNTOWYHXUSPAIBRCJ", "AJDKSIRUXBLHWTMCQGZNPYFVOE", "BDFHJLCPRTXVZNYEIWGAKMUSQO"};
String reflect = "YRUHQSLDPXNGOKMIEBFZCWVJAT";
Character[] rollVals={'E', 'V'};
ArrayList<Integer> reflector = new ArrayList<>();
String rotors="AAC"; //Make an area to decide the rotor combination
boolean showSteps = false;
String input = "";
String output = "";
ArrayList<key> keys = new ArrayList<>();
boolean selectingRotor = false;
int selectedRotorIndex = -1;
// Something about reflector, find out later
class key {
  char letter;
  float x;
  float y;
  color c;

  // Constructor
  public key(char letter, float x, float y, color c){
    this.letter = letter;
    this.x = x;
    this.y = y;
    this.c = c;
  }
}
void keyboard(String alpha){
  float padding = 60;
  float spacing = (width - 2 * padding) / ((alpha.length()/2)-1);
  float y = 100;
  for (int j = 0; j < 2; j ++) {
    for (int i = 0; i < alpha.length()/2; i++) {
      int k=(13*j) + i;
      float x = padding + i*spacing;
      key chr = new key(alpha.charAt(k), x, y, color(255, 255, 255));
      keys.add(chr);
      drawLetter(chr.letter, chr.x, chr.y, 30, 240);
    }
    y += 2*padding;
  }
}
void setup() {
  size(1000, 600);         // Set window size
  background(255); // Set background color
  textAlign(CENTER, CENTER);
  textSize(24);
  fill(0);
  text("TAB to show Encryption Steps", 160, 20);
  for (int i = 0; i < reflect.length(); i++){
    reflector.add(index(reflect.charAt(i)));
  }
  keyboard(alphabet);
  drawIOBoxes(30, 410);
}
void changeKey(){
  for (int i = 0; i < keys.size(); i ++){
    key let = keys.get(i);
    if (let.letter == letters[letters.length - 1]){
      let.c = color(252, 230, 86);
      drawLetter(let.letter, let.x, let.y, 30, let.c);
      //delay(1000);
      //drawLetter(let.letter, let.x, let.y, 30, color(240));
    }
    else if (let.c == color(252, 230, 86)){
      drawLetter(let.letter, let.x, let.y, 30, color(240));
    }
  }
}
void keyPressed(){
  Character chrtr = Character.toUpperCase(key);
  if (chrtr == BACKSPACE || chrtr == DELETE) {
    if (input.length() > 0 && output.length() > 0) {
      input = input.substring(0, input.length()-1);
      output = output.substring(0, output.length()-1);
      rotors = update(rotors, true);
    }

  }
  else if(chrtr == TAB){
    showSteps = !showSteps;
    steps(showSteps);
  }
  else if(Character.isLetter(chrtr)) {
    letters[0] = chrtr;
    encode(letters[0], "", rotors); //call it directly to set the letters
    changeKey();
    rotors = update(rotors, false);
    if (showSteps){
      steps(showSteps);
    }
  }
  drawIOBoxes(30, 410);
}

void draw() {
  drawRotors();
//  //drawLetter(letters[0], 200, height/2);
//  //drawLetter(letters[1], 600, height/2);
}

void drawLetter(char letter, float xcor, float ycor, float radius, color c) {
  fill(c);
  stroke(0);
  ellipse(xcor, ycor, 2*radius, 2*radius);
  fill(0);
  text(letter, xcor, ycor);
}

void drawArrow(float x1, float y1, float x2, float y2) {
  stroke(0);
  line(x1, y1, x2, y2);
  triangle(x2, y2+10, x2, y2-10, x2+10, y2);
}

void drawIOBoxes(float pad, float y) {
  print(width);
  float boxWidth = 400;
  float boxHeight = 100;
  float x2=width-boxWidth-pad;

  fill(255);
  stroke(0);
  rect(pad, y,  boxWidth, boxHeight);
  fill(0);
  text(input, pad+boxWidth/2, y+boxHeight/2);

  fill(255);
  stroke(0);
  rect(x2, y,  boxWidth, boxHeight);
  fill(0);
  print(1);
  text(output, x2+boxWidth/2, y+boxHeight/2);
}

void drawRotors() {
  textSize(32);
  for (int i = 0; i < 3; i++) {
    float x = 420 + i * 80;
    if (selectingRotor && selectedRotorIndex == i) {
      fill(color(180, 220, 255));
    } 
    else {
      fill(240);
    }
    stroke(0);
    rect(x-20, 265, 40, 60);
    fill(0);
    text(rotors.charAt(i), x, 295);
  }
}

int index(char c) {
  c = Character.toUpperCase(c);
  return mod26((int)c - (int)('A'));
}
int mod26(int num){
    return (num + 26) % 26;
}
char c(int num){
  return (char)(num + (int)('A'));
}

char encode(char chr, String plugboard, String rotors) {
  int order = index(chr);
  input += chr;
  // pb function, ignore plugboard
  int pos = 1;
  for (int i = r.length - 1; i > -1; i--) {
    //println(index(rotors.charAt(i)));
    order = index(r[i].charAt(mod26(order + index(rotors.charAt(i))))) - index(rotors.charAt(i));
    order = mod26(order);
    letters[pos] = c(order);
    pos += 1;
    //println((char)((int)('A')+order));
  }
  order = reflector.get(order);
  letters[pos] = c(order);
  pos += 1;
  for (int i = 0; i < r.length; i ++){
    //println(index(rotors.charAt(i)));
    //println((char)((order + index(rotors.charAt(i)) + (int)('A'))));
    order=r[i].indexOf((char)((order + index(rotors.charAt(i))) %26 + (int)('A')))-index(rotors.charAt(i));
    order = mod26(order);
    letters[pos] = c(order);
    pos += 1;
    //println((char)((int)('A')+order));
  }//
  letters[pos] = c(order);
  output += letters[letters.length-1];
  return c(order);
}

String update(String rotors, boolean reverse) {
  Character[] roll = rollVals.clone();
  int inc = 1;
  if (reverse){
    for (int i = 0; i < rollVals.length; i ++){
      roll[i] = (char)(c(index(rollVals[i])+1));
    }
    inc = -1;
  }
  if (rotors.charAt(2) == roll[1]) {
    rotors = rotors.substring(0,1) + (char)(c(index(rotors.charAt(1))+inc)) + (char)(rotors.charAt(2));
    print(rotors);
    if (rotors.charAt(1) == roll[0]) {
      rotors = c(index(rotors.charAt(0))+inc) + rotors.substring(1);
      print(rotors);
    }
  }
  rotors = rotors.substring(0,2) + c(index(rotors.charAt(2))+inc);
  print(rotors);
  return rotors;
}

void steps(boolean show){
  float y = 360;
  float padding = 60;
  float spacing = (width - 2 * padding) / (7);
  float radius = 30;
  color col = 240; 
  if (show){
    print("wtf");
    for (int i = 0; i < letters.length; i++) {
      float x = padding + i*spacing;
      drawLetter(letters[i], x, y, radius, col);
      if (i < letters.length-2) {
        float x2 = padding + (i+1) * spacing;
        drawArrow(x+30, y, x2-40, y);
      }
    }
  }
  else{
    fill(255); // white color, same as background
    noStroke();
    rect(0, y-radius, width, y+radius); // covers up that area
  }
}
