import java.util.ArrayList;
String alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
char[] letters = new char[9];
String[] r = {"EKMFLGDQVZNTOWYHXUSPAIBRCJ", "AJDKSIRUXBLHWTMCQGZNPYFVOE", "BDFHJLCPRTXVZNYEIWGAKMUSQO"};
String reflect = "YRUHQSLDPXNGOKMIEBFZCWVJAT";
ArrayList<Integer> reflector = new ArrayList<>();
String rotors="AAC"; //Make an area to decide the rotor combination 
boolean pressed = false;
String input = "";
String output = "";
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
  ArrayList<key> keys = new ArrayList<>();
  float padding = 60;
  float spacing = (width - 2 * padding) / (alpha.length()/2);
  float y = 100;
  for (int j = 0; j < 2; j ++) {
    for (int i = 0; i < alpha.length()/2; i++) {
      int k=(13*j) + i;
      float x = padding + i*spacing;
      key chr = new key(alpha.charAt(k), x, y, color(255, 255, 255));
      keys.add(chr);
      drawLetter(chr.letter, chr.x, chr.y, 30);
    }
    y += 2*padding;
  }
}
void setup() {
  size(1000, 600);         // Set window size
  background(255); // Set background color
  textAlign(CENTER, CENTER);
  textSize(24);
  for (int i = 0; i < reflect.length(); i++){
    reflector.add(index(reflect.charAt(i)));
  }
  keyboard(alphabet);
  // Circle arrow details
  float padding = 60;
  float spacing = (width - 2 * padding) / (7);
  float y = 300;
  for (int i = 0; i < letters.length; i++) {
    float x = padding + i*spacing;
    if (i < letters.length-2) {
      float x2 = padding + (i+1) * spacing;
      drawArrow(x+30, y+60, x2-40, y+60);
    }
  }
  drawIOBoxes(30, 900, 410);
}

void keyPressed(){
  if (letters[0] == BACKSPACE || letters[0] == DELETE) {
    if (input.length() > 0 && output.length() > 0) {
      input = input.substring(0, input.length()-1);
      output = output.substring(0, output.length()-1);
    }

  }
  else {
    letters[0] = Character.toUpperCase(key);
    encode(letters[0], "", rotors); //call it directly to set the letters
    float y = 300;
    float padding = 60;
    float spacing = (width - 2 * padding) / (7);
    for (int i = 0; i < letters.length; i++) {
      float x = padding + i*spacing;
      drawLetter(letters[i], x, y+60, 30);
    }
    rotors = update(rotors);
    drawIOBoxes(30, 900, 410);
  }
}

void draw() {
//  //drawLetter(letters[0], 200, height/2);
//  //drawLetter(letters[1], 600, height/2);
}

void drawLetter(char letter, float xcor, float ycor, float radius) {
  fill(240);
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

void drawIOBoxes(float x1, float x2, float y) {
  float boxWidth = 80;
  float boxHeight = 40;
  
  fill(255);
  stroke(0);
  rect(x1, y,  boxWidth, boxHeight);
  fill(0);
  text(input, x1+boxWidth/2, y+boxHeight/2);
  
  fill(255);
  stroke(0);
  rect(x2, y,  boxWidth, boxHeight);
  fill(0);
  text(output, x2+boxWidth/2, y+boxHeight/2);
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

char encode(char input, String plugboard, String rotors) {
  int order = index(input);
  input += c(order);
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
  output += c(order);
  return c(order);
}

String update(String rotors) {
  if (rotors.charAt(2) == 'V') {
    rotors = rotors.substring(0,1) + (char)(c(index(rotors.charAt(1))+1)) + (char)(rotors.charAt(2));
    print(rotors);
    if (rotors.charAt(1) == 'E') {
      rotors = c(index(rotors.charAt(0))+1) + rotors.substring(1);
      print(rotors);
    }
  }
  rotors = rotors.substring(0,2) + c(index(rotors.charAt(2))+1);
  print(rotors);
  return rotors;
}
