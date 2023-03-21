import 'package:flutter/material.dart';
import 'package:movie_picker/models/movie.dart';
import 'package:movie_picker/services/firestore_services_provider.dart';
import 'package:movie_picker/styles/default_background_decoration.dart';

class FavoritesTab extends StatelessWidget {
  const FavoritesTab({super.key});

  @override
  Widget build(BuildContext context) {

    final db = FiresStoreServiceProvider();

    final Future<List<Movie>> userMovies = db.obterFilmes();

    return FutureBuilder(
      future: userMovies,
      builder: (context, snapshot) {
        if (snapshot.connectionState == ConnectionState.done){
          return Scaffold(
            body: Ink(
              decoration: mpDefaultBackgroundDecoration(),
              child: GridView.builder(
                gridDelegate: const SliverGridDelegateWithMaxCrossAxisExtent(
                  maxCrossAxisExtent: 160,
                  childAspectRatio: 5 / 7,
                  crossAxisSpacing: 15,
                  mainAxisSpacing: 2),
                itemCount: snapshot.data!.length,
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
                      Text(snapshot.data![index].title),
                      IconButton(
                        onPressed: () {},
                        icon: const Icon(Icons.favorite,
                        color: Color.fromARGB(255, 218, 55, 43)),
                        padding: EdgeInsets.zero,
                          constraints: const BoxConstraints(),
                          splashRadius: 15,
                      )
                    ],
                  ),
                );
              })
            )
          );
        } else {
          return Container(
            decoration: mpDefaultBackgroundDecoration(),
            child: const Center(
              child: CircularProgressIndicator(),
            )
          );
        }
      }
    );
  }
}
