import 'package:firebase_auth/firebase_auth.dart';
import 'package:flutter/material.dart';
import 'package:animated_text_kit/animated_text_kit.dart';
import 'package:movie_picker/pages/login_page.dart';
import 'package:movie_picker/pages/main_page/main_page.dart';
import '../styles/default_background_decoration.dart';

class StartPage extends StatefulWidget {
  static const routeName = '/';

  const StartPage({super.key});

  @override
  State<StartPage> createState() => _StartPageState();
}

class _StartPageState extends State<StartPage> {

  handleNavigation() {
    final user = FirebaseAuth.instance.currentUser;
    if (user != null) {
      Navigator.popAndPushNamed(context, MainPage.routeName, arguments: user);
    } else {
      Navigator.popAndPushNamed(context, LoginPage.routeName);
    }
  }

  @override
  Widget build(BuildContext context) {
    return Container(
      decoration: mpDefaultBackgroundDecoration(),
      child: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            const Icon(Icons.movie_creation, color: Colors.white, size: 64),
            AnimatedTextKit(
              totalRepeatCount: 1,
              onFinished: handleNavigation,
              animatedTexts: [
                TyperAnimatedText(
                  speed: const Duration(milliseconds: 115),
                  'MoviePicker',
                  textStyle: const TextStyle(
                    fontSize: 48,
                    color: Colors.white,
                    fontFamily: "Roboto",
                    decoration: TextDecoration.none
                  )
                )
              ],
            )
          ],
        ) 
      ),
    );
  }
}