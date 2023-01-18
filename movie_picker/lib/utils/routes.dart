import 'package:flutter/material.dart';
import 'package:movie_picker/pages/login_page.dart';
import 'package:movie_picker/pages/main_page/main_page.dart';
import 'package:movie_picker/pages/movie_page.dart';
import 'package:movie_picker/pages/start_page.dart';

// As rotas do app devem ser colocadas neste arquivo

Map<String, Widget Function(dynamic)> instanceRoutes(BuildContext context) => {
        '/': (context) => const StartPage(),
        '/login': (context) => const LoginPage(),
        '/main': (context) => const MainPage(),
        '/movie': (context) => const MoviePage()
};