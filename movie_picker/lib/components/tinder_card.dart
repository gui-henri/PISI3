import 'package:flutter/material.dart';
import 'package:movie_picker/utils/card_provider.dart';
import 'package:provider/provider.dart';

class TinderCard extends StatefulWidget {

  final String urlImage;

  const TinderCard({super.key, required this.urlImage});

  @override
  State<TinderCard> createState() => _TinderCardState();
}

class _TinderCardState extends State<TinderCard> {
  @override
  Widget build(BuildContext context) {
    return SizedBox.expand(
      child: buildFrontCard(),
    );
  }

  Widget buildFrontCard() => GestureDetector(
    onPanStart: (details) {
      final provider = Provider.of<CardProvider>(context);
        provider.startPosition(details);
    },
    onPanUpdate: (details) {
      final provider = Provider.of<CardProvider>(context);
        provider.updatePosition(details);
    },
    onPanEnd: (details) {
      final provider = Provider.of<CardProvider>(context);
        // talvez precise adicionar o details mais tarde
        provider.endPosition();
    },
    child: Builder(
      builder: (context) {
        final provider = Provider.of<CardProvider>(context);
        final position = provider.position;
        const milliseconds = 0;

        return AnimatedContainer(
          curve: Curves.easeInOut,
          duration: const Duration(milliseconds: milliseconds),
          transform: Matrix4.identity()..translate(position.dx, position.dy),
          child: buildCard(),
        );
      },
    ),
  );

  Widget buildCard() => ClipRRect(
    borderRadius: BorderRadius.circular(20),
    child: Container(
      decoration: BoxDecoration(
         image: DecorationImage(
           image: NetworkImage(widget.urlImage),
           fit: BoxFit.cover,
           alignment: const Alignment(-0.3, 0),
        ),
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
        child: Container(
          padding: const EdgeInsets.all(20),
          child: Column(
            children: [
              const Spacer(),
              buildName(),
              const SizedBox(height: 8),
              buildDirector(),
          ],
          )
        )
      ),
    ),
  );

  //buildName
  Widget buildName() => Row(
      children: const [
        Text(
          "Rainha da cocada preta",
          style: TextStyle(
            fontSize: 32,
            color: Colors.white,
            fontWeight: FontWeight.bold,
          ),
        ),
        SizedBox(width: 16),
        Text(
          '2099',
          style: TextStyle(
            fontSize: 32,
            color: Colors.white,
          ),
        )
    ],); 

 Widget buildDirector() => Row(
  children: [
    Container(
      decoration: const BoxDecoration(
        shape: BoxShape.circle,
        color: Colors.white,
      ),
      width: 12,
      height: 12,
    ),
  const SizedBox(width: 8),
  const Text(
    'Nome do diretor',
    style: TextStyle(
      fontSize: 20,
      color:  Colors.white,),
     ),
   ],
  );
}



         