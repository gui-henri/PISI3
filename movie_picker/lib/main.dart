import 'package:flutter/material.dart';
import 'package:movie_picker/pages/login_page.dart';
import 'package:movie_picker/pages/start_page.dart';
import 'package:movie_picker/pages/main_page/main_page.dart';
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

