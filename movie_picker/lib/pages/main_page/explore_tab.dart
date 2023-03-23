import 'package:flutter/material.dart';
import '../../styles/default_background_decoration.dart';

class ExploreTab extends StatelessWidget {
  const ExploreTab({super.key});

  @override
  Widget build(BuildContext context) {
    final PageController pageController1 = PageController();

    final List<Widget> cards1 = List.generate(10, (index) {
      return Card(
        margin: const EdgeInsets.all(7),
        child: SizedBox(
          width: 50, //NÃO TÁ PEGANDOOOOOOOO
          child: Center(
            child: Text("Card ${index + 1}"),
          ),
        ),
      );
    });

    final List<Widget> cards2 = List.generate(50, (index) {
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
              "Assistir mais tarde",
              style: TextStyle(
                  fontSize: 18,
                  fontWeight: FontWeight.bold,
                  color: Colors.white),
            ),
          ),
          SizedBox(
            height: 130, //ALTURA PEGA NORMAL
            width: 50,
            child: PageView(
              controller: pageController1,
              children: cards1,
            ),
          ),
          const Padding(
            padding: EdgeInsets.all(8),
            child: Text(
              "Mais Populares",
              style: TextStyle(
                  fontSize: 18,
                  fontWeight: FontWeight.bold,
                  color: Colors.white),
            ),
          ),
          GridView.count(
              crossAxisCount: 3,
              shrinkWrap: true,
              physics: const NeverScrollableScrollPhysics(),
              children: cards2),
        ],
      ),
    ));
  }
}
