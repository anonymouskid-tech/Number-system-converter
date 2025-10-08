PROGRAM  DOCUMENTATION
SYSTEM OVERVIEW
This program converts numbers between the following no systems
Binary(base2)
Decimal(base10)
Octal(base8)
Hexadecimal(base16)
The user inputs a number and selects it’s base system.The system then automatically converts it to the required format.
SYSTEM ARCHITECTURE
1.Fronted UI
.Input fields for number and base selection
Display area for converted results
2.Backened (logic)
.Conversion algorithms(Decimal Binary Octal Hexadecimal)
2.Optional future feature
Store user history of conversions

SYSTEM DESIGN
DFD
.Focuses on how data moves across the system
.Shows inputs>processes >outputs
.User enters number >system validates>converts>outputs results

 DFD diagram 
  











CODE SNIPPET(PYTHON)EXAMPLE WITH FLET 
 
   
 

 


TESTING PLAN
.Unit tests are written for conversion functions to ensure accuracy
.Manual testing is perfomed on the UI for usability and corectness
DEPLOYMENT PLAN
The app is deployed to web Android and iOS platforfms.
.Export mobile app package(APK for Android,IPA for iOS)
.Test installation on real devices
.Deploy via GitHub

USER MANUAL
1.Open the app on Android or Ios.
2.Enter a number in the input box .
3.Select the base of the number(Binary,Decimal,Hexadecimal,Octal)
4.Press convert
5.View the results displayed



FINAL  OUTLOOK OF THE APP 

 
