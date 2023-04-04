import 'package:flutter/material.dart';
import 'package:movie_picker/services/tmdb_service_provider.dart';

import '../../models/movie.dart';

class ExploreTab extends StatelessWidget {
  const ExploreTab({super.key});

  @override
  Widget build(BuildContext context) {
    final ciel = TmdbServiceProvider();
    final Future<List<Movie>> lulaFazueli = ciel.fetchMostPopular();

    // chamar o método fetchMostPopular e armazenar numa lista

    FutureBuilder cardBuilder() {
      return FutureBuilder(
          future: lulaFazueli,
          builder: (context, snapshot) {
            if (snapshot.connectionState == ConnectionState.done) {
              final movieData = snapshot.data! as List<Movie>;
              return GridView.builder(
                  gridDelegate: const SliverGridDelegateWithMaxCrossAxisExtent(
                      maxCrossAxisExtent: 140,
                      childAspectRatio: 0.65,
                      crossAxisSpacing: 4,
                      mainAxisSpacing: 2),
                  itemCount: movieData.length,
                  itemBuilder: ((context, index) {
                    return Card(
                        child: Column(children: [
                      // Adicione a imagem aqui
                      Expanded(
                        child: Image.network(
                          "https://image.tmdb.org/t/p/w500${snapshot.data![index].posterPath}",
                          fit: BoxFit.cover,
                        ),
                      ),
                    ]));
                  }));
            } else {
              return const CircularProgressIndicator();
            }
          });
    }

    return Column(
      children: [
        const Padding(
          padding: EdgeInsets.all(8),
          child: Text(
            "Mais Populares",
            style: TextStyle(
                decoration: TextDecoration.none,
                fontSize: 22,
                //fontWeight: FontWeight.bold,
                color: Colors.white),
          ),
        ),
        Expanded(child: cardBuilder())
      ],
    );
  }
}