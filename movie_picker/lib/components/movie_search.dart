import 'dart:convert';

import 'package:flutter/material.dart';
import 'package:movie_picker/components/movie_search_results.dart';
import 'package:movie_picker/styles/default_background_decoration.dart';
import 'package:http/http.dart' as http;
import 'package:movie_picker/utils/movie.dart';

class MovieSearch extends SearchDelegate {

  Future<List<Movie>> fetchMovies(String query, BuildContext context) async {
    try {
      if (query.isNotEmpty) {
      String ulr = 'https://api.themoviedb.org/3/search/movie?api_key=TMDB_API_KEY&query=$query';
      final response = await http.get(Uri.parse(ulr));
      if(response.statusCode == 200) {
        final json = jsonDecode(response.body);
        return Movie.fromJsonToObjectList(json['results']);
      } else {
        throw Exception('Failed to load movie search. The server did not responded with status code 200.');
        }
      }
    } catch (e) {
      final errorMessage = e.toString();
      showDialog(
        context: context, 
        builder: ((context) {
          return AlertDialog(
            title: const Text("Error"),
            content: SingleChildScrollView(
              child: ListBody(
                children: <Widget>[
                  Text("An error ocourred during the search. This is the error message: $errorMessage")
                ],
              ),
            ),
          );
        })
      );
    }
    return <Movie>[];
  }

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
      future: fetchMovies(query, context),
      builder: ((context, snapshot) {
        if (snapshot.connectionState == ConnectionState.done) {
          return MovieSearchResults(
            itemCount: snapshot.data!.length,
            movies: snapshot.data!,
            onSelectMovie: (movie) {
              close(context, movie);  // Retornando o filme selecionado para a p??gina principal.
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