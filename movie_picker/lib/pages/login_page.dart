import 'package:flutter/material.dart';

class LoginPage extends StatelessWidget {
  const LoginPage({super.key});

  @override
  Widget build(BuildContext context) {

    void toStart() {
      Navigator.popAndPushNamed(context, '/');
    }
    
    return Container(
      decoration: const BoxDecoration(
        gradient: LinearGradient(
          colors: [
            Color.fromARGB(255, 20, 42, 99), 
            Color.fromARGB(255, 38, 17, 35)
            ],
            begin: Alignment.topCenter,
            end: Alignment.bottomCenter
        )
      ),
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