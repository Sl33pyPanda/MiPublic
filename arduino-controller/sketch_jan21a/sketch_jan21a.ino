int datafromUser=0;
const byte numChars = 100;
char receivedChars[numChars];   // an array to store the received data

void setup() {
  pinMode( 13 , OUTPUT );
  Serial.begin(115200);
  Serial.println("<Controller is ready>");
}


void loop() {
    getParam();
}

void getParam() {
    static byte ndx = 0;
    char endMarker = '\n';
    char rc;
    char * pch;  
    int x , y ;
   
    while (Serial.available() > 0) {
        rc = Serial.read();

        if (rc != endMarker) {
              x = Serial.parseInt();
              y = Serial.parseInt();
              Serial.print(x);
              Serial.print(":");
              Serial.println(y);
//            receivedChars[ndx] = rc;
//            ndx++;
        }
        else {
//            receivedChars[ndx] = '/0' ;
//            pch = strtok (receivedChars,":");         // get first token            
//            Serial.println(pch);          // print it
//            pch = strtok (NULL, ":*");     // get next token
//            Serial.println(pch);    
//            ndx = 0;
        }
    }
}
