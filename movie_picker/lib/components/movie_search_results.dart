import 'package:flutter/material.dart';
import 'package:movie_picker/styles/default_background_decoration.dart';
import 'package:movie_picker/utils/movie.dart';

class MovieSearchResults extends StatelessWidget {
  const MovieSearchResults({super.key, required this.itemCount, required this.movies, required this.onSelectMovie, this.selectedMovie});

  final int itemCount;
  final List<Movie> movies;
  final Function(Movie) onSelectMovie;
  final Movie? selectedMovie;

  @override
  Widget build(BuildContext context) {
    return Container(
      decoration: mpDefaultBackgroundDecoration(),
      child: ListView.builder(
        itemCount: itemCount * 2,
        itemBuilder: ((context, index) {
          if (index.isOdd) {
            return const Divider(
              color: Colors.white,
            );
          }

          final treatedIndex = index ~/2;
          String? posterPath = movies[treatedIndex].posterPath;
          String? overview = movies[treatedIndex].overview ??  "Unavailable overview";

          if (posterPath != null) {
            return GestureDetector(
              onTap: () {
                onSelectMovie(movies[treatedIndex]); // a implementação dessa função receberá o filme através do parâmetro
              },
              child: Row(
                children: [
                  Image.network(
                    height: 200,
                    width: 150,
                    "https://image.tmdb.org/t/p/w500${movies[treatedIndex].posterPath}"
                  ),
                  Flexible(
                    child: Column(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: [
                        Text(
                          movies[treatedIndex].title,
                          style: const TextStyle(
                            color: Colors.white,
                            fontFamily: "Roboto",
                            fontSize: 24
                          ),
                        ),
                        Text(
                            overview,
                            maxLines: 3,
                            overflow: TextOverflow.ellipsis,
                            style: const TextStyle(
                              color: Colors.white,
                              fontFamily: "Roboto",
                              fontSize: 14
                            ),
                          ),
                      ],
                    ),
                  )
                ],
              ),
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