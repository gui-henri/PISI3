import 'package:flutter/material.dart';

BoxDecoration mpDefaultBackgroundDecoration() {
    return const BoxDecoration(
      gradient: LinearGradient(
        colors: [
          Color.fromARGB(255, 20, 42, 99), 
          Color.fromARGB(255, 38, 17, 35)
          ],
          begin: Alignment.topCenter,
          end: Alignment.bottomCenter
      )
    );
  }