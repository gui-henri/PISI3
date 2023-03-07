import 'package:flutter/material.dart';
import 'package:movie_picker/styles/default_background_decoration.dart';

class FavoritesTab extends StatelessWidget {
  const FavoritesTab({super.key});

  @override
  Widget build(BuildContext context) {
    final List<Map> myProducts =
        List.generate(5000, (index) => {"id": index, "name": "Movie $index"})
            .toList();

    return Scaffold(
        body: Ink(
            decoration: mpDefaultBackgroundDecoration(),
            child: GridView.builder(
                gridDelegate: const SliverGridDelegateWithMaxCrossAxisExtent(
                    maxCrossAxisExtent: 160,
                    childAspectRatio: 5 / 7,
                    crossAxisSpacing: 15,
                    mainAxisSpacing: 2),
                itemCount: myProducts.length,
                itemBuilder: (BuildContext ctx, index) {
                  return Container(
                    margin: const EdgeInsets.all(7),
                    alignment: Alignment.bottomRight,
                    decoration: BoxDecoration(
                        color: const Color.fromARGB(255, 255, 255, 255),
                        borderRadius: BorderRadius.circular(10)),
                    child: Column(
                      mainAxisAlignment: MainAxisAlignment.spaceBetween,
                      children: [
                        Text(myProducts[index]["name"]),
                        IconButton(
                          onPressed: () {},
                          icon: const Icon(Icons.favorite, color: Colors.red),
                          padding: EdgeInsets.zero,
                          constraints: const BoxConstraints(),
                          splashRadius: 15,
                        )
                      ],
                    ),
                  );
                })));
  }
}
