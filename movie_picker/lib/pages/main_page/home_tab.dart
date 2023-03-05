import 'package:flutter/material.dart';

class HomeTab extends StatelessWidget {
  const HomeTab({super.key});

  @override
  Widget build(BuildContext context) => Container(
    /* return const Center(
      child: Text(
        "Home Tab",
        style: TextStyle(
          fontSize: 80,
          decorationStyle: TextDecorationStyle.dotted,
          decoration: TextDecoration.none
        ),
      ),
    ); */

    decoration: BoxDecoration(
      image: DecorationImage(
        image: NetworkImage(), //aqui
        fit: BoxFit.cover,
        )
    )
  );
}