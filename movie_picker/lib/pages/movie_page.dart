import 'dart:math';

import 'package:auto_size_text/auto_size_text.dart';
import 'package:flutter/material.dart';
import 'package:movie_picker/services/firestore_services_provider.dart';
import 'package:movie_picker/styles/default_background_decoration.dart';
import 'package:movie_picker/models/movie.dart';
import 'package:movie_picker/services/tmdb_service_provider.dart';
import 'package:palette_generator/palette_generator.dart';

class MoviePage extends StatelessWidget {
  static const routeName = '/movie';
  const MoviePage({super.key});
  @override
  Widget build(BuildContext context) {
    final movie = ModalRoute.of(context)!.settings.arguments as Movie;
    final providers = TmdbServiceProvider().fetchMovieProviders(movie.id);
    final db = FiresStoreServiceProvider();
    return FutureBuilder<String>(
        future: providers,
        initialData: "Carregando...",
        builder: (BuildContext context, AsyncSnapshot<String> text) {
          return Scaffold(
              appBar: AppBar(
                backgroundColor: const Color.fromARGB(255, 31, 3, 88),
                title: const Text("Detalhes"),
                leading: IconButton(
                  onPressed: () => Navigator.pop(context),
                  icon: const Icon(Icons.arrow_back),
                ),
              ),
              body: Container(
                  decoration: mpDefaultBackgroundDecoration(),
                  child: Column(
                    children: [
                      Expanded(
                        child: Padding(
                          padding: const EdgeInsets.all(12),
                          child: Column(
                            children: [
                              SizedBox(
                                width: 387.4,
                                height: 300,
                                child: Row(
                                  mainAxisAlignment: MainAxisAlignment.start,
                                  crossAxisAlignment: CrossAxisAlignment.start,
                                  children: [
                                    Image.network(
                                        alignment: Alignment.topLeft,
                                        width: 185,
                                        "https://image.tmdb.org/t/p/w500${movie.posterPath}"),
                                    Expanded(
                                      child: Padding(
                                        padding: const EdgeInsets.fromLTRB(
                                            8, 0, 8, 0),
                                        child: Column(
                                          mainAxisAlignment:
                                              MainAxisAlignment.start,
                                          crossAxisAlignment:
                                              CrossAxisAlignment.start,
                                          children: [
                                            Padding(
                                              padding:
                                                  const EdgeInsets.fromLTRB(
                                                      0, 0, 0, 8),
                                              child: SizedBox(
                                                child: AutoSizeText(
                                                  movie.title,
                                                  style: const TextStyle(
                                                      color: Colors.white,
                                                      fontWeight:
                                                          FontWeight.bold,
                                                      fontSize: 14.5),
                                                ),
                                              ),
                                            ),
                                            const Text("Popularidade:",
                                                style: TextStyle(
                                                    color: Colors.white,
                                                    fontSize: 12)),
                                            Row(
                                              children: [
                                                const Padding(
                                                  padding: EdgeInsets.fromLTRB(
                                                      0, 4, 4, 8),
                                                  child: Icon(
                                                      Icons.analytics_outlined,
                                                      color: Colors.white),
                                                ),
                                                Text(
                                                    movie.popularity
                                                        .toStringAsFixed(0),
                                                    style: const TextStyle(
                                                        color: Colors.white)),
                                              ],
                                            ),
                                            const Text("Nota:",
                                                style: TextStyle(
                                                    color: Colors.white,
                                                    fontSize: 12)),
                                            Row(
                                              children: [
                                                const Padding(
                                                  padding: EdgeInsets.fromLTRB(
                                                      0, 4, 4, 8),
                                                  child: Icon(
                                                      Icons
                                                          .rate_review_outlined,
                                                      color: Colors.white),
                                                ),
                                                Text(
                                                    movie.voteAverage
                                                        .toStringAsFixed(1),
                                                    style: const TextStyle(
                                                        color: Colors.white)),
                                              ],
                                            ),
                                            const Text('Streams:',
                                                style: TextStyle(
                                                    color: Colors.white,
                                                    fontSize: 12)),
                                            Row(
                                              children: [
                                                const Padding(
                                                  padding: EdgeInsets.fromLTRB(
                                                      0, 4, 4, 8),
                                                  child: Icon(Icons.cast_sharp,
                                                      color: Colors.white),
                                                ),
                                                Flexible(
                                                  child: Text(
                                                    text.data.toString(),
                                                    style: const TextStyle(
                                                        color: Colors.white,
                                                        fontSize: 13),
                                                  ),
                                                ),
                                              ],
                                            ),
                                            Padding(
                                              padding:
                                                  const EdgeInsets.fromLTRB(
                                                      8, 0, 0, 0),
                                              child: Row(
                                                children: [
                                                  const IconButton(
                                                      alignment:
                                                          Alignment.topLeft,
                                                      onPressed: null,
                                                      icon: Icon(
                                                        Icons.favorite,
                                                        color: Colors.white,
                                                        size: 30,
                                                      )),
                                                  IconButton(
                                                      alignment:
                                                          Alignment.topLeft,
                                                      onPressed: () async {
                                                        db.adicionarFilme(
                                                            movie);
                                                      },
                                                      icon: const Icon(
                                                        Icons.add,
                                                        color: Colors.white,
                                                        size: 30,
                                                      )),
                                                ],
                                              ),
                                            ),
                                          ],
                                        ),
                                      ),
                                    ),
                                  ],
                                ),
                              ),
                              Padding(
                                padding: const EdgeInsets.fromLTRB(0, 0, 0, 0),
                                child: SingleChildScrollView(
                                    child: AutoSizeText(
                                  movie.overview,
                                  style: const TextStyle(
                                    color: Colors.white,
                                  ),
                                  minFontSize: 9,
                                  maxFontSize: 12,
                                  textAlign: TextAlign.justify,
                                )),
                              ),
                            ],
                          ),
                        ),
                      ),
                    ],
                  )));
        });
  }
}