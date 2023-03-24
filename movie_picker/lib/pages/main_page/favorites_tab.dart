import 'package:flutter/material.dart';
import 'package:movie_picker/models/movie.dart';
import 'package:movie_picker/services/firestore_services_provider.dart';
import 'package:movie_picker/styles/default_background_decoration.dart';

class FavoritesTab extends StatelessWidget {
  const FavoritesTab({super.key});

  @override
  Widget build(BuildContext context) {
    //final movie = ModalRoute.of(context)!.settings.arguments as Movie;
    final db = FiresStoreServiceProvider();

    final Future<List<Movie>> userMovies = db.obterFilmes();

    return FutureBuilder(
        future: userMovies,
        builder: (context, snapshot) {
          if (snapshot.connectionState == ConnectionState.done) {
            return Scaffold(
                body: Ink(
                    decoration: mpDefaultBackgroundDecoration(),
                    child: GridView.builder(
                        gridDelegate:
                            const SliverGridDelegateWithMaxCrossAxisExtent(
                                maxCrossAxisExtent: 140,
                                childAspectRatio: 0.65,
                                crossAxisSpacing: 4,
                                mainAxisSpacing: 2),
                        itemCount: snapshot.data!.length,
                        itemBuilder: (BuildContext ctx, index) {
                          return Container(
                              margin: const EdgeInsets.all(7.5),
                              alignment: Alignment.bottomRight,
                              decoration: BoxDecoration(
                                  color: Colors.transparent,
                                  borderRadius: BorderRadius.circular(10)),
                              child: Column(
                                mainAxisAlignment:
                                    MainAxisAlignment.spaceBetween,
                                children: [
                                  Stack(
                                    children: [
                                      snapshot.data != null
                                          ? Image.network(
                                              "https://image.tmdb.org/t/p/w500${snapshot.data![index].posterPath}",
                                              fit: BoxFit.fill,
                                            )
                                          : Image.asset(
                                              "movie_picker/lib/styles/image-placeholder.png",
                                              fit: BoxFit.fill,
                                            ),
                                      //Text(snapshot.data![index].title),
                                      Positioned(
                                          bottom: 5,
                                          right: 5,
                                          child: IconButton(
                                            onPressed: () {},
                                            icon: const Icon(Icons.favorite,
                                                color: Color.fromARGB(
                                                    255, 201, 43, 32)),
                                            padding: EdgeInsets.zero,
                                            constraints: const BoxConstraints(),
                                            splashRadius: 15,
                                            iconSize: 22,
                                          ))
                                    ],
                                  )
                                ],
                              ));
                        })));
          } else {
            return Container(
                decoration: mpDefaultBackgroundDecoration(),
                child: const Center(
                  child: CircularProgressIndicator(),
                ));
          }
        });
  }
}
