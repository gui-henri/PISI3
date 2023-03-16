import 'package:flutter/material.dart';
import 'package:movie_picker/components/tinder_card.dart';

class HomeTab extends StatelessWidget {
  const HomeTab({super.key});

  @override
  Widget build(BuildContext context) => Container(
    alignment: Alignment.center,
    padding: const EdgeInsets.all(16),
    child: const TinderCard(
      urlImage: "https://i.pinimg.com/236x/9d/5e/6c/9d5e6ccba128314dd3dfe59f404da6b6.jpg",
    )
  );
}

/*
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
        ),
      ),
      child: Container(
        padding: const EdgeInsets.all(20),
        child: Column(
          children: [
            const Spacer(),
            buildName(),
            const SizedBox(height: 8,),
            buildDirector(),
          ],
        ),
      ),
    ),
    ),
  );

  Widget buildName() => Row(
    children: const [
      Text(
        "Chunky shoes",
        style: TextStyle(
          fontSize: 32,
          color: Colors.white,
          fontWeight: FontWeight.bold,
        ),
      ),
      SizedBox(width: 16),
      Text('{',
      style: TextStyle(
        fontSize: 32,
        color: Colors.white,
      ),
    ),
  ],
);

Widget buildDirector() => Row(
  children: [
    Container(
      decoration: const BoxDecoration(
        shape: BoxShape.circle,
        color: Colors.white
      ),
      width: 12,
      height: 12,
    ),
    const SizedBox(width: 8,),
    const Text('diretor aqui', //aqui
    style: TextStyle(
      fontSize: 20, color: Colors.white
    ),
    )
  ],
);

Widget buildlogo() => Row(
      children: const [
        Icon(
          Icons.movie_creation, //aqui
          color: Colors.white,
          size: 36,
        )
      ],
);
  
 Widget buildbuttons() => Row(
  mainAxisAlignment: MainAxisAlignment.spaceEvenly,
  children: const [],
  );


*/ 