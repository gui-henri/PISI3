import 'package:flutter/material.dart';
import 'package:animated_text_kit/animated_text_kit.dart';
import '../styles/default_background_decoration.dart';

class StartPage extends StatelessWidget {
  const StartPage({super.key});

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
              onFinished: () => Navigator.popAndPushNamed(context, '/main'),
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