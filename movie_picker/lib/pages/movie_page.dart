import 'package:flutter/material.dart';
import 'package:movie_picker/styles/default_background_decoration.dart';
import 'package:movie_picker/utils/movie.dart';

class MoviePage extends StatelessWidget {

  static const routeName = '/movie';

  const MoviePage({super.key});

  @override
  Widget build(BuildContext context) {

    final movie = ModalRoute.of(context)!.settings.arguments as Movie;

    return Container(
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
            child: ListView(
              children: [
                Text(movie.title),
                Text(movie.overview),
                Text(movie.popularity.toString()),
                Text(movie.voteAverage.toString())
              ],
            ),
          ),
        ],
      ),
    );
  }
}