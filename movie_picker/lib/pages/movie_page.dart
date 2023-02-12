import 'package:auto_size_text/auto_size_text.dart';
import 'package:flutter/material.dart';
import 'package:movie_picker/styles/default_background_decoration.dart';
import 'package:movie_picker/models/movie.dart';
import 'package:movie_picker/services/tmdb_service_provider.dart';

class MoviePage extends StatelessWidget {
  static const routeName = '/movie';

  const MoviePage({super.key});

  @override
  Widget build(BuildContext context) {
    final movie = ModalRoute.of(context)!.settings.arguments as Movie;
    final providers = TmdbServiceProvider().fetchMovieProviders(movie.id);

    return FutureBuilder<List>(
        future: providers,
        initialData: const ["Carregando..."],
        builder: (BuildContext context, AsyncSnapshot<List> text) {
          return Scaffold(
              body: Container(
                  decoration: mpDefaultBackgroundDecoration(),
                  child: Column(
                    children: [
                      AppBar(
                        backgroundColor: const Color.fromARGB(255, 31, 3, 88),
                        title: const Text("Detalhes"),
                        leading: IconButton(
                          onPressed: () => Navigator.pop(context),
                          icon: const Icon(Icons.arrow_back),
                        ),
                      ),
                      Expanded(
                        child: Padding(
                          padding: const EdgeInsets.all(12.0),
                          child: Column(
                            children: [
                              Padding(
                                padding: const EdgeInsets.fromLTRB(0, 0, 0, 8),
                                child: SizedBox(
                                  child: AutoSizeText(movie.title,
                                      style: const TextStyle(
                                          color: Colors.white, fontSize: 40),
                                      maxLines: 1),
                                ),
                              ),
                              SizedBox(
                                child: Row(
                                  mainAxisAlignment: MainAxisAlignment.start,
                                  crossAxisAlignment: CrossAxisAlignment.start,
                                  children: [
                                    Image.network(
                                        alignment: Alignment.topLeft,
                                        height: 300,
                                        "https://image.tmdb.org/t/p/w500${movie.posterPath}"),
                                    Column(
                                      mainAxisAlignment: MainAxisAlignment.start,
                                      crossAxisAlignment: CrossAxisAlignment.start,
                                      children: [
                                        Text("Popularidade:",
                                            style: const TextStyle(
                                                color: Colors.white)),
                                        Row(
                                          children: [
                                            Icon(
                                                Icons.analytics_outlined,
                                                color: Colors.white),
                                            Text(movie.popularity.toString(),
                                                style: const TextStyle(
                                                    color: Colors.white)),
                                          ],
                                        ),
                                        Text("Nota:",
                                            style: const TextStyle(
                                                color: Colors.white)),
                                        Row(
                                          children: [
                                            Icon(Icons.auto_awesome,
                                                color: Colors.white),
                                            Text(movie.voteAverage.toString(),
                                                style: const TextStyle(
                                                    color: Colors.white)),
                                          ],
                                        ),
                                        Row(
                                          children: [
                                            Icon(Icons.cast_sharp,
                                                color: Colors.white),
                                            Text(text.data.toString(),
                                                style: const TextStyle(
                                                    color: Colors.white,),
                                            ),
                                          ],
                                        ),
                                      ],
                                    ),
                                  ],
                                ),
                              ),
                              Padding(
                                padding: const EdgeInsets.fromLTRB(0, 16, 0, 0),
                                child: Text(
                                  movie.overview,
                                  style: const TextStyle(
                                      color: Colors.white, fontSize: 20),
                                ),
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
