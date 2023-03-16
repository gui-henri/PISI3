import 'package:firebase_core/firebase_core.dart';
import 'package:flutter/material.dart';
import 'package:flutter_dotenv/flutter_dotenv.dart';
import 'package:movie_picker/firebase_options.dart';
import 'package:movie_picker/utils/card_provider.dart';
import 'package:movie_picker/utils/routes.dart';
import 'package:provider/provider.dart';

Future main() async {
  await dotenv.load(fileName: ".env");
  await Firebase.initializeApp(
    options: DefaultFirebaseOptions.currentPlatform
  );
  Paint.enableDithering = true;
  runApp(const MoviePicker());
}

class MoviePicker extends StatelessWidget {
  const MoviePicker({super.key});

  @override
  Widget build(BuildContext context) {
    return ChangeNotifierProvider(
      create: (context) => CardProvider(),
      child: MaterialApp(
        title: 'Flutter Demo',
        initialRoute: '/',
        theme: ThemeData(
          primarySwatch: Colors.blue,
        ),
        routes: instanceRoutes(context),
      )
    );
  }
}
