import 'package:flutter/material.dart';

class HomeTab extends StatelessWidget {
  const HomeTab({super.key});

  @override
  Widget build(BuildContext context) => ClipRRect(
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
    borderRadius: BorderRadius.circular(20),
    child: Container(
      decoration: BoxDecoration(
        image: DecorationImage(
          image: NetworkImage(), //aqui
          fit: BoxFit.cover,
          )
      )
      child: Container(
        padding: EdgeInsets.all(20),
        child: Column(children: [
          buildName(),
          ]
          ),
      ),
  )
  );

  Widget buildName() => Row(
    children: [
      Text(
        '${}',
        style: TextStyle(
          fontSize: 32,
          color: Colors.black,
          fontWeight: FontWeight.bold,
        ),
      )
      const SizedBox(width: 16),
    ],)
}