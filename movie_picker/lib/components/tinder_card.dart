import 'package:flutter/material.dart';
import 'package:movie_picker/utils/card_provider.dart';
import 'package:provider/provider.dart';

class TinderCard extends StatefulWidget {

  final String urlImage;
  final bool isFront;

  const TinderCard({super.key, required this.urlImage, required this.isFront});

  @override
  State<TinderCard> createState() => _TinderCardState();
}

class _TinderCardState extends State<TinderCard> {
  @override
  void initState() {
    super.initState();

    WidgetsBinding.instance.addPostFrameCallback((_) { 
      final size = MediaQuery.of(context).size;

      final provider = Provider.of<CardProvider>(context,listen: false);
      provider.setScreenSize(size);
    });
  }

  @override
  Widget build(BuildContext context) {
    return SizedBox.expand(
      child: widget.isFront ? buildFrontCard() : buildCard(),
    ); 
  }

  Widget buildFrontCard() => GestureDetector(
    onPanStart: (details) {
      final provider = Provider.of<CardProvider>(context, listen: false);
        provider.startPosition(details);
    },
    onPanUpdate: (details) {
      final provider = Provider.of<CardProvider>(context, listen: false);
        provider.updatePosition(details);
    },
    onPanEnd: (details) {
      final provider = Provider.of<CardProvider>(context, listen: false);
        // talvez precise adicionar o details mais tarde
        provider.endPosition();
    },
    child: LayoutBuilder(
      builder: (context, constraints) {
        final provider = Provider.of<CardProvider>(context);
        final position = provider.position;
        final milliseconds = provider.isDragging ? 0 : 400;
        
        //minuto 12:00 do vídeo aproximadamente
        final center = constraints.smallest.center(Offset.zero);
        final angle = provider.angle * 3.1415 /180;
        final rotatedMatrix = Matrix4.identity()
          ..translate(center.dx, center.dy)
          ..rotateZ(angle)
          ..translate(-center.dx, -center.dy);

        return AnimatedContainer(
          curve: Curves.easeInOut,
          duration: Duration(milliseconds: milliseconds),
          transform: rotatedMatrix..translate(position.dx, position.dy),
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
        Expanded(
          child: Text(
            "Rainha da cocada preta, 2099",
            maxLines: 3,
            overflow: TextOverflow.clip,
            style: TextStyle(
              fontSize: 32,
              color: Colors.white,
              fontWeight: FontWeight.bold,
              decoration: TextDecoration.none
            ),
          ),
        ),
      ],
    ); 

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
    'Beyoncé',
    style: TextStyle(
      fontSize: 20,
      decoration: TextDecoration.none,
      color:  Colors.white,
      ),
     ),
   ],
  );

}



         