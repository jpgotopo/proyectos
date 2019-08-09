import 'package:flutter/material.dart';
import 'package:flutter/services.dart';

void main() => runApp(Login());

class Login extends StatelessWidget {
  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'PhoneAnalyzer',
      theme: ThemeData(

        primarySwatch: Colors.blue,
      ),
      home: LoginPage(),
    );
  }
}
class LoginPage extends StatefulWidget {
  @override
  State<StatefulWidget> createState(){
    return _LoginPageState();
  }
}
class _LoginPageState extends State<LoginPage>{
  //#2048E8, #061E7E
  @override
  void initState() {
    SystemChrome.setEnabledSystemUIOverlays([]);
    super.initState();
  }

  @override
  Widget build(BuildContext context){
    return Scaffold(
      body: Container(
        decoration: BoxDecoration(
          gradient: LinearGradient(
              begin:Alignment.center,
              end: Alignment.topRight,
              colors: [
                Color(0xFF2048E8),
                Color(0xFF061E7E)
              ],
          ),
        ),
      ), //Container
    );
  }

}