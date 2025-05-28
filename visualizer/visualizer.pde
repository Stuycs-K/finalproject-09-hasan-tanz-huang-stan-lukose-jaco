String input = "A";
String output = "B";

void setup() {
  size(800, 600);         // Set window size
  background(255); // Set background color
  textAlign(CENTER, CENTER);
  textSize(32);
  
  drawLetter(input, 200, height/2);
  drawLetter(output, 600, height/2);
  
}

void drawLetter(String letter, float xcor, float ycor) {
  fill(240);
  stroke(0);
  ellipse(xcor, ycor, 80, 80);
  fill(0);
  text(letter, xcor, ycor);
}
