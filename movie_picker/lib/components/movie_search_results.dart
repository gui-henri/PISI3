import 'package:flutter/material.dart';
import 'package:movie_picker/styles/default_background_decoration.dart';
import 'package:movie_picker/models/movie.dart';

class MovieSearchResults extends StatelessWidget {
  const MovieSearchResults({super.key, required this.itemCount, required this.movies, required this.onSelectMovie, this.selectedMovie, this.scrollKey = 'scroll-search'});

  final int itemCount;
  final List<Movie> movies;
  final Function(Movie) onSelectMovie;
  final Movie? selectedMovie;
  final String scrollKey;

  @override
  Widget build(BuildContext context) {
    return Container(
      decoration: mpDefaultBackgroundDecoration(),
      child: ListView.builder(
        controller: ScrollController(),
        itemCount: itemCount * 2,
        key: PageStorageKey(scrollKey),
        itemBuilder: ((context, index) {
          if (index.isOdd) {
            return const Divider(
              color: Colors.white,
            );
          }

          final treatedIndex = index ~/2;
    
          return GestureDetector(
            behavior: HitTestBehavior.opaque,
            onTap: () {
              onSelectMovie(movies[treatedIndex]); // a implementação dessa função receberá o filme através do parâmetro
            },
            child: Row(
              children: [
                (movies[treatedIndex].posterPath.isNotEmpty) ? 
                  Image.network(
                    height: 200,
                    width: 150,
                    "https://image.tmdb.org/t/p/w500${movies[treatedIndex].posterPath}"
                  ):
                  // TO DO: Substituir o widget abaixo por uma imagem fixa para caso o filme não tenha pôster 
                  const SizedBox(
                    width: 150,
                    height: 200,
                  ) 
                ,
                Flexible(
                  child: Padding(
                    padding: const EdgeInsets.fromLTRB(10, 10, 10, 10),
                    child: Column(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: [
                        Text(
                          movies[treatedIndex].title,
                          style: const TextStyle(
                            color: Colors.white,
                            fontFamily: "Roboto",
                            fontSize: 22
                          ),
                        ),
                        Text(
                            movies[treatedIndex].overview,
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
                  ),
                )
              ],
            ),
          );
        }),
      ),
    );
  }
}