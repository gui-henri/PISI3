import 'package:flutter/material.dart';
import 'package:movie_picker/utils/card_provider.dart';
import 'package:provider/provider.dart';

class TinderCard extends StatefulWidget {
  final String urlImage;
  final String title;
  final Future<String> director;
  final bool isFront;

  const TinderCard({Key? key, required this.urlImage, required this.isFront, required this.title, required this.director})
      : super(key: key);

  @override
  State<TinderCard> createState() => _TinderCardState();
}

class _TinderCardState extends State<TinderCard> {
  @override
  void initState() {
    super.initState();

    WidgetsBinding.instance.addPostFrameCallback((_) {
      final size = MediaQuery.of(context).size;

      final provider = Provider.of<CardProvider>(context, listen: false);
      provider.setScreenSize(size);
    });
  }

  @override
  Widget build(BuildContext context) {
    return SizedBox.expand(
      child: widget.isFront ? buildFrontCard() : buildCard(widget.director),
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
            final angle = provider.angle * 3.1415 / 180;
            final rotatedMatrix = Matrix4.identity()
              ..translate(center.dx, center.dy)
              ..rotateZ(angle)
              ..translate(-center.dx, -center.dy);

            return AnimatedContainer(
                curve: Curves.easeInOut,
                duration: Duration(milliseconds: milliseconds),
                transform: rotatedMatrix..translate(position.dx, position.dy),
                child: Stack(children: [
                  buildCard(widget.director),
                  buildStamps(),
                ]));
          },
        ),
      );

  Widget buildCard(Future<String> director) => ClipRRect(
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
              )),
              child: Container(
                  padding: const EdgeInsets.all(20),
                  child: Column(
                    children: [
                      const Spacer(),
                      buildName(),
                      const SizedBox(height: 8),
                      buildDirector(director),
                    ],
                  ))),
        ),
      );

  //buildName
  Widget buildName() => Row(
        children: [
          Expanded(
            child: Text(
              widget.title,
              maxLines: 3,
              overflow: TextOverflow.clip,
              style: const TextStyle(
                  fontSize: 32,
                  color: Colors.white,
                  fontWeight: FontWeight.bold,
                  decoration: TextDecoration.none),
            ),
          ),
        ],
      );

  Widget buildDirector(Future<String> director) => 
    FutureBuilder(
      future: director,
      builder: (context, snapshot) {
        if(snapshot.connectionState == ConnectionState.done) {
          return Row(
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
            Text(
              snapshot.data!,
              style:const TextStyle(
                fontSize: 20,
                decoration: TextDecoration.none,
                color: Colors.white,
                ),
              ),
            ],
        );
        } else {
          return const Text('Obtendo diretor...');
        }
      }
    );
      

  Widget buildStamps() {
    //final provider = Provider.of<CardProvider>(context);
    final status = Provider.of<CardProvider>(context).status;

    switch (status) {
      case CardStatus.favorite:
        final child =
            buildStamp(angle: -0.5, color: Colors.green, text: 'FAVORITE');

        return Positioned(top: 64, left: 50, child: child);

      case CardStatus.nope:
        final child = buildStamp(color: Colors.red, text: 'NOPE');

        return Positioned(top: 64, right: 50, child: child);

      case CardStatus.watchLater:
        final child = Center(
          child: buildStamp(color: Colors.blue, text: 'WATCH/nLATER'),
        );

        return Positioned(top: 64, right: 0, left: 0, child: child);

      default:
        return Container();
    }
  }

  Widget buildStamp({
    double angle = 0,
    required Color color,
    required String text,
  }) {
    return Transform.rotate(
        angle: angle,
        child: Container(
            padding: const EdgeInsets.symmetric(horizontal: 8),
            decoration: BoxDecoration(
              borderRadius: BorderRadius.circular(12),
              border: Border.all(color: color, width: 4),
            ),
            child: Text(
              text,
              textAlign: TextAlign.center,
              style: TextStyle(
                color: color,
                fontSize: 48,
                fontWeight: FontWeight.bold,
              ),
            )));
  }
}
