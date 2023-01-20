import 'package:flutter/material.dart';
import 'package:movie_picker/components/movie_search_results.dart';
import 'package:movie_picker/controllers/movie_search_controller.dart';
import 'package:movie_picker/pages/movie_page.dart';
import 'package:movie_picker/styles/default_background_decoration.dart';

class MovieSearch extends SearchDelegate {

  MovieSearchController controller = MovieSearchController();

  @override
  ThemeData appBarTheme(BuildContext context) {
    return ThemeData(
      appBarTheme: const AppBarTheme(
        backgroundColor: Color.fromARGB(255, 31, 3, 88),
      ),
      textTheme: const TextTheme(
        headline6: TextStyle(
          fontSize: 18,
          color: Colors.white
        )
      ),
      inputDecorationTheme: const InputDecorationTheme(
        border: InputBorder.none,
        hintStyle: TextStyle(
          color: Colors.white60
        )
      )
    );
  }

  @override
  List<Widget>? buildActions(BuildContext context) {
    return [
      IconButton(
        icon: const Icon(Icons.clear),
        onPressed: () { 
          if (query.isEmpty) {
            close(context, null);
          } else {
            query = '';
          }
        }
      )
    ];
  }

  @override
  Widget? buildLeading(BuildContext context) {
    return IconButton(
      icon: const Icon(Icons.arrow_back),
      onPressed: () => close(context, null)
    );
  }

  @override
  Widget buildResults(BuildContext context) {
    if (query.isEmpty) {
      return Container(
        decoration: mpDefaultBackgroundDecoration(),
      );
    }
    return FutureBuilder(
      future: controller.searchMovieByQuery(query, context),
      builder: ((context, snapshot) {
        if (snapshot.connectionState == ConnectionState.done) {
          return MovieSearchResults(
            itemCount: snapshot.data!.data.length,
            movies: snapshot.data!.data,
            onSelectMovie: (movie) {
              Navigator.pushNamed(context, MoviePage.routeName, arguments: movie);  // Retornando o filme selecionado para a página principal.
            },
          );
        } else {
          return Container(
            decoration: mpDefaultBackgroundDecoration(),
            child: const Center(
              child: CircularProgressIndicator(),
            )
          );
        }
      }),
    );
  }

  @override
  Widget buildSuggestions(BuildContext context) {
    return Container(
      decoration: mpDefaultBackgroundDecoration(),
    );
  }
}