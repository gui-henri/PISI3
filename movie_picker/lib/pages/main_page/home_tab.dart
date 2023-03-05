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
      decoration: const BoxDecoration(
        image: DecorationImage(
          image: NetworkImage("https://www.lamoda.co.uk/media/amasty/webp/catalog/product/cache/5ed917d940d58a890691074cb8cdcf0c/c/m/cmv_0962_jpg.webp"), //aqui
          fit: BoxFit.cover,
          alignment: Alignment(-0.3, 0),
          )
      ),
      child: Container(
        decoration: const BoxDecoration(
          gradient: LinearGradient(
            colors: [Colors.transparent, Colors.black],
            begin: Alignment.topCenter,
            end: Alignment.bottomCenter,
            stops: [0.7, 1],
        )
      ),
      child: Container()
    ),
  ));

  Widget buildName() => Row(
    children: const [
      Text(
        "Chunky shoes",
        style: TextStyle(
          fontSize: 32,
          color: Colors.black,
          fontWeight: FontWeight.bold,
        ),
      ),
      SizedBox(width: 16),
      Text('{',
      style: TextStyle(
        fontSize: 32,
        color: Colors.black,
      ),
    ),
  ],
);

Widget buildDirector() => Container();
  
}