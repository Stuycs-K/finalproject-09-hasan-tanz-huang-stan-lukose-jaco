import java.util.ArrayList;
char[] input = new char[1];
char[] output = new char[1];
String[] r = {"EKMFLGDQVZNTOWYHXUSPAIBRCJ", "AJDKSIRUXBLHWTMCQGZNPYFVOE", "BDFHJLCPRTXVZNYEIWGAKMUSQO"};
String reflect = "YRUHQSLDPXNGOKMIEBFZCWVJAT";
ArrayList<Integer> reflector = new ArrayList<>();
String rotors="AAC";
boolean pressed = false;
// Something about reflector, find out later

void setup() {
  size(800, 600);         // Set window size
  background(255); // Set background color
  textAlign(CENTER, CENTER);
  textSize(32);
  for (int i = 0; i < reflect.length(); i++){
    reflector.add(index(reflect.charAt(i)));
  }
  drawLetter(input[0], 200, height/2);
  drawLetter(output[0], 600, height/2);
  drawArrow(240, height/2, 550, height/2);
  
}

void keyPressed(){
  input[0] = Character.toUpperCase(key);
  output[0]=encode(input[0], "", rotors);
  char newChar= (char)((int)rotors.charAt(rotors.length()-1)+1);
  rotors= rotors.substring(0, rotors.length()-1) + newChar;
  println(rotors.length());
}

void draw() {
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
  return mod26((int)c - (int)('A'));
}
int mod26(int num){
    return (num + 26) % 26;
}

char encode(char input, String plugboard, String rotors) {
  int order = index(input);
  // pb function, ignore plugboard
  for (int i = r.length - 1; i > -1; i--) {
    //println(index(rotors.charAt(i)));
    order = index(r[i].charAt(mod26(order + index(rotors.charAt(i))))) - index(rotors.charAt(i));
    order %= 26;
    //println((char)((int)('A')+order));
  }
  order = reflector.get(order);
  for (int i = 0; i < r.length; i ++){
    //println(index(rotors.charAt(i)));
    //println((char)((order + index(rotors.charAt(i)) + (int)('A'))));
    order=r[i].indexOf((char)((order + index(rotors.charAt(i))) %26 + (int)('A')))-index(rotors.charAt(i));
    order = ((order % 26) + 26) % 26;
    //println((char)((int)('A')+order));  
  }//
  return (char) (order+(int)('A'));
}
