import 'package:flutter/material.dart';
import 'package:movie_picker/models/movie.dart';
import 'package:movie_picker/services/firestore_services_provider.dart';
import 'package:movie_picker/services/tmdb_service_provider.dart';
import 'package:movie_picker/styles/default_background_decoration.dart';

import '../movie_page.dart';

class FavoritesTab extends StatefulWidget {
  const FavoritesTab({super.key});

  @override
  State<FavoritesTab> createState() => _FavoritesTabState();
}

class _FavoritesTabState extends State<FavoritesTab> {
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
                                          ? GestureDetector(
                                              onTap: () async {
                                                final provider =
                                                    TmdbServiceProvider();
                                                provider
                                                    .fetchMovieById(snapshot
                                                        .data![index].id
                                                        .toString())
                                                    .then((value) {
                                                  Navigator.pushNamed(context,
                                                      MoviePage.routeName,
                                                      arguments: value);
                                                });
                                              },
                                              child: Image.network(
                                                "https://image.tmdb.org/t/p/w500${snapshot.data![index].posterPath}",
                                                fit: BoxFit.fill,
                                              ),
                                            )
                                          : Image.network(
                                              "https://ih1.redbubble.net/image.1304795334.8057/fposter,small,wall_texture,product,750x1000.jpg",
                                              fit: BoxFit.fill,
                                            ),
                                      //Text(snapshot.data![index].title),
                                      Positioned(
                                          bottom: 5,
                                          right: 5,
                                          child: IconButton(
                                            onPressed: () async {
                                              await db.removerFilme(
                                                  snapshot.data![index]);
                                              setState(() {});
                                            },
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
