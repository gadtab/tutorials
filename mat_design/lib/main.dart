import 'package:flutter/material.dart';
import 'package:css_colors/css_colors.dart';
import 'package:mat_design/screens/kittens.dart';
//import 'package:firebase_storage/firebase_storage.dart';

void main() => runApp(new MyApp());

class MyApp extends StatelessWidget {
  const MyApp();

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Navigation',
      theme: ThemeData(
        primarySwatch: Colors.purple,
        buttonColor: CSSColors.purple,
        buttonTheme: const ButtonThemeData(
          textTheme: ButtonTextTheme.primary,
        ),
      ),
      routes: <String, WidgetBuilder> {
        '/Kittens': (BuildContext context) => new Kittens(),
      },
      home: new Kittens(),
    );
  }
}

