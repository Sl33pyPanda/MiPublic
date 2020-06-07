const uint8_t channels[] = {1,2,3,4,5,6,7,8,9,10,11,12,13}; // used Wi-Fi channels (available: 1-14)
const bool wpa2 = true; // WPA2 networks
const bool appendSpaces = true; // makes all SSIDs 32 characters long to improve performance

/*
  SSIDs:
  - don't forget the \n at the end of each SSID!
  - max. 32 characters per SSID
  - don't add duplicates! You have to change one character at least
*/
const char ssids[] PROGMEM = {"C+ita\n"
"r&=U>\n"
"1c<F~\n"
"$yZ!z\n"
";50s!\n"
"/x~d^\n"
"_;9%/\n"
";}0ot\n"
")B8*9\n"
"zZ=a)\n"
"<3>0Z\n"
"iyS%h\n"
"cOcJ{\n"
"s'yn/\n"
"&?*PD\n"
"x4Ksx\n"
"r*u<p\n"
"y%l9;\n"
"32qKq\n"
"A;Hsf\n"
"REy7l\n"
"xx9th\n"
"S>z1%\n"
"Z;+bN\n"
"UD/y2\n"
".mo=U\n"
"7(6Y8\n"
"GIx5D\n"
"du%*s\n"
"t<mn3\n"
"Ks.~A\n"
"uLYF$\n"
"xaM=B\n"
"z%/i5\n"
")P1h5\n"
"Zo(S5\n"
"@mUb)\n"
"mb>af\n"
"iY)sp\n"
"so~Y8\n"
"_f8?b\n"
"Jh596\n"
"gL7N=\n"
"!0X&;\n"
"5RDb_\n"
"o{OZQ\n"
"Bci`L\n"
",@Hkb\n"
"{(B?n\n"
"TAu]7\n"
"p6?NA\n"
"l0APH\n"
"Dfwk=\n"
"u],a;\n"
"^rC.Y\n"
"Dx`p~\n"
"9Ovee\n"
"zGmx_\n"
"Ib-rA\n"
"Z2G@i\n"
"e7env\n"
"YA?JE\n"
"C)ddV\n"
">kiB,\n"
"Q$qHo\n"
"2k4@F\n"
"G[{t9\n"
"`~kA6\n"
"P+?JF\n"
"5H;{3\n"
"aQ^Q'\n"
"#rM^#\n"
"Tt5Aq\n"
"hX8]=\n"
"a(1M<\n"
"FZ,p+\n"
";plKI\n"
"h><lY\n"
"/ipqD\n"
"Huwc5\n"
"K6S2R\n"
"$mRh2\n"
"Xzkua\n"
"o8Lca\n"
"aX'#s\n"
"Kz(21\n"
"6hY]y\n"
"hAF)%\n"
"MQXeb\n"
"lSH'r\n"
"5mH8u\n"
"ovcAI\n"
"<scCs\n"
"hzw6%\n"
"GMyZ@\n"
"O@k9'\n"
"G`;}E\n"
"D~rl.\n"
"]XRcP\n"
"YG]pY\n"
"'YR{x\n"
"AYJ.3\n"
"s?!2u\n"
"2XcQ*\n"
"H/U3v\n"
"}(?C+\n"
"*EDHo\n"
"8{Y;C\n"
"Y-F1C\n"
".8f0v\n"
"$BtXr\n"
",Qp<G\n"
"Iu4~c\n"
"U,M#V\n"
"L~&`n\n"
",]M?[\n"
"lb+Zf\n"
"vi)ak\n"
",e6U<\n"
"?nt$#\n"
"5Mgd?\n"
";{-Ov\n"
"42qb_\n"
".]TAG\n"
"T)Se]\n"
"h)*qn\n"
"Dru4F\n"
"F]D%)\n"
"K@I,v\n"
"ac1~;\n"
"H,#3S\n"
"f?I*M\n"
"ktK}N\n"
"U$bi^\n"
"#RiFL\n"
"'er^*\n"
"@5$X2\n"
"/~.?;\n"
"+Cx5I\n"
"^?I1.\n"
"7SS,(\n"
"z=;+w\n"
"H{Co%\n"
"2&rMg\n"
"A=tkF\n"
"#(;Qi\n"
">-9}m\n"
"qQo1Y\n"
"&Mp0s\n"
"Rsd;n\n"
"R)t7y\n"
"ANVuJ\n"
"V6eV.\n"
"~Z/5D\n"
"+;Fgh\n"
"CuR26\n"
"F<aKF\n"
"K@v&U\n"
"2qvV-\n"
"7])!Q\n"
"82;Q)\n"
";_]t}\n"
"BiO74\n"
"Xs<(X\n"
"rSsFS\n"
"M`008\n"
"4D#</\n"
"Z{1o!\n"
"U?}{g\n"
"JaBcb\n"
"ScwD]\n"
"*)Sio\n"
"7'&s-\n"
"gvF/V\n"
"zn61B\n"
"mCyu0\n"
"@EJ7d\n"
"6q09Q\n"
"_V0I,\n"
"{,XoJ\n"
"YC2RO\n"
"Lpy?a\n"
"6[Pd(\n"
"`w,eV\n"
"6')v=\n"
"'^xLY\n"
"@B-e0\n"
"P5p;U\n"
"]i?@~\n"
"'Hqvv\n"
"[w(g>\n"
"x&wV~\n"
"?F!VQ\n"
"S$J@N\n"
"s!n`J\n"
"B`n]o\n"
"q0n~O\n"
"rO6#1\n"
"6*EX(\n"
"]S#i.\n"
"?qI=O\n"
"xUb8k\n"
"$/GMs\n"
"!MYc_\n"
"fGQ&H\n"
"UZkrr\n"
"VB>{X\n"
".Z2#N\n"
"X;]t9\n"
"P8Nx7\n"
"Bx@q)\n"
"RAZ7Q\n"
"Ur6lH\n"
"0@06U\n"
"29(xQ\n"
"2orIU\n"
"l-uu6\n"
")~)MN\n"
"GB5`]\n"
"{^]{c\n"
"uKiSI\n"
"9oI[M\n"
"45gx^\n"
";x(H~\n"
"Fy&YX\n"
"yS<Bs\n"
"u3yhl\n"
"u=s^1\n"
"YmDik\n"
"u,/q>\n"
"zsTqa\n"
")N[wv\n"
"u{}/[\n"
"8T4tU\n"
"ik3IU\n"
"4qC(L\n"
",oU@e\n"
"_`/!S\n"
"X&_@1\n"
"9)H@f\n"
",[/9'\n"
"#p+Gm\n"
"?}taB\n"
",!P56\n"
"nUF?H\n"
"^Nos0\n"
"E(C,H\n"
">AJ>8\n"
"A=]{q\n"
"3K%}r\n"
"p@ACJ\n"
"K;Os@\n"
"b^#I)\n"
"$si[q\n"
"ues+f\n"
"$hEs+\n"
"+ixod\n"
"$pcHO\n"
"Fu77%\n"
")OvAM\n"
"i~n6+\n"
"2-Iac\n"
">a/ws\n"
"mn')=\n"
"83%8/\n"
"R_P!Q\n"
"*i,ND\n"
"TiGR!\n"
"qkSV8\n"
"'SDlt\n"
"@2&`%\n"
"rh%6r\n"
"ugF%e\n"
"d*t8E\n"
"^vi.x\n"
"}t.Ay\n"
"M$v6d\n"
"^yNvp\n"
"o.#q'\n"
"o/+F~\n"
"O%SZO\n"
"!?,LM\n"
">`K/#\n"
"3Lb=6\n"
"#K(0q\n"
"d^v=S\n"
"e&LAG\n"
"Qk<Dc\n"
"bfIZ%\n"
"n4+a1\n"
"wpz/^\n"
"]DCFk\n"
"Iolw5\n"
"'FY*&\n"
"RZLon\n"
"~?_wU\n"
"A&xt,\n"
">kKw1\n"
"3q1Kc\n"
"`'cEz\n"
};
// ==================== //

// ===== Includes ===== //
#include <ESP8266WiFi.h>

extern "C" {
#include "user_interface.h"
  typedef void (*freedom_outside_cb_t)(uint8 status);
  int wifi_register_send_pkt_freedom_cb(freedom_outside_cb_t cb);
  void wifi_unregister_send_pkt_freedom_cb(void);
  int wifi_send_pkt_freedom(uint8 *buf, int len, bool sys_seq);
}
// ==================== //

// run-time variables
char emptySSID[32];
uint8_t channelIndex = 0;
uint8_t macAddr[6];
uint8_t wifi_channel = 1;
uint32_t currentTime = 0;
uint32_t packetSize = 0;
uint32_t packetCounter = 0;
uint32_t attackTime = 0;
uint32_t packetRateTime = 0;

// beacon frame definition
uint8_t beaconPacket[109] = {
  /*  0 - 3  */ 0x80, 0x00, 0x00, 0x00, // Type/Subtype: managment beacon frame
  /*  4 - 9  */ 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, // Destination: broadcast
  /* 10 - 15 */ 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, // Source
  /* 16 - 21 */ 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, // Source

  // Fixed parameters
  /* 22 - 23 */ 0x00, 0x00, // Fragment & sequence number (will be done by the SDK)
  /* 24 - 31 */ 0x83, 0x51, 0xf7, 0x8f, 0x0f, 0x00, 0x00, 0x00, // Timestamp
  /* 32 - 33 */ 0xe8, 0x03, // Interval: 0x64, 0x00 => every 100ms - 0xe8, 0x03 => every 1s
  /* 34 - 35 */ 0x31, 0x00, // capabilities Tnformation

  // Tagged parameters

  // SSID parameters
  /* 36 - 37 */ 0x00, 0x20, // Tag: Set SSID length, Tag length: 32
  /* 38 - 69 */ 0x20, 0x20, 0x20, 0x20,
  0x20, 0x20, 0x20, 0x20,
  0x20, 0x20, 0x20, 0x20,
  0x20, 0x20, 0x20, 0x20,
  0x20, 0x20, 0x20, 0x20,
  0x20, 0x20, 0x20, 0x20,
  0x20, 0x20, 0x20, 0x20,
  0x20, 0x20, 0x20, 0x20, // SSID

  // Supported Rates
  /* 70 - 71 */ 0x01, 0x08, // Tag: Supported Rates, Tag length: 8
  /* 72 */ 0x82, // 1(B)
  /* 73 */ 0x84, // 2(B)
  /* 74 */ 0x8b, // 5.5(B)
  /* 75 */ 0x96, // 11(B)
  /* 76 */ 0x24, // 18
  /* 77 */ 0x30, // 24
  /* 78 */ 0x48, // 36
  /* 79 */ 0x6c, // 54

  // Current Channel
  /* 80 - 81 */ 0x03, 0x01, // Channel set, length
  /* 82 */      0x01,       // Current Channel

  // RSN information
  /*  83 -  84 */ 0x30, 0x18,
  /*  85 -  86 */ 0x01, 0x00,
  /*  87 -  90 */ 0x00, 0x0f, 0xac, 0x02,
  /*  91 -  92 */ 0x02, 0x00,
  /*  93 - 100 */ 0x00, 0x0f, 0xac, 0x04, 0x00, 0x0f, 0xac, 0x04, /*Fix: changed 0x02(TKIP) to 0x04(CCMP) is default. WPA2 with TKIP not supported by many devices*/
  /* 101 - 102 */ 0x01, 0x00,
  /* 103 - 106 */ 0x00, 0x0f, 0xac, 0x02,
  /* 107 - 108 */ 0x00, 0x00
};

// goes to next channel
void nextChannel() {
  if(sizeof(channels) > 1){
    uint8_t ch = channels[channelIndex];
    channelIndex++;
    if (channelIndex > sizeof(channels)) channelIndex = 0;
  
    if (ch != wifi_channel && ch >= 1 && ch <= 14) {
      wifi_channel = ch;
      wifi_set_channel(wifi_channel);
    }
  }
}

// generates random MAC
void randomMac() {
  for (int i = 0; i < 6; i++)
    macAddr[i] = random(256);
}

void spamSetup() {
  // create empty SSID
  for (int i = 0; i < 32; i++)
    emptySSID[i] = ' ';

  // for random generator
  randomSeed(os_random());

  // set packetSize
  packetSize = sizeof(beaconPacket);
  if (wpa2) {
    beaconPacket[34] = 0x31;
  } else {
    beaconPacket[34] = 0x21;
    packetSize -= 26;
  }

  // generate random mac address
  randomMac();

  // start serial
  Serial.begin(115200);
  Serial.println();

  // get time
  currentTime = millis();

  // start WiFi
  WiFi.mode(WIFI_OFF);
  wifi_set_opmode(STATION_MODE);

  // set channel
  wifi_set_channel(channels[0]);

  // print out saved SSIDs
  Serial.println("SSIDs:");
  int i = 0;
  int len = sizeof(ssids);
  while(i < len){
    Serial.print((char)pgm_read_byte(ssids + i));
    i++;
  }
  
  Serial.println();
  Serial.println("Started \\o/");
  Serial.println();
}

void beaconSpam() {
  currentTime = millis();

  // send out SSIDs
  if (currentTime - attackTime > 100) {
    attackTime = currentTime;

    // temp variables
    int i = 0;
    int j = 0;
    int ssidNum = 1;
    char tmp;
    int ssidsLen = strlen_P(ssids);
    bool sent = false;
    
    // go to next channel
    nextChannel();

    while (i < ssidsLen) {
      // read out next SSID
      j = 0;
      do {
        tmp = pgm_read_byte(ssids + i + j);
        j++;
      } while (tmp != '\n' && j <= 32 && i + j < ssidsLen);

      uint8_t ssidLen = j - 1;
      
      // set MAC address
      macAddr[5] = ssidNum;
      ssidNum++;

      // write MAC address into beacon frame
      memcpy(&beaconPacket[10], macAddr, 6);
      memcpy(&beaconPacket[16], macAddr, 6);

      // reset SSID
      memcpy(&beaconPacket[38], emptySSID, 32);

      // write new SSID into beacon frame
      memcpy_P(&beaconPacket[38], &ssids[i], ssidLen);

      // set channel for beacon frame
      beaconPacket[82] = wifi_channel;

      // send packet
      if(appendSpaces){
        for(int k=0;k<3;k++){
          packetCounter += wifi_send_pkt_freedom(beaconPacket, packetSize, 0) == 0;
          delay(1);
        }
      }
      
      // remove spaces
      else {
        
        uint16_t tmpPacketSize = (packetSize - 32) + ssidLen; // calc size
        uint8_t* tmpPacket = new uint8_t[tmpPacketSize]; // create packet buffer
        memcpy(&tmpPacket[0], &beaconPacket[0], 38 + ssidLen); // copy first half of packet into buffer
        tmpPacket[37] = ssidLen; // update SSID length byte
        memcpy(&tmpPacket[38 + ssidLen], &beaconPacket[70], wpa2 ? 39 : 13); // copy second half of packet into buffer

        // send packet
        for(int k=0;k<3;k++){
          packetCounter += wifi_send_pkt_freedom(tmpPacket, tmpPacketSize, 0) == 0;
          delay(1);
        }

        delete tmpPacket; // free memory of allocated buffer
      }

      i += j;
    }
  }

  // show packet-rate each second
  if (currentTime - packetRateTime > 1000) {
    
     Serial.print(packetCounter);
    Serial.print(" / ");
    Serial.println(currentTime - packetRateTime);
    packetRateTime = currentTime;   
    packetCounter = 0;
  }
}



void setup(){
spamSetup();
}
void loop(){
beaconSpam();
}
