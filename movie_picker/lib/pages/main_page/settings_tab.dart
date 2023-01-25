import 'package:firebase_auth/firebase_auth.dart';
import 'package:flutter/material.dart';
import 'package:movie_picker/pages/login_page.dart';

class SettingsTab extends StatelessWidget {
  const SettingsTab({super.key});

  Future<void> handleLogOut() async {
    FirebaseAuth.instance.signOut();
  }

  @override
  Widget build(BuildContext context) {
    return Center(
      child: ElevatedButton(onPressed: () {
        final signOut =  handleLogOut();
        signOut.then((_) => Navigator.popAndPushNamed(context, LoginPage.routeName));
      }, child: const Text("Log out")),
    );
  }
}