import 'package:flutter/material.dart';
import 'package:movie_picker/styles/default_background_decoration.dart';
import 'package:movie_picker/utils/movie.dart';

class MovieSearchResults extends StatelessWidget {
  const MovieSearchResults({super.key, required this.itemCount, required this.movies});

  final int itemCount;
  final List<Movie> movies;

  @override
  Widget build(BuildContext context) {
    return Container(
      decoration: mpDefaultBackgroundDecoration(),
      child: ListView.builder(
        itemCount: itemCount,
        itemBuilder: ((context, index) {
          String? posterPath = movies[index].posterPath;
          if (posterPath != null) {
            return Row(
              children: [
                Image.network(
                  height: 200,
                  width: 150,
                  "https://image.tmdb.org/t/p/w500${movies[index].posterPath}"
                )
              ],
            );
          }
          return Row(
            children: const [
               Text("Image unavailable")
            ],
          );
        }),
      ),
    );
  }
}