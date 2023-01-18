import 'package:flutter/material.dart';
import '../styles/default_background_decoration.dart';

class LoginPage extends StatelessWidget {

  static const routeName = '/login';

  const LoginPage({super.key});

  @override
  Widget build(BuildContext context) {

    void toStart() {
      Navigator.popAndPushNamed(context, '/');
    }
    
    return Container(
      decoration: mpDefaultBackgroundDecoration(),
      child: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
             const Icon(Icons.movie_creation, color: Colors.white, size: 64),
             ElevatedButton(onPressed: toStart, child: const Text('return to SplashScreen'))
          ],
        ) 
      ),
    );
  }
}