import 'package:flutter/material.dart';
import '../../styles/default_background_decoration.dart';

class ExploreTab extends StatelessWidget {
  const ExploreTab({super.key});

  @override
  Widget build(BuildContext context) {
    final List<Widget> cards = List.generate(50, (index) {
      return Card(
        margin: const EdgeInsets.all(7),
        child: SizedBox(
          child: Center(
            child: Text("Card ${index + 1}"),
          ),
        ),
      );
    });

    return Scaffold(
        body: Ink(
      decoration: mpDefaultBackgroundDecoration(),
      child: ListView(
        children: [
          const Padding(
            padding: EdgeInsets.all(8),
            child: Text(
              "Mais Populares",
              style: TextStyle(
                  fontSize: 24,
                  //fontWeight: FontWeight.bold,
                  color: Colors.white),
            ),
          ),
          GridView.count(
              crossAxisCount: 3,
              shrinkWrap: true,
              physics: const NeverScrollableScrollPhysics(),
              children: cards),
        ],
      ),
    ));
  }
}
