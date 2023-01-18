import 'package:flutter/material.dart';
import 'package:movie_picker/utils/routes.dart';

void main() {
  Paint.enableDithering = true;
  runApp(const MoviePicker());
}

class MoviePicker extends StatelessWidget {
  const MoviePicker({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
      initialRoute: '/',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      routes: instanceRoutes(context),
    );
  }
}

