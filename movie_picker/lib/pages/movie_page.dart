import 'package:auto_size_text/auto_size_text.dart';
import 'package:flutter/material.dart';
import 'package:movie_picker/styles/default_background_decoration.dart';
import 'package:movie_picker/models/movie.dart';

//"https://image.tmdb.org/t/p/w500${movie.posterPath}"

class MoviePage extends StatelessWidget {

  static const routeName = '/movie';

  const MoviePage({super.key});

  @override
  Widget build(BuildContext context) {

    final movie = ModalRoute.of(context)!.settings.arguments as Movie;

    return Scaffold(
      body:
      Container(
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
          Padding(
            padding: const EdgeInsets.all(12.0),
            child: Expanded(
              child:
                 Column(
                    children: [
                      Padding(
                        padding: const EdgeInsets.fromLTRB(0, 0, 0, 8),
                        child: SizedBox(
                          child: AutoSizeText(movie.title,
                              style: TextStyle(color: Colors.white, fontSize: 200),
                              maxLines: 1
                          ),
                        ),
                      ),
                      Row(
                        mainAxisAlignment: MainAxisAlignment.start,
                        children: [
                          Image.network(
                              alignment: Alignment.topLeft,
                              height: 300,
                              "https://image.tmdb.org/t/p/w500${movie.posterPath}"
                          ),
                          Column(
                            mainAxisAlignment: MainAxisAlignment.start,
                            children: [
                              Padding(
                                padding: const EdgeInsets.all(8.0),
                                child: Align(
                                  alignment: Alignment.topLeft,
                                  child: Text("Popularidade: " + movie.popularity.toString(), style: const TextStyle(color: Colors.white)
                                  ),
                                ),
                              ),
                              Padding(
                                padding: const EdgeInsets.all(8.0),
                                child: Align(
                                  alignment: Alignment.topLeft,
                                  child:
                                    Text("Média: " + movie.voteAverage.toString(),  style: const TextStyle(color: Colors.white)
                                    ),
                                ),
                              ),
                            ],
                          ),

                        ],
                      ),
                    Padding(
                      padding: const EdgeInsets.fromLTRB(0, 16, 0, 0),
                      child: Text(movie.overview, style: const TextStyle(color: Colors.white, fontSize: 20),
                  ),
                    ),
            ],
                 ),
              ),
          ),
          ],
    )
    )
    );
  }
}