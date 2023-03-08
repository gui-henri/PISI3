import 'package:flutter/material.dart';

class ExploreTab extends StatelessWidget {
  const ExploreTab({super.key});

  @override
  Widget build(BuildContext context) {
    final PageController pageController1 = PageController();
    final PageController pageController2 = PageController();

    final List<Widget> cards1 = List.generate(10, (index) {
      return Card(
        child: SizedBox(
          height: 115,
          width: 82,
          child: Center(
            child: Text("Card ${index + 1}"),
          ),
        ),
      );
    });

    final List<Widget> cards2 = List.generate(10, (index) {
      return Card(
        child: SizedBox(
          height: 5,
          width: 5,
          child: Center(
            child: Text("Lista 2, Card ${index + 1}"),
          ),
        ),
      );
    });

    final List<Widget> cards3 = List.generate(52, (index) {
      return Card(
        child: SizedBox(
          height: 115,
          width: 82,
          child: Center(
            child: Text("Card ${index + 1}"),
          ),
        ),
      );
    });

    return Scaffold(
      body: ListView(
        children: [
          const Padding(
            padding: EdgeInsets.all(8.0),
            child: Text(
              "Principais escolhas",
              style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold),
            ),
          ),
          SizedBox(
            height: 150,
            child: PageView(
              controller: pageController1,
              children: cards1,
            ),
          ),
          const Padding(
            padding: EdgeInsets.all(8.0),
            child: Text(
              "Assistir mais tarde",
              style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold),
            ),
          ),
          SizedBox(
            height: 150,
            child: PageView(
              controller: pageController2,
              children: cards2,
            ),
          ),
          const Padding(
            padding: EdgeInsets.all(8.0),
            child: Text(
              "Outros Filmes",
              style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold),
            ),
          ),
          GridView.count(
            crossAxisCount: 3,
            shrinkWrap: true,
            physics: const NeverScrollableScrollPhysics(),
            children: cards3,
          ),
        ],
      ),
    );
  }
}
