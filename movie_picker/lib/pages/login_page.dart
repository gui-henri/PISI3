import 'package:firebase_auth/firebase_auth.dart';
import 'package:flutter/material.dart';
import 'package:google_sign_in/google_sign_in.dart';
import '../styles/default_background_decoration.dart';
import 'main_page/main_page.dart';

class LoginPage extends StatelessWidget {

  static const routeName = '/login';

  const LoginPage({super.key});

  @override
  Widget build(BuildContext context) {

    Future<UserCredential> signInWithGoogle() async {
      final GoogleSignInAccount? googleUser = await GoogleSignIn().signIn();
      final GoogleSignInAuthentication? googleAuth = await googleUser?.authentication;
      final credential = GoogleAuthProvider.credential(
        accessToken: googleAuth?.accessToken,
        idToken: googleAuth?.idToken,
      );
      return await FirebaseAuth.instance.signInWithCredential(credential);
    }

    Future<void> googleLogin() async {
      signInWithGoogle().then((UserCredential result) {
        final user = result.user;
        if (user != null) {
          Navigator.popAndPushNamed(context, MainPage.routeName, arguments: user);
        }
      });
    }
    
    return Container(
      decoration: mpDefaultBackgroundDecoration(),
      child: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
             const Icon(Icons.movie_creation, color: Colors.white, size: 64),
             ElevatedButton(onPressed: googleLogin, child: const Text('Try login with Google'))
          ],
        ) 
      ),
    );
  }
}