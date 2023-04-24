import 'package:flutter/material.dart';
import 'package:movie_picker/pages/login_page.dart';
import 'package:movie_picker/pages/main_page/main_page.dart';
import 'package:movie_picker/pages/movie_page.dart';
import 'package:movie_picker/pages/start_page.dart';
import 'package:movie_picker/pages/watch_later.dart';

// As rotas do app devem ser colocadas neste arquivo

Map<String, Widget Function(dynamic)> instanceRoutes(BuildContext context) => {
        StartPage.routeName: (context) => const StartPage(),
        LoginPage.routeName: (context) => const LoginPage(),
        MainPage.routeName: (context) => const MainPage(),
        MoviePage.routeName: (context) => const MoviePage(),
        WatchLaterTab.routeName:(context) => const WatchLaterTab() 
};