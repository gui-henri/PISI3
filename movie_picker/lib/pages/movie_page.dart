import 'package:auto_size_text/auto_size_text.dart';
import 'package:flutter/material.dart';
import 'package:movie_picker/styles/default_background_decoration.dart';
import 'package:movie_picker/utils/movie.dart';

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
            leading: IconButton(
              onPressed: () => Navigator.pop(context), 
              icon: const Icon(Icons.arrow_back),
            ),
          ),
          Expanded(
            child: ListView(
              children: [
                Row(
                  children: [
                      Image.network(
                        alignment: Alignment.topLeft,
                        height: 500,
                        "https://image.tmdb.org/t/p/w500${movie.posterPath}"
                    ),
                    Expanded(
                      child:
                        AutoSizeText(movie.title,  style: TextStyle(color: Colors.white, fontSize: 200), maxLines: 1)
                        ),
                      ],
                    ),
                Text(movie.popularity.toString(), style: TextStyle(color: Colors.white)),
                Text(movie.voteAverage.toString(), style: TextStyle(color: Colors.white)),
                Text(movie.overview, style: TextStyle(color: Colors.white, fontSize: 20), )
              ],
            ),
          ),
        ],
      ),
    )
    );
  }
}