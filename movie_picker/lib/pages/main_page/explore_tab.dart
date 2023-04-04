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
          if(snapshot.connectionState == ConnectionState.done){
            final movieData = snapshot.data! as List<Movie>;
            return GridView.builder(
              gridDelegate: const SliverGridDelegateWithFixedCrossAxisCount(crossAxisCount: 3),
              itemCount: movieData.length,
              itemBuilder: ((context, index) {
                return Card(
                  margin: const EdgeInsets.all(7),
                  child: SizedBox(
                    child: Center(
                      child: Text(movieData[index].title),
                    ),
                  ),
                );
              }
            ));
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
              fontSize: 24,
              //fontWeight: FontWeight.bold,
              color: Colors.white),
            ),
        ),
        Expanded(child: cardBuilder())
      ],
    );
  }
}
